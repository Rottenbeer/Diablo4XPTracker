import logging
import csv

from datetime import timedelta
from typing import Optional, List


from .configreader import ConfigReader
from .levelinfo import LevelInfo
from .ocrextract import XPExtractor


class Dungeon:
    def __init__(self) -> None:
        self.name = "Unknown Dungeon"
        self.start_state: Optional[LevelInfo] = None
        self.end_state: Optional[LevelInfo] = None
        self.farming_duration: timedelta = timedelta(seconds=0)
        self.summary = ""
        self.xp_gained = 0
        self.xp_hour = 0.0

    def set_start(self, levelinfo: LevelInfo) -> None:
        self.start_state = levelinfo

    def set_end(self, levelinfo: LevelInfo) -> None:
        self.end_state = levelinfo

    def calc_xp_per_hour(self, xpgained: int, duration: timedelta) -> float:
        seconds = duration.total_seconds()
        seconds_hour = 60 * 60
        xp_hour = (seconds_hour / seconds) * xpgained
        return xp_hour

    def calc_xp_info(self) -> None:
        self.xp_gained = 0
        if self.start_state is None:
            return
        if self.end_state is None:
            return
        if self.start_state.level == self.end_state.level:
            xpgained = self.end_state.xp_current - self.start_state.xp_current
        else:
            xp_gained_previous_level = (
                self.start_state.xp_max - self.start_state.xp_current
            )
            xp_gained_current_level = self.end_state.xp_current
            xpgained = xp_gained_current_level + xp_gained_previous_level

        self.xp_gained = xpgained
        self.farming_duration = (
            self.end_state.time_captured - self.start_state.time_captured
        )
        self.xp_hour = self.calc_xp_per_hour(self.xp_gained, self.farming_duration)

        if self.start_state.level == self.end_state.level:
            self.summary = f"Gained {self.xp_gained:,} XP in {self.name}. It took {self.farming_duration} XP/H: {self.xp_hour:,.2f}!"
        else:
            self.summary = f"Leveled up from {self.start_state.level} to {self.end_state.level} in {self.name} and gained {self.xp_gained:,} XP. It took {self.farming_duration} XP/H: {self.xp_hour:,.2f}!"

    def log_dungeon_info(self) -> None:
        logging.info(self.summary)


class DungeonManager:
    def __init__(self, config: ConfigReader, ocrextractor: XPExtractor) -> None:
        self._config = config
        self._is_running: bool = False
        self._ocrextractor: XPExtractor = ocrextractor
        self._current_dungeon: Optional[Dungeon] = None
        self._completed_dungeons: List[Dungeon] = []
        self._already_parsed_files: List[str] = []

    def _start_new_dungeon(self, dungeon_name: str, levelinfo: LevelInfo) -> None:
        # A new dungeon started
        logging.info(
            f"Started a new dungeon {dungeon_name} with level {levelinfo.level}, {levelinfo.xp_current}"
        )
        dungeon = Dungeon()
        dungeon.name = dungeon_name
        dungeon.set_start(levelinfo)
        self._current_dungeon = dungeon

    def _end_current_dungeon(self, levelinfo: LevelInfo) -> None:
        # A dungeon ended
        if self._current_dungeon is not None:
            logging.info(
                f"Ended a dungeon {self._current_dungeon.name} with level {levelinfo.level}, {levelinfo.xp_current}"
            )
            self._current_dungeon.set_end(levelinfo)
            self._current_dungeon.calc_xp_info()
            self._current_dungeon.log_dungeon_info()
            self._completed_dungeons.append(self._current_dungeon)
        self._current_dungeon = None

    def dungeon_event_callback(self, path: str) -> None:
        levelinfo = self._ocrextractor.extract_xp(path)
        dungeon_name = self._ocrextractor.extract_name(path)
        if not levelinfo:
            logging.debug(f"Failed to parse level information for {path}")
            return
        if path in self._already_parsed_files:
            logging.debug(f"Already, processed this file, skipping {path}")
            return
        self._already_parsed_files.append(path)
        if not self._current_dungeon:
            self._start_new_dungeon(dungeon_name, levelinfo)
        else:
            self._end_current_dungeon(levelinfo)

    def dump_dungeons(self) -> None:
        with open(self._config.output_csv, "a", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            for i in self._completed_dungeons:
                logging.info(i.summary)
                if i.start_state is None:
                    continue
                if i.end_state is None:
                    continue
                writer.writerow(
                    (
                        i.name,
                        i.start_state.level,
                        i.start_state.xp_current,
                        i.start_state.time_captured,
                        i.end_state.level,
                        i.end_state.xp_current,
                        i.end_state.time_captured,
                        i.xp_gained,
                        i.farming_duration,
                        i.xp_hour,
                    )
                )

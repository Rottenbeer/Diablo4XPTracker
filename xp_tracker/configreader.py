import configparser
import logging
import sys

from typing import List


class ConfigReader:
    def __init__(self, configpath: str) -> None:
        config = configparser.ConfigParser()
        config.read(configpath)

        for i in [
            "Paths",
            "Coordinates",
        ]:
            if i not in config:
                logging.error("%s missing in config.ini", i)
                sys.exit(-1)

        for i in [
            "D4ScreenshotPath",
            "TesseractExecutable",
            "OutputCSV",
        ]:
            if i not in config["Paths"]:
                logging.error("%s missing in config.ini", i)
                sys.exit(-1)

        for i in [
            "DungeonNameCoordinates",
            "XPBoxCoordinates",
        ]:
            if i not in config["Coordinates"]:
                logging.error("%s missing in config.ini", i)
                sys.exit(-1)

        self._screenshot_path = config["Paths"]["D4ScreenshotPath"]
        self._tesseract_exe = config["Paths"]["TesseractExecutable"]
        self._output_csv = config["Paths"]["OutputCSV"]
        self._dungeon_name_coordinates = [
            int(i) for i in config["Coordinates"]["DungeonNameCoordinates"].split(",")
        ]
        self._xp_box_coordinates = [
            int(i) for i in config["Coordinates"]["XPBoxCoordinates"].split(",")
        ]
        if len(self._dungeon_name_coordinates) != 4:
            logging.error(
                "Expected 4 coordinates in XPBoxCoordinates and DungeonNameCoordinates"
            )
            sys.exit(-1)
        if len(self._xp_box_coordinates) != 4:
            logging.error(
                "Expected 4 coordinates in XPBoxCoordinates and DungeonNameCoordinates"
            )
            sys.exit(-1)

    @property
    def screenshot_path(self) -> str:
        return self._screenshot_path

    @screenshot_path.setter
    def screenshot_path(self, _) -> None:
        raise AttributeError("Read-only attribute")

    @property
    def tesseract_exe(self) -> str:
        return self._tesseract_exe

    @tesseract_exe.setter
    def tesseract_exe(self, _) -> None:
        raise AttributeError("Read-only attribute")

    @property
    def output_csv(self) -> str:
        return self._output_csv

    @output_csv.setter
    def output_csv(self, _) -> str:
        raise AttributeError("Read-only attribute")

    @property
    def dungeon_name_coordinates(self) -> List[int]:
        return self._dungeon_name_coordinates

    @dungeon_name_coordinates.setter
    def dungeon_name_coordinates(self, _) -> None:
        raise AttributeError("Read-only attribute")

    @property
    def xp_box_coordinates(self) -> List[int]:
        return self._xp_box_coordinates

    @xp_box_coordinates.setter
    def xp_box_coordinates(self, _):
        raise AttributeError("Read-only attribute")

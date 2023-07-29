import time
import logging

from screenshotwatcher import ScreenshotWatcher
from ocrextract import XPExtractor
from dungeonmanager import DungeonManager
from configreader import ConfigReader

LOGGING_FORMAT = "%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)

logging.info("Diablo IV Nightmare Dungeon Experience Tracker")

config = ConfigReader("config.ini")
watcher = ScreenshotWatcher(config)
extractor = XPExtractor(config)
dungeon_manager = DungeonManager(config, extractor)

watcher.register_on_modified_callback(dungeon_manager.dungeon_event_callback)
watcher.start_watcher()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcher.stop_watcher()
    logging.info("Run summary:")
    dungeon_manager.dump_dungeons()

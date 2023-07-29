import pytest
import csv

from unittest.mock import MagicMock, Mock
import os

from dungeonmanager import DungeonManager
from ocrextract import XPExtractor
from configreader import ConfigReader


@pytest.fixture(autouse=True)
def prepare_config():
    pytest._d4config = ConfigReader("tests/resources/test_config.ini")
    pytest._d4extractor = XPExtractor(pytest._d4config)
    if os.path.exists(pytest._d4config.output_csv):
        os.remove(pytest._d4config.output_csv)
    yield
    if os.path.exists(pytest._d4config.output_csv):
        os.remove(pytest._d4config.output_csv)
    pytest._d4config = None
    pytest._d4extractor = None


def test_dungeonmanager_init():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)


def test_dungeonmanager_start_dungeon():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d._start_new_dungeon = MagicMock()
    d.dungeon_event_callback("tests/resources/screenshot.jpg")
    assert d._start_new_dungeon.called


def test_dungeonmanager_end_dungeon():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d.dungeon_event_callback("tests/resources/screenshot.jpg")
    assert d._current_dungeon is not None
    d._end_current_dungeon = MagicMock()
    d.dungeon_event_callback("tests/resources/screenshot_end.jpg")
    assert d._end_current_dungeon.called


def test_dungeonmanager_level_up():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d.dungeon_event_callback("tests/resources/screenshot_level_up_1.jpg")
    assert d._current_dungeon is not None
    d.dungeon_event_callback("tests/resources/screenshot_level_up_2.jpg")
    assert d._current_dungeon is None


def test_dungeonmanager_detect_already_passed_screenshots():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d.dungeon_event_callback("tests/resources/screenshot.jpg")
    d._start_new_dungeon = MagicMock()
    d._end_current_dungeon = MagicMock()
    d.dungeon_event_callback("tests/resources/screenshot.jpg")
    assert not d._end_current_dungeon.called
    assert not d._start_new_dungeon.called


def test_dungeonmanager_missing_xp():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d._start_new_dungeon = MagicMock()
    d._end_current_dungeon = MagicMock()
    d.dungeon_event_callback("tests/resources/screenshot_no_xp.jpg")
    assert not d._end_current_dungeon.called
    assert not d._start_new_dungeon.called


def test_dungeonmanager_dump_dungeons():
    d = DungeonManager(pytest._d4config, pytest._d4extractor)
    d.dungeon_event_callback("tests/resources/screenshot.jpg")
    d.dungeon_event_callback("tests/resources/screenshot_end.jpg")
    d.dump_dungeons()
    with open("dungeons_test.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        l = list(reader)
        assert l[0][0] == "Sarat's Lair"
        assert l[0][1] == "96"
        assert l[0][2] == "4124533"
        assert l[0][4] == "96"

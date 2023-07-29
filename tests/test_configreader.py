import pytest

from configreader import ConfigReader


def test_init_correct_config():
    c = ConfigReader("tests/resources/test_config.ini")


def test_init_empty_config():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/test_empty_config.ini")


def test_init_empty_config_1():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/test_empty_config_1.ini")


def test_init_empty_config_2():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/test_empty_config_2.ini")


def test_init_config_not_found():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/not_found")


# DungeonNameCoordinates = 2097,442,2502,489
def test_config_parsing_dungeon_name():
    c = ConfigReader("tests/resources/test_config.ini")
    left, top, right, bottom = c.dungeon_name_coordinates
    assert left == 2097
    assert top == 442
    assert right == 2502
    assert bottom == 489


# XPBoxCoordinates = 1054,1164,1520,1230
def test_config_parsing_xp_box():
    c = ConfigReader("tests/resources/test_config.ini")
    left, top, right, bottom = c.xp_box_coordinates
    assert left == 1054
    assert top == 1164
    assert right == 1520
    assert bottom == 1230


def test_config_parsing_screenshot_path():
    c = ConfigReader("tests/resources/test_config.ini")
    assert c.screenshot_path == "C:/Users/rotte/Documents/Diablo IV/Screenshots"


def test_config_raises_set_screenshot_path():
    c = ConfigReader("tests/resources/test_config.ini")
    with pytest.raises(AttributeError):
        c.screenshot_path = "RaisePlx"


def test_config_raises_set_tesseract_exe():
    c = ConfigReader("tests/resources/test_config.ini")
    with pytest.raises(AttributeError):
        c.tesseract_exe = "RaisePlx"


def test_config_raises_set_output_csv():
    c = ConfigReader("tests/resources/test_config.ini")
    with pytest.raises(AttributeError):
        c.output_csv = "RaisePlx"


def test_config_raises_set_dungeon_name_coordinates():
    c = ConfigReader("tests/resources/test_config.ini")
    with pytest.raises(AttributeError):
        c.dungeon_name_coordinates = "RaisePlx"


def test_config_raises_set_xp_box_coordinates():
    c = ConfigReader("tests/resources/test_config.ini")
    with pytest.raises(AttributeError):
        c.xp_box_coordinates = "RaisePlx"


def test_config_raises_not_enough_coordinates_1():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/test_wrong_coordinates_1.ini")


def test_config_raises_not_enough_coordinates_2():
    with pytest.raises(SystemExit):
        c = ConfigReader("tests/resources/test_wrong_coordinates_2.ini")

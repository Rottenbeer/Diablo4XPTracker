import pytest

from ocrextract import XPExtractor
from configreader import ConfigReader


@pytest.fixture(autouse=True)
def prepare_config():
    pytest._d4config = ConfigReader("tests/resources/test_config.ini")
    yield
    pytest._d4config = None
    pytest._d4extractor = None


def test_ocr_extract_parsename():
    e = XPExtractor(pytest._d4config)
    assert e.extract_name("tests/resources/screenshot.jpg") == "Sarat's Lair"


def test_ocr_extract_parsename_unknown_dungeon():
    e = XPExtractor(pytest._d4config)
    assert (
        e.extract_name("tests/resources/screenshot_small_xp_box.jpg")
        == "Unknown Dungeon"
    )


def test_ocr_extract_level():
    e = XPExtractor(pytest._d4config)
    x = e.extract_xp("tests/resources/screenshot.jpg")
    assert x.level == 96


def test_ocr_extract_parse_xp():
    e = XPExtractor(pytest._d4config)
    x = e.extract_xp("tests/resources/screenshot.jpg")
    assert x.xp_current == 4124533


def test_ocr_extract_parse_xp_small_box():
    e = XPExtractor(pytest._d4config)
    x = e.extract_xp("tests/resources/screenshot_small_xp_box.jpg")
    assert x.xp_current == 11343


def test_ocr_extract_parse_xp_max():
    e = XPExtractor(pytest._d4config)
    x = e.extract_xp("tests/resources/screenshot.jpg")
    assert x.xp_max == 20234250

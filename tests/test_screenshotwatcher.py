import pytest
import os
import shutil
import time

from unittest.mock import MagicMock

from screenshotwatcher import ScreenshotWatcher
from configreader import ConfigReader


@pytest.fixture(autouse=True)
def prepare_config():
    pytest._d4config = ConfigReader("tests/resources/test_config.ini")
    tmpdir = "tests/resources/tmp"
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
    os.mkdir(tmpdir)

    yield

    pytest._d4config = None
    pytest._d4extractor = None
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)


def test_watcher_init():
    s = ScreenshotWatcher(pytest._d4config)


def test_watcher_start_watching():
    s = ScreenshotWatcher(pytest._d4config)
    s.start_watcher()


def test_watcher_stop_watching():
    s = ScreenshotWatcher(pytest._d4config)
    s.start_watcher()
    s.stop_watcher()


def test_watcher_register_callbacks():
    s = ScreenshotWatcher(pytest._d4config)
    m1 = MagicMock()
    m2 = MagicMock()
    m3 = MagicMock()
    m4 = MagicMock()
    s.register_on_created_callback(m1)
    s.register_on_modified_callback(m2)
    s.register_on_moved_callback(m3)
    s.register_on_deleted_callback(m4)
    s.start_watcher()
    with open("tests/resources/tmp/bla.jpg", "w") as f:
        f.write("Yoo test!")
        f.close()
    time.sleep(1)
    assert m1.called
    assert m2.called
    os.rename("tests/resources/tmp/bla.jpg", "tests/resources/tmp/bla2.jpg")
    time.sleep(1)
    assert m3.called
    os.remove("tests/resources/tmp/bla2.jpg")
    time.sleep(1)
    assert m4.called


def test_watcher_register_one_callback():
    s = ScreenshotWatcher(pytest._d4config)
    m1 = MagicMock()
    m2 = MagicMock()
    s.register_on_modified_callback(m2)
    s.start_watcher()
    with open("tests/resources/tmp/bla.jpg", "w") as f:
        f.write("Yoo test!")
        f.close()
    time.sleep(1)
    assert not m1.called
    assert m2.called


def test_watcher_no_callbacks_registered():
    try:
        s = ScreenshotWatcher(pytest._d4config)
        s.start_watcher()
        with open("tests/resources/tmp/bla.jpg", "w") as f:
            f.write("Yoo test!")
            f.close()
        time.sleep(1)
        os.rename("tests/resources/tmp/bla.jpg", "tests/resources/tmp/bla2.jpg")
        time.sleep(1)
        os.remove("tests/resources/tmp/bla2.jpg")
        time.sleep(1)
        s.stop_watcher()
    except Exception:
        pytest.fail("Unexpected Exception")

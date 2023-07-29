import pytest
import datetime
from unittest.mock import MagicMock

from levelinfo import LevelInfo

FAKE_NOW = datetime.datetime(2023, 7, 30, 17, 0, 0)


@pytest.fixture()
def mock_datetime_now(monkeypatch):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = FAKE_NOW
    monkeypatch.setattr(datetime, "datetime", datetime_mock)


def test_levelinfo():
    l = LevelInfo(95, 100, 200)


def test_levelinfo_str(mock_datetime_now):
    l = LevelInfo(95, 100, 200)
    assert str(l) == "Level: 95, 100 / 200, captured at 2023-07-30 17:00:00"

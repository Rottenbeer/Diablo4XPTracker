import re
import logging

from typing import Optional

import pytesseract  # type: ignore

from PIL import Image

from .levelinfo import LevelInfo
from .configreader import ConfigReader


class XPExtractor:
    def __init__(self, config: ConfigReader) -> None:
        # If you don't have tesseract executable in your PATH, include the following:
        self._config = config
        pytesseract.pytesseract.tesseract_cmd = self._config.tesseract_exe
        self.xpregex = re.compile(r".*Level (\d+) Experience: (\d+)\s*\/\s*(\d+).*")

    def _parsexp(self, raw_string: str) -> Optional[LevelInfo]:
        raw_string = raw_string.strip()
        raw_string = raw_string.replace("\n", "")
        raw_string = raw_string.replace(",", "")

        logging.debug(f"Trying to parse extracted string {raw_string}")
        result = re.match(self.xpregex, raw_string)
        if result:
            levelinfo = LevelInfo(int(result[1]), int(result[2]), int(result[3]))
        else:
            logging.debug(f"Regex did not match extracted string: {raw_string}")
            return None

        return levelinfo

    def _parse_name(self, raw_string: str) -> str:
        raw_string = raw_string.replace("\n", "")
        raw_string = raw_string.lstrip()
        raw_string = raw_string.rstrip()
        return raw_string

    def extract_xp(self, image_path: str) -> Optional[LevelInfo]:
        image = Image.open(image_path)

        # Setting the points for cropped image
        left, top, right, bottom = self._config.xp_box_coordinates
        im1 = image.crop((left, top, right, bottom))

        raw_string = pytesseract.image_to_string(im1)
        logging.debug(f"Extracted {raw_string}")
        return self._parsexp(raw_string)

    def extract_name(self, image_path: str) -> str:
        image = Image.open(image_path)

        # Setting the points for cropped image
        left, top, right, bottom = self._config.dungeon_name_coordinates
        im1 = image.crop((left, top, right, bottom))

        raw_string = pytesseract.image_to_string(im1)
        logging.debug(f"Extracted {raw_string}")
        if raw_string != "":
            return self._parse_name(raw_string)
        else:
            return "Unknown Dungeon"

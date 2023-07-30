import re
import logging

import pytesseract

from PIL import Image

from .levelinfo import LevelInfo


class XPExtractor:
    def __init__(self, config):
        # If you don't have tesseract executable in your PATH, include the following:
        self._config = config
        pytesseract.pytesseract.tesseract_cmd = self._config.tesseract_exe
        self.xpregex = re.compile(r".*Level (\d+) Experience: (\d+)\s*\/\s*(\d+).*")

    def _parsexp(self, rawstring):
        rawstring = rawstring.strip()
        rawstring = rawstring.replace("\n", "")
        rawstring = rawstring.replace(",", "")

        logging.debug(f"Trying to parse extracted string {rawstring}")
        result = re.match(self.xpregex, rawstring)
        if result:
            levelinfo = LevelInfo(int(result[1]), int(result[2]), int(result[3]))
        else:
            logging.debug(f"Regex did not match extracted string: {rawstring}")
            return None

        return levelinfo

    def _parse_name(self, rawstring):
        rawstring = rawstring.replace("\n", "")
        rawstring = rawstring.lstrip()
        rawstring = rawstring.rstrip()
        return rawstring

    def extract_xp(self, imagepath):
        image = Image.open(imagepath)

        # Setting the points for cropped image
        left, top, right, bottom = self._config.xp_box_coordinates
        im1 = image.crop((left, top, right, bottom))

        rawstring = pytesseract.image_to_string(im1)
        logging.debug(f"Extracted {rawstring}")
        return self._parsexp(rawstring)

    def extract_name(self, image_path):
        image = Image.open(image_path)

        # Setting the points for cropped image
        left, top, right, bottom = self._config.dungeon_name_coordinates
        im1 = image.crop((left, top, right, bottom))

        rawstring = pytesseract.image_to_string(im1)
        logging.debug(f"Extracted {rawstring}")
        if rawstring != "":
            return self._parse_name(rawstring)
        else:
            return "Unknown Dungeon"

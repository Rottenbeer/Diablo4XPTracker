# type: ignore
from setuptools import setup

setup(
    name="Diablo4XPTracker",
    version="1.0.0",
    packages=["xp_tracker"],
    url="https://github.com/Rottenbeer/Diablo4XPTracker",
    author="Florian Meier",
    author_email="flmeier90@gmail.com",
    description="A Diablo4 Nightmare Dungeon XP Tracker",
    install_requires=[
        "pytest",
        "pytesseract",
        "watchdog",
        "coverage",
    ],
    entry_points={
        "console_scripts": [
            "d4xptracker=xp_tracker.xp_tracker:main",
        ],
    },
)

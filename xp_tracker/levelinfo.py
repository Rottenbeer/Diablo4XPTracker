import datetime


class LevelInfo:
    def __init__(self, level: int, xpstart: int, xpend: int) -> None:
        self.level = level
        self.xp_current = xpstart
        self.xp_max = xpend
        self.time_captured = datetime.datetime.now()

    def __str__(self) -> str:
        return f"Level: {self.level}, {self.xp_current} / {self.xp_max}, captured at {self.time_captured}"

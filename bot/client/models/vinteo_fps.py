from enum import IntEnum


class VinteoFPS(IntEnum):
    VALUE_15 = 15
    VALUE_25 = 25
    VALUE_30 = 30
    VALUE_45 = 45
    VALUE_60 = 60

    def __str__(self) -> str:
        return str(self.value)

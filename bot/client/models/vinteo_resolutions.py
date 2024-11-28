from enum import Enum


class VinteoResolutions(str, Enum):
    CIF = "CIF"
    FULLHD = "FULLHD"
    VALUE_1 = "4CIF"
    VALUE_2 = "640x360"
    VALUE_3 = "720p"

    def __str__(self) -> str:
        return str(self.value)

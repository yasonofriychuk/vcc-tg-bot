from enum import Enum


class ReportType(str, Enum):
    DATES = "dates"
    DEPARTMENTS = "departments"
    GENERAL = "general"

    def __str__(self) -> str:
        return str(self.value)

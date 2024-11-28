import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReportByDate")


@_attrs_define
class ReportByDate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        booked (int):
        cancelled (int):
        ended (int):
        started (int):
        total (int):
        date (datetime.date):
    """

    booked: int
    cancelled: int
    ended: int
    started: int
    total: int
    date: datetime.date
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        booked = self.booked

        cancelled = self.cancelled

        ended = self.ended

        started = self.started

        total = self.total

        date = self.date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "booked": booked,
                "cancelled": cancelled,
                "ended": ended,
                "started": started,
                "total": total,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        booked = d.pop("booked")

        cancelled = d.pop("cancelled")

        ended = d.pop("ended")

        started = d.pop("started")

        total = d.pop("total")

        date = isoparse(d.pop("date")).date()

        report_by_date = cls(
            booked=booked,
            cancelled=cancelled,
            ended=ended,
            started=started,
            total=total,
            date=date,
        )

        report_by_date.additional_properties = d
        return report_by_date

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
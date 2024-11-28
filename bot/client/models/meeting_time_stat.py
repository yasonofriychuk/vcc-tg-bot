from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeetingTimeStat")


@_attrs_define
class MeetingTimeStat:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        average (float):
        min_ (float):
        max_ (float):
        sum_ (float):
    """

    average: float
    min_: float
    max_: float
    sum_: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average = self.average

        min_ = self.min_

        max_ = self.max_

        sum_ = self.sum_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "average": average,
                "min": min_,
                "max": max_,
                "sum": sum_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average = d.pop("average")

        min_ = d.pop("min")

        max_ = d.pop("max")

        sum_ = d.pop("sum")

        meeting_time_stat = cls(
            average=average,
            min_=min_,
            max_=max_,
            sum_=sum_,
        )

        meeting_time_stat.additional_properties = d
        return meeting_time_stat

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

from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeetingLicenseThreshold")


@_attrs_define
class MeetingLicenseThreshold:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        time_start (str):
        time_end (str):
        value (int):
    """

    time_start: str
    time_end: str
    value: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_start = self.time_start

        time_end = self.time_end

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeStart": time_start,
                "timeEnd": time_end,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_start = d.pop("timeStart")

        time_end = d.pop("timeEnd")

        value = d.pop("value")

        meeting_license_threshold = cls(
            time_start=time_start,
            time_end=time_end,
            value=value,
        )

        meeting_license_threshold.additional_properties = d
        return meeting_license_threshold

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

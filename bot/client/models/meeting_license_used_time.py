from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingLicenseUsedTime")


@_attrs_define
class MeetingLicenseUsedTime:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        time_start (str):
        time_end (str):
        private_licenses_used_count_relative (Union[Unset, float]):
        public_licenses_used_count_relative (Union[Unset, float]):
    """

    time_start: str
    time_end: str
    private_licenses_used_count_relative: Union[Unset, float] = UNSET
    public_licenses_used_count_relative: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_start = self.time_start

        time_end = self.time_end

        private_licenses_used_count_relative = self.private_licenses_used_count_relative

        public_licenses_used_count_relative = self.public_licenses_used_count_relative

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeStart": time_start,
                "timeEnd": time_end,
            }
        )
        if private_licenses_used_count_relative is not UNSET:
            field_dict["privateLicensesUsedCountRelative"] = private_licenses_used_count_relative
        if public_licenses_used_count_relative is not UNSET:
            field_dict["publicLicensesUsedCountRelative"] = public_licenses_used_count_relative

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_start = d.pop("timeStart")

        time_end = d.pop("timeEnd")

        private_licenses_used_count_relative = d.pop("privateLicensesUsedCountRelative", UNSET)

        public_licenses_used_count_relative = d.pop("publicLicensesUsedCountRelative", UNSET)

        meeting_license_used_time = cls(
            time_start=time_start,
            time_end=time_end,
            private_licenses_used_count_relative=private_licenses_used_count_relative,
            public_licenses_used_count_relative=public_licenses_used_count_relative,
        )

        meeting_license_used_time.additional_properties = d
        return meeting_license_used_time

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

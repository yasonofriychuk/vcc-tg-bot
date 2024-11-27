import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_license_threshold import MeetingLicenseThreshold


T = TypeVar("T", bound="MeetingLicense")


@_attrs_define
class MeetingLicense:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        date (datetime.date):
        private_licenses_used_count_relative (Union[Unset, float]):
        public_licenses_used_count_relative (Union[Unset, float]):
        max_license (Union[Unset, MeetingLicenseThreshold]): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования
        min_license (Union[Unset, MeetingLicenseThreshold]): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования
    """

    date: datetime.date
    private_licenses_used_count_relative: Union[Unset, float] = UNSET
    public_licenses_used_count_relative: Union[Unset, float] = UNSET
    max_license: Union[Unset, "MeetingLicenseThreshold"] = UNSET
    min_license: Union[Unset, "MeetingLicenseThreshold"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        private_licenses_used_count_relative = self.private_licenses_used_count_relative

        public_licenses_used_count_relative = self.public_licenses_used_count_relative

        max_license: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_license, Unset):
            max_license = self.max_license.to_dict()

        min_license: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.min_license, Unset):
            min_license = self.min_license.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
            }
        )
        if private_licenses_used_count_relative is not UNSET:
            field_dict["privateLicensesUsedCountRelative"] = private_licenses_used_count_relative
        if public_licenses_used_count_relative is not UNSET:
            field_dict["publicLicensesUsedCountRelative"] = public_licenses_used_count_relative
        if max_license is not UNSET:
            field_dict["maxLicense"] = max_license
        if min_license is not UNSET:
            field_dict["minLicense"] = min_license

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meeting_license_threshold import MeetingLicenseThreshold

        d = src_dict.copy()
        date = isoparse(d.pop("date")).date()

        private_licenses_used_count_relative = d.pop("privateLicensesUsedCountRelative", UNSET)

        public_licenses_used_count_relative = d.pop("publicLicensesUsedCountRelative", UNSET)

        _max_license = d.pop("maxLicense", UNSET)
        max_license: Union[Unset, MeetingLicenseThreshold]
        if isinstance(_max_license, Unset):
            max_license = UNSET
        else:
            max_license = MeetingLicenseThreshold.from_dict(_max_license)

        _min_license = d.pop("minLicense", UNSET)
        min_license: Union[Unset, MeetingLicenseThreshold]
        if isinstance(_min_license, Unset):
            min_license = UNSET
        else:
            min_license = MeetingLicenseThreshold.from_dict(_min_license)

        meeting_license = cls(
            date=date,
            private_licenses_used_count_relative=private_licenses_used_count_relative,
            public_licenses_used_count_relative=public_licenses_used_count_relative,
            max_license=max_license,
            min_license=min_license,
        )

        meeting_license.additional_properties = d
        return meeting_license

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

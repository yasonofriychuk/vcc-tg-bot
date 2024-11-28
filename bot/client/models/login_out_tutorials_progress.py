import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LoginOutTutorialsProgress")


@_attrs_define
class LoginOutTutorialsProgress:
    """ """

    additional_properties: Dict[str, datetime.datetime] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.isoformat()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_out_tutorials_progress = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = isoparse(prop_dict)

            additional_properties[prop_name] = additional_property

        login_out_tutorials_progress.additional_properties = additional_properties
        return login_out_tutorials_progress

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> datetime.datetime:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: datetime.datetime) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
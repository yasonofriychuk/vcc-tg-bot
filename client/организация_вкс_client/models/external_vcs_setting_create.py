from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalVCSSettingCreate")


@_attrs_define
class ExternalVCSSettingCreate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        external_url (str):
        permanent_room_id (Union[Unset, int]):
    """

    external_url: str
    permanent_room_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_url = self.external_url

        permanent_room_id = self.permanent_room_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalUrl": external_url,
            }
        )
        if permanent_room_id is not UNSET:
            field_dict["permanentRoomId"] = permanent_room_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_url = d.pop("externalUrl")

        permanent_room_id = d.pop("permanentRoomId", UNSET)

        external_vcs_setting_create = cls(
            external_url=external_url,
            permanent_room_id=permanent_room_id,
        )

        external_vcs_setting_create.additional_properties = d
        return external_vcs_setting_create

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

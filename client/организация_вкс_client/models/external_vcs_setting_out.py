from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permanent_room_out import PermanentRoomOut


T = TypeVar("T", bound="ExternalVCSSettingOut")


@_attrs_define
class ExternalVCSSettingOut:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        external_url (str):
        id (int):
        permanent_room_id (Union[Unset, int]):
        permanent_room (Union[Unset, PermanentRoomOut]): Базовая модель для выдачи любого каталога
    """

    external_url: str
    id: int
    permanent_room_id: Union[Unset, int] = UNSET
    permanent_room: Union[Unset, "PermanentRoomOut"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_url = self.external_url

        id = self.id

        permanent_room_id = self.permanent_room_id

        permanent_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permanent_room, Unset):
            permanent_room = self.permanent_room.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalUrl": external_url,
                "id": id,
            }
        )
        if permanent_room_id is not UNSET:
            field_dict["permanentRoomId"] = permanent_room_id
        if permanent_room is not UNSET:
            field_dict["permanentRoom"] = permanent_room

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.permanent_room_out import PermanentRoomOut

        d = src_dict.copy()
        external_url = d.pop("externalUrl")

        id = d.pop("id")

        permanent_room_id = d.pop("permanentRoomId", UNSET)

        _permanent_room = d.pop("permanentRoom", UNSET)
        permanent_room: Union[Unset, PermanentRoomOut]
        if isinstance(_permanent_room, Unset):
            permanent_room = UNSET
        else:
            permanent_room = PermanentRoomOut.from_dict(_permanent_room)

        external_vcs_setting_out = cls(
            external_url=external_url,
            id=id,
            permanent_room_id=permanent_room_id,
            permanent_room=permanent_room,
        )

        external_vcs_setting_out.additional_properties = d
        return external_vcs_setting_out

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

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoomShort")


@_attrs_define
class RoomShort:
    """Базовая модель для выдачи любого каталога

    Attributes:
        name (str):
        description (str):
        id (int):
        building_id (int):  Example: 1.
        max_participants (int):  Example: 2.
        is_skit_notified (Union[Unset, bool]): Если выставлен данный флаг, при создании ВКС в данной комнате, в СКИТ
            будет отправлено письмо Default: False.
    """

    name: str
    description: str
    id: int
    building_id: int
    max_participants: int
    is_skit_notified: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        id = self.id

        building_id = self.building_id

        max_participants = self.max_participants

        is_skit_notified = self.is_skit_notified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "id": id,
                "buildingId": building_id,
                "maxParticipants": max_participants,
            }
        )
        if is_skit_notified is not UNSET:
            field_dict["isSkitNotified"] = is_skit_notified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        id = d.pop("id")

        building_id = d.pop("buildingId")

        max_participants = d.pop("maxParticipants")

        is_skit_notified = d.pop("isSkitNotified", UNSET)

        room_short = cls(
            name=name,
            description=description,
            id=id,
            building_id=building_id,
            max_participants=max_participants,
            is_skit_notified=is_skit_notified,
        )

        room_short.additional_properties = d
        return room_short

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

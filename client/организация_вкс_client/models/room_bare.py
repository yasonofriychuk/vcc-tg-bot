from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_brief import UserBrief


T = TypeVar("T", bound="RoomBare")


@_attrs_define
class RoomBare:
    """Базовая модель для выдачи любого каталога

    Attributes:
        name (str):
        description (str):
        id (int):
        building_id (int):  Example: 1.
        max_participants (int):  Example: 2.
        is_skit_notified (Union[Unset, bool]): Если выставлен данный флаг, при создании ВКС в данной комнате, в СКИТ
            будет отправлено письмо Default: False.
        responsible_user (Union[Unset, UserBrief]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
    """

    name: str
    description: str
    id: int
    building_id: int
    max_participants: int
    is_skit_notified: Union[Unset, bool] = False
    responsible_user: Union[Unset, "UserBrief"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        id = self.id

        building_id = self.building_id

        max_participants = self.max_participants

        is_skit_notified = self.is_skit_notified

        responsible_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.responsible_user, Unset):
            responsible_user = self.responsible_user.to_dict()

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
        if responsible_user is not UNSET:
            field_dict["responsibleUser"] = responsible_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_brief import UserBrief

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        id = d.pop("id")

        building_id = d.pop("buildingId")

        max_participants = d.pop("maxParticipants")

        is_skit_notified = d.pop("isSkitNotified", UNSET)

        _responsible_user = d.pop("responsibleUser", UNSET)
        responsible_user: Union[Unset, UserBrief]
        if isinstance(_responsible_user, Unset):
            responsible_user = UNSET
        else:
            responsible_user = UserBrief.from_dict(_responsible_user)

        room_bare = cls(
            name=name,
            description=description,
            id=id,
            building_id=building_id,
            max_participants=max_participants,
            is_skit_notified=is_skit_notified,
            responsible_user=responsible_user,
        )

        room_bare.additional_properties = d
        return room_bare

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

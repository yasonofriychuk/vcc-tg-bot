from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meeting_backend import MeetingBackend
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermanentRoomIn")


@_attrs_define
class PermanentRoomIn:
    """Базовая модель для любого каталога

    Attributes:
        name (str):
        link (str):
        description (Union[Unset, str]): Описание постоянной комнаты, которое будет рассылаться в письме-приглашении
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default: MeetingBackend.CISCO.
    """

    name: str
    link: str
    description: Union[Unset, str] = UNSET
    backend: Union[Unset, MeetingBackend] = MeetingBackend.CISCO
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        link = self.link

        description = self.description

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "link": link,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if backend is not UNSET:
            field_dict["backend"] = backend

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        link = d.pop("link")

        description = d.pop("description", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, MeetingBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = MeetingBackend(_backend)

        permanent_room_in = cls(
            name=name,
            link=link,
            description=description,
            backend=backend,
        )

        permanent_room_in.additional_properties = d
        return permanent_room_in

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

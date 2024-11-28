import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_backend import MeetingBackend
from ..models.meeting_states import MeetingStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cisco_room_public_bare import CiscoRoomPublicBare
    from ..models.external_vcs_setting_out import ExternalVCSSettingOut
    from ..models.room_full import RoomFull
    from ..models.user_brief import UserBrief
    from ..models.vinteo_room_public_bare import VinteoRoomPublicBare


T = TypeVar("T", bound="MeetingPermalinkOut")


@_attrs_define
class MeetingPermalinkOut:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        name (str):
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.827487.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.827513.
        state (MeetingStates): Перечень состояний, в которых может находиться сущность ВКС
        organizer (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования
        room_id (Union[Unset, int]):
        room (Union[Unset, RoomFull]): Базовая модель для выдачи любого каталога
        cisco_room (Union[Unset, CiscoRoomPublicBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
        vinteo_room (Union[Unset, VinteoRoomPublicBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
        external_settings (Union[Unset, ExternalVCSSettingOut]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        participants_count (Union[Unset, int]):
        duration (Union[Unset, int]):  Example: 120.
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default: MeetingBackend.CISCO.
        link (Union[Unset, str]): Ссылка на реальный ВКС (при наличии, т.е. после создания реальной комнаты)
        enable_conference_before (Union[Unset, int]): Количество часов до начала конференции, за которое комната будет
            доступна
    """

    id: int
    name: str
    started_at: datetime.datetime
    ended_at: datetime.datetime
    state: MeetingStates
    organizer: "UserBrief"
    room_id: Union[Unset, int] = UNSET
    room: Union[Unset, "RoomFull"] = UNSET
    cisco_room: Union[Unset, "CiscoRoomPublicBare"] = UNSET
    vinteo_room: Union[Unset, "VinteoRoomPublicBare"] = UNSET
    external_settings: Union[Unset, "ExternalVCSSettingOut"] = UNSET
    participants_count: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    backend: Union[Unset, MeetingBackend] = MeetingBackend.CISCO
    link: Union[Unset, str] = UNSET
    enable_conference_before: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        state = self.state.value

        organizer = self.organizer.to_dict()

        room_id = self.room_id

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        cisco_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cisco_room, Unset):
            cisco_room = self.cisco_room.to_dict()

        vinteo_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vinteo_room, Unset):
            vinteo_room = self.vinteo_room.to_dict()

        external_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_settings, Unset):
            external_settings = self.external_settings.to_dict()

        participants_count = self.participants_count

        duration = self.duration

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        link = self.link

        enable_conference_before = self.enable_conference_before

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "startedAt": started_at,
                "endedAt": ended_at,
                "state": state,
                "organizer": organizer,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room is not UNSET:
            field_dict["room"] = room
        if cisco_room is not UNSET:
            field_dict["ciscoRoom"] = cisco_room
        if vinteo_room is not UNSET:
            field_dict["vinteoRoom"] = vinteo_room
        if external_settings is not UNSET:
            field_dict["externalSettings"] = external_settings
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if backend is not UNSET:
            field_dict["backend"] = backend
        if link is not UNSET:
            field_dict["link"] = link
        if enable_conference_before is not UNSET:
            field_dict["enableConferenceBefore"] = enable_conference_before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cisco_room_public_bare import CiscoRoomPublicBare
        from ..models.external_vcs_setting_out import ExternalVCSSettingOut
        from ..models.room_full import RoomFull
        from ..models.user_brief import UserBrief
        from ..models.vinteo_room_public_bare import VinteoRoomPublicBare

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        state = MeetingStates(d.pop("state"))

        organizer = UserBrief.from_dict(d.pop("organizer"))

        room_id = d.pop("roomId", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomFull]
        if isinstance(_room, Unset):
            room = UNSET
        else:
            room = RoomFull.from_dict(_room)

        _cisco_room = d.pop("ciscoRoom", UNSET)
        cisco_room: Union[Unset, CiscoRoomPublicBare]
        if isinstance(_cisco_room, Unset):
            cisco_room = UNSET
        else:
            cisco_room = CiscoRoomPublicBare.from_dict(_cisco_room)

        _vinteo_room = d.pop("vinteoRoom", UNSET)
        vinteo_room: Union[Unset, VinteoRoomPublicBare]
        if isinstance(_vinteo_room, Unset):
            vinteo_room = UNSET
        else:
            vinteo_room = VinteoRoomPublicBare.from_dict(_vinteo_room)

        _external_settings = d.pop("externalSettings", UNSET)
        external_settings: Union[Unset, ExternalVCSSettingOut]
        if isinstance(_external_settings, Unset):
            external_settings = UNSET
        else:
            external_settings = ExternalVCSSettingOut.from_dict(_external_settings)

        participants_count = d.pop("participantsCount", UNSET)

        duration = d.pop("duration", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, MeetingBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = MeetingBackend(_backend)

        link = d.pop("link", UNSET)

        enable_conference_before = d.pop("enableConferenceBefore", UNSET)

        meeting_permalink_out = cls(
            id=id,
            name=name,
            started_at=started_at,
            ended_at=ended_at,
            state=state,
            organizer=organizer,
            room_id=room_id,
            room=room,
            cisco_room=cisco_room,
            vinteo_room=vinteo_room,
            external_settings=external_settings,
            participants_count=participants_count,
            duration=duration,
            backend=backend,
            link=link,
            enable_conference_before=enable_conference_before,
        )

        meeting_permalink_out.additional_properties = d
        return meeting_permalink_out

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

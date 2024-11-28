import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_backend import MeetingBackend
from ..models.meeting_states import MeetingStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cisco_room_bare import CiscoRoomBare
    from ..models.external_vcs_setting_out import ExternalVCSSettingOut
    from ..models.participant_out import ParticipantOut
    from ..models.room_full import RoomFull
    from ..models.user_brief import UserBrief
    from ..models.vinteo_room_bare import VinteoRoomBare


T = TypeVar("T", bound="MeetingPermalinkOrganizerFull")


@_attrs_define
class MeetingPermalinkOrganizerFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        name (str):
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.839636.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.839659.
        state (MeetingStates): Перечень состояний, в которых может находиться сущность ВКС
        participants (List['ParticipantOut']):
        event_id (int):
        organizer (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования
        room_id (Union[Unset, int]):
        room (Union[Unset, RoomFull]): Базовая модель для выдачи любого каталога
        participants_count (Union[Unset, int]):
        duration (Union[Unset, int]):  Example: 120.
        cisco_room (Union[Unset, CiscoRoomBare]): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        vinteo_room (Union[Unset, VinteoRoomBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
        external_settings (Union[Unset, ExternalVCSSettingOut]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        cisco_settings_id (Union[Unset, int]):
        vinteo_settings_id (Union[Unset, int]):
        cisco_room_id (Union[Unset, int]):
        vinteo_room_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default: MeetingBackend.CISCO.
        link (Union[Unset, str]): Ссылка на реальный ВКС (при наличии, т.е. после создания реальной комнаты)
        organizer_link (Union[Unset, str]): Ссылка на реальный ВКС (при наличии, т.е. после создания реальной комнаты),
            для подключения организатора. По сути – основная ссылка для странички организатора, по котоорй он и должен
            переходить
        enable_conference_before (Union[Unset, int]): Количество часов до начала конференции, за которое комната будет
            доступна
    """

    id: int
    name: str
    started_at: datetime.datetime
    ended_at: datetime.datetime
    state: MeetingStates
    participants: List["ParticipantOut"]
    event_id: int
    organizer: "UserBrief"
    room_id: Union[Unset, int] = UNSET
    room: Union[Unset, "RoomFull"] = UNSET
    participants_count: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    cisco_room: Union[Unset, "CiscoRoomBare"] = UNSET
    vinteo_room: Union[Unset, "VinteoRoomBare"] = UNSET
    external_settings: Union[Unset, "ExternalVCSSettingOut"] = UNSET
    cisco_settings_id: Union[Unset, int] = UNSET
    vinteo_settings_id: Union[Unset, int] = UNSET
    cisco_room_id: Union[Unset, int] = UNSET
    vinteo_room_id: Union[Unset, int] = UNSET
    backend: Union[Unset, MeetingBackend] = MeetingBackend.CISCO
    link: Union[Unset, str] = UNSET
    organizer_link: Union[Unset, str] = UNSET
    enable_conference_before: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        state = self.state.value

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        event_id = self.event_id

        organizer = self.organizer.to_dict()

        room_id = self.room_id

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        participants_count = self.participants_count

        duration = self.duration

        cisco_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cisco_room, Unset):
            cisco_room = self.cisco_room.to_dict()

        vinteo_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vinteo_room, Unset):
            vinteo_room = self.vinteo_room.to_dict()

        external_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_settings, Unset):
            external_settings = self.external_settings.to_dict()

        cisco_settings_id = self.cisco_settings_id

        vinteo_settings_id = self.vinteo_settings_id

        cisco_room_id = self.cisco_room_id

        vinteo_room_id = self.vinteo_room_id

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        link = self.link

        organizer_link = self.organizer_link

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
                "participants": participants,
                "eventId": event_id,
                "organizer": organizer,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room is not UNSET:
            field_dict["room"] = room
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if cisco_room is not UNSET:
            field_dict["ciscoRoom"] = cisco_room
        if vinteo_room is not UNSET:
            field_dict["vinteoRoom"] = vinteo_room
        if external_settings is not UNSET:
            field_dict["externalSettings"] = external_settings
        if cisco_settings_id is not UNSET:
            field_dict["ciscoSettingsId"] = cisco_settings_id
        if vinteo_settings_id is not UNSET:
            field_dict["vinteoSettingsId"] = vinteo_settings_id
        if cisco_room_id is not UNSET:
            field_dict["ciscoRoomId"] = cisco_room_id
        if vinteo_room_id is not UNSET:
            field_dict["vinteoRoomId"] = vinteo_room_id
        if backend is not UNSET:
            field_dict["backend"] = backend
        if link is not UNSET:
            field_dict["link"] = link
        if organizer_link is not UNSET:
            field_dict["organizerLink"] = organizer_link
        if enable_conference_before is not UNSET:
            field_dict["enableConferenceBefore"] = enable_conference_before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cisco_room_bare import CiscoRoomBare
        from ..models.external_vcs_setting_out import ExternalVCSSettingOut
        from ..models.participant_out import ParticipantOut
        from ..models.room_full import RoomFull
        from ..models.user_brief import UserBrief
        from ..models.vinteo_room_bare import VinteoRoomBare

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        state = MeetingStates(d.pop("state"))

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = ParticipantOut.from_dict(participants_item_data)

            participants.append(participants_item)

        event_id = d.pop("eventId")

        organizer = UserBrief.from_dict(d.pop("organizer"))

        room_id = d.pop("roomId", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomFull]
        if isinstance(_room, Unset):
            room = UNSET
        else:
            room = RoomFull.from_dict(_room)

        participants_count = d.pop("participantsCount", UNSET)

        duration = d.pop("duration", UNSET)

        _cisco_room = d.pop("ciscoRoom", UNSET)
        cisco_room: Union[Unset, CiscoRoomBare]
        if isinstance(_cisco_room, Unset):
            cisco_room = UNSET
        else:
            cisco_room = CiscoRoomBare.from_dict(_cisco_room)

        _vinteo_room = d.pop("vinteoRoom", UNSET)
        vinteo_room: Union[Unset, VinteoRoomBare]
        if isinstance(_vinteo_room, Unset):
            vinteo_room = UNSET
        else:
            vinteo_room = VinteoRoomBare.from_dict(_vinteo_room)

        _external_settings = d.pop("externalSettings", UNSET)
        external_settings: Union[Unset, ExternalVCSSettingOut]
        if isinstance(_external_settings, Unset):
            external_settings = UNSET
        else:
            external_settings = ExternalVCSSettingOut.from_dict(_external_settings)

        cisco_settings_id = d.pop("ciscoSettingsId", UNSET)

        vinteo_settings_id = d.pop("vinteoSettingsId", UNSET)

        cisco_room_id = d.pop("ciscoRoomId", UNSET)

        vinteo_room_id = d.pop("vinteoRoomId", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, MeetingBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = MeetingBackend(_backend)

        link = d.pop("link", UNSET)

        organizer_link = d.pop("organizerLink", UNSET)

        enable_conference_before = d.pop("enableConferenceBefore", UNSET)

        meeting_permalink_organizer_full = cls(
            id=id,
            name=name,
            started_at=started_at,
            ended_at=ended_at,
            state=state,
            participants=participants,
            event_id=event_id,
            organizer=organizer,
            room_id=room_id,
            room=room,
            participants_count=participants_count,
            duration=duration,
            cisco_room=cisco_room,
            vinteo_room=vinteo_room,
            external_settings=external_settings,
            cisco_settings_id=cisco_settings_id,
            vinteo_settings_id=vinteo_settings_id,
            cisco_room_id=cisco_room_id,
            vinteo_room_id=vinteo_room_id,
            backend=backend,
            link=link,
            organizer_link=organizer_link,
            enable_conference_before=enable_conference_before,
        )

        meeting_permalink_organizer_full.additional_properties = d
        return meeting_permalink_organizer_full

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

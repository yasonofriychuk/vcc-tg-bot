import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_backend import MeetingBackend
from ..models.meeting_states import MeetingStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cisco_room_bare import CiscoRoomBare
    from ..models.cisco_vcs_setting_bare import CiscoVCSSettingBare
    from ..models.event_bare import EventBare
    from ..models.external_vcs_setting_out import ExternalVCSSettingOut
    from ..models.file_bare import FileBare
    from ..models.group_bare import GroupBare
    from ..models.meeting_recurrence_brief import MeetingRecurrenceBrief
    from ..models.participant_out import ParticipantOut
    from ..models.room_bare import RoomBare
    from ..models.user_brief import UserBrief
    from ..models.vinteo_room_bare import VinteoRoomBare
    from ..models.vinteo_vcs_setting_bare import VinteoVCSSettingBare


T = TypeVar("T", bound="MeetingFull")


@_attrs_define
class MeetingFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):
        send_notifications_at (Union[datetime.datetime, int]):  Example: 2024-11-27T16:32:19.816061.
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.816087.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.816099.
        is_governor_presents (bool):
        created_at (datetime.datetime):
        state (MeetingStates): Перечень состояний, в которых может находиться сущность ВКС
        created_by (int):
        is_notify_accepted (bool):
        event (EventBare): Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования
        participants (List['ParticipantOut']):
        attachments (List['FileBare']):
        groups (List['GroupBare']):
        event_id (int):
        updated_at (datetime.datetime):
        created_user (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        permalink_id (Union[Unset, str]): идентификатор постоянной ссылка на ВКС. доступна сразу после создания и
            содержит базовую информацию для подключения к ВКС
        permalink (Union[Unset, str]): Ссылка на frontend страницу для перехода в вкс
        id (Union[Unset, int]):
        room_id (Union[Unset, int]):
        participants_count (Union[Unset, int]):
        duration (Union[Unset, int]):  Example: 120.
        closed_at (Union[Unset, datetime.datetime]):
        organized_by (Union[Unset, int]):
        is_virtual (Union[Unset, bool]): Является ли ВКС виртуально созданным объектом Default: False.
        organizer_permalink_id (Union[Unset, str]): идентификатор постоянной ссылка на ВКС для организатора. доступна
            сразу после создания и содержит данные для подключения к ВКС с полным доступом к управлению
        organizer_permalink (Union[Unset, str]): Ссылка на frontend страницу для перехода в вкс для организатора
        comment (Union[Unset, str]):
        room (Union[Unset, RoomBare]): Базовая модель для выдачи любого каталога
        cisco_room (Union[Unset, CiscoRoomBare]): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        cisco_settings (Union[Unset, CiscoVCSSettingBare]): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования
        vinteo_room (Union[Unset, VinteoRoomBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
        vinteo_settings (Union[Unset, VinteoVCSSettingBare]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        external_settings (Union[Unset, ExternalVCSSettingOut]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        cisco_settings_id (Union[Unset, int]):
        cisco_room_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default: MeetingBackend.CISCO.
        organized_user (Union[Unset, UserBrief]): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        recurrence (Union[Unset, MeetingRecurrenceBrief]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
    """

    name: str
    send_notifications_at: Union[datetime.datetime, int]
    started_at: datetime.datetime
    ended_at: datetime.datetime
    is_governor_presents: bool
    created_at: datetime.datetime
    state: MeetingStates
    created_by: int
    is_notify_accepted: bool
    event: "EventBare"
    participants: List["ParticipantOut"]
    attachments: List["FileBare"]
    groups: List["GroupBare"]
    event_id: int
    updated_at: datetime.datetime
    created_user: "UserBrief"
    permalink_id: Union[Unset, str] = UNSET
    permalink: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    room_id: Union[Unset, int] = UNSET
    participants_count: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    closed_at: Union[Unset, datetime.datetime] = UNSET
    organized_by: Union[Unset, int] = UNSET
    is_virtual: Union[Unset, bool] = False
    organizer_permalink_id: Union[Unset, str] = UNSET
    organizer_permalink: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    room: Union[Unset, "RoomBare"] = UNSET
    cisco_room: Union[Unset, "CiscoRoomBare"] = UNSET
    cisco_settings: Union[Unset, "CiscoVCSSettingBare"] = UNSET
    vinteo_room: Union[Unset, "VinteoRoomBare"] = UNSET
    vinteo_settings: Union[Unset, "VinteoVCSSettingBare"] = UNSET
    external_settings: Union[Unset, "ExternalVCSSettingOut"] = UNSET
    cisco_settings_id: Union[Unset, int] = UNSET
    cisco_room_id: Union[Unset, int] = UNSET
    backend: Union[Unset, MeetingBackend] = MeetingBackend.CISCO
    organized_user: Union[Unset, "UserBrief"] = UNSET
    recurrence: Union[Unset, "MeetingRecurrenceBrief"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        send_notifications_at: Union[int, str]
        if isinstance(self.send_notifications_at, datetime.datetime):
            send_notifications_at = self.send_notifications_at.isoformat()
        else:
            send_notifications_at = self.send_notifications_at

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        is_governor_presents = self.is_governor_presents

        created_at = self.created_at.isoformat()

        state = self.state.value

        created_by = self.created_by

        is_notify_accepted = self.is_notify_accepted

        event = self.event.to_dict()

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        event_id = self.event_id

        updated_at = self.updated_at.isoformat()

        created_user = self.created_user.to_dict()

        permalink_id = self.permalink_id

        permalink = self.permalink

        id = self.id

        room_id = self.room_id

        participants_count = self.participants_count

        duration = self.duration

        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        organized_by = self.organized_by

        is_virtual = self.is_virtual

        organizer_permalink_id = self.organizer_permalink_id

        organizer_permalink = self.organizer_permalink

        comment = self.comment

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        cisco_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cisco_room, Unset):
            cisco_room = self.cisco_room.to_dict()

        cisco_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cisco_settings, Unset):
            cisco_settings = self.cisco_settings.to_dict()

        vinteo_room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vinteo_room, Unset):
            vinteo_room = self.vinteo_room.to_dict()

        vinteo_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vinteo_settings, Unset):
            vinteo_settings = self.vinteo_settings.to_dict()

        external_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_settings, Unset):
            external_settings = self.external_settings.to_dict()

        cisco_settings_id = self.cisco_settings_id

        cisco_room_id = self.cisco_room_id

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        organized_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organized_user, Unset):
            organized_user = self.organized_user.to_dict()

        recurrence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sendNotificationsAt": send_notifications_at,
                "startedAt": started_at,
                "endedAt": ended_at,
                "isGovernorPresents": is_governor_presents,
                "createdAt": created_at,
                "state": state,
                "createdBy": created_by,
                "isNotifyAccepted": is_notify_accepted,
                "event": event,
                "participants": participants,
                "attachments": attachments,
                "groups": groups,
                "eventId": event_id,
                "updatedAt": updated_at,
                "createdUser": created_user,
            }
        )
        if permalink_id is not UNSET:
            field_dict["permalinkId"] = permalink_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if id is not UNSET:
            field_dict["id"] = id
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if organized_by is not UNSET:
            field_dict["organizedBy"] = organized_by
        if is_virtual is not UNSET:
            field_dict["isVirtual"] = is_virtual
        if organizer_permalink_id is not UNSET:
            field_dict["organizerPermalinkId"] = organizer_permalink_id
        if organizer_permalink is not UNSET:
            field_dict["organizerPermalink"] = organizer_permalink
        if comment is not UNSET:
            field_dict["comment"] = comment
        if room is not UNSET:
            field_dict["room"] = room
        if cisco_room is not UNSET:
            field_dict["ciscoRoom"] = cisco_room
        if cisco_settings is not UNSET:
            field_dict["ciscoSettings"] = cisco_settings
        if vinteo_room is not UNSET:
            field_dict["vinteoRoom"] = vinteo_room
        if vinteo_settings is not UNSET:
            field_dict["vinteoSettings"] = vinteo_settings
        if external_settings is not UNSET:
            field_dict["externalSettings"] = external_settings
        if cisco_settings_id is not UNSET:
            field_dict["ciscoSettingsId"] = cisco_settings_id
        if cisco_room_id is not UNSET:
            field_dict["ciscoRoomId"] = cisco_room_id
        if backend is not UNSET:
            field_dict["backend"] = backend
        if organized_user is not UNSET:
            field_dict["organizedUser"] = organized_user
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cisco_room_bare import CiscoRoomBare
        from ..models.cisco_vcs_setting_bare import CiscoVCSSettingBare
        from ..models.event_bare import EventBare
        from ..models.external_vcs_setting_out import ExternalVCSSettingOut
        from ..models.file_bare import FileBare
        from ..models.group_bare import GroupBare
        from ..models.meeting_recurrence_brief import MeetingRecurrenceBrief
        from ..models.participant_out import ParticipantOut
        from ..models.room_bare import RoomBare
        from ..models.user_brief import UserBrief
        from ..models.vinteo_room_bare import VinteoRoomBare
        from ..models.vinteo_vcs_setting_bare import VinteoVCSSettingBare

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_send_notifications_at(data: object) -> Union[datetime.datetime, int]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                send_notifications_at_type_1 = isoparse(data)

                return send_notifications_at_type_1
            except:  # noqa: E722
                pass
            return cast(Union[datetime.datetime, int], data)

        send_notifications_at = _parse_send_notifications_at(d.pop("sendNotificationsAt"))

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        is_governor_presents = d.pop("isGovernorPresents")

        created_at = isoparse(d.pop("createdAt"))

        state = MeetingStates(d.pop("state"))

        created_by = d.pop("createdBy")

        is_notify_accepted = d.pop("isNotifyAccepted")

        event = EventBare.from_dict(d.pop("event"))

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = ParticipantOut.from_dict(participants_item_data)

            participants.append(participants_item)

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = FileBare.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = GroupBare.from_dict(groups_item_data)

            groups.append(groups_item)

        event_id = d.pop("eventId")

        updated_at = isoparse(d.pop("updatedAt"))

        created_user = UserBrief.from_dict(d.pop("createdUser"))

        permalink_id = d.pop("permalinkId", UNSET)

        permalink = d.pop("permalink", UNSET)

        id = d.pop("id", UNSET)

        room_id = d.pop("roomId", UNSET)

        participants_count = d.pop("participantsCount", UNSET)

        duration = d.pop("duration", UNSET)

        _closed_at = d.pop("closedAt", UNSET)
        closed_at: Union[Unset, datetime.datetime]
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        organized_by = d.pop("organizedBy", UNSET)

        is_virtual = d.pop("isVirtual", UNSET)

        organizer_permalink_id = d.pop("organizerPermalinkId", UNSET)

        organizer_permalink = d.pop("organizerPermalink", UNSET)

        comment = d.pop("comment", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomBare]
        if isinstance(_room, Unset):
            room = UNSET
        else:
            room = RoomBare.from_dict(_room)

        _cisco_room = d.pop("ciscoRoom", UNSET)
        cisco_room: Union[Unset, CiscoRoomBare]
        if isinstance(_cisco_room, Unset):
            cisco_room = UNSET
        else:
            cisco_room = CiscoRoomBare.from_dict(_cisco_room)

        _cisco_settings = d.pop("ciscoSettings", UNSET)
        cisco_settings: Union[Unset, CiscoVCSSettingBare]
        if isinstance(_cisco_settings, Unset):
            cisco_settings = UNSET
        else:
            cisco_settings = CiscoVCSSettingBare.from_dict(_cisco_settings)

        _vinteo_room = d.pop("vinteoRoom", UNSET)
        vinteo_room: Union[Unset, VinteoRoomBare]
        if isinstance(_vinteo_room, Unset):
            vinteo_room = UNSET
        else:
            vinteo_room = VinteoRoomBare.from_dict(_vinteo_room)

        _vinteo_settings = d.pop("vinteoSettings", UNSET)
        vinteo_settings: Union[Unset, VinteoVCSSettingBare]
        if isinstance(_vinteo_settings, Unset):
            vinteo_settings = UNSET
        else:
            vinteo_settings = VinteoVCSSettingBare.from_dict(_vinteo_settings)

        _external_settings = d.pop("externalSettings", UNSET)
        external_settings: Union[Unset, ExternalVCSSettingOut]
        if isinstance(_external_settings, Unset):
            external_settings = UNSET
        else:
            external_settings = ExternalVCSSettingOut.from_dict(_external_settings)

        cisco_settings_id = d.pop("ciscoSettingsId", UNSET)

        cisco_room_id = d.pop("ciscoRoomId", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, MeetingBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = MeetingBackend(_backend)

        _organized_user = d.pop("organizedUser", UNSET)
        organized_user: Union[Unset, UserBrief]
        if isinstance(_organized_user, Unset):
            organized_user = UNSET
        else:
            organized_user = UserBrief.from_dict(_organized_user)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[Unset, MeetingRecurrenceBrief]
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = MeetingRecurrenceBrief.from_dict(_recurrence)

        meeting_full = cls(
            name=name,
            send_notifications_at=send_notifications_at,
            started_at=started_at,
            ended_at=ended_at,
            is_governor_presents=is_governor_presents,
            created_at=created_at,
            state=state,
            created_by=created_by,
            is_notify_accepted=is_notify_accepted,
            event=event,
            participants=participants,
            attachments=attachments,
            groups=groups,
            event_id=event_id,
            updated_at=updated_at,
            created_user=created_user,
            permalink_id=permalink_id,
            permalink=permalink,
            id=id,
            room_id=room_id,
            participants_count=participants_count,
            duration=duration,
            closed_at=closed_at,
            organized_by=organized_by,
            is_virtual=is_virtual,
            organizer_permalink_id=organizer_permalink_id,
            organizer_permalink=organizer_permalink,
            comment=comment,
            room=room,
            cisco_room=cisco_room,
            cisco_settings=cisco_settings,
            vinteo_room=vinteo_room,
            vinteo_settings=vinteo_settings,
            external_settings=external_settings,
            cisco_settings_id=cisco_settings_id,
            cisco_room_id=cisco_room_id,
            backend=backend,
            organized_user=organized_user,
            recurrence=recurrence,
        )

        meeting_full.additional_properties = d
        return meeting_full

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

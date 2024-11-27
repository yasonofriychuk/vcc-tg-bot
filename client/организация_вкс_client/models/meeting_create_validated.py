import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_backend import MeetingBackend
from ..models.meeting_recurrence_update_type import MeetingRecurrenceUpdateType
from ..models.meeting_states import MeetingStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cisco_vcs_setting_create import CiscoVCSSettingCreate
    from ..models.external_vcs_setting_create import ExternalVCSSettingCreate
    from ..models.id_mixin import IdMixin
    from ..models.meeting_recurrence_create import MeetingRecurrenceCreate
    from ..models.participant_create import ParticipantCreate
    from ..models.participant_mock import ParticipantMock
    from ..models.vinteo_vcs_setting_create import VinteoVCSSettingCreate


T = TypeVar("T", bound="MeetingCreateValidated")


@_attrs_define
class MeetingCreateValidated:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):
        send_notifications_at (Union[datetime.datetime, int]):  Example: 2024-11-27T16:32:19.794033.
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.794310.
        participants (List[Union['ParticipantCreate', 'ParticipantMock']]): Перечень участников ВКС. Если указан только
            **id**, то будет произведён поиск по уже существующим в системе пользователям, иначе пользователь будет создан
        attachments (Union[Unset, List[str]]): Перечень идентификаторов файлов, которые будут вложены при рассылке
        room_id (Union[Unset, int]):
        comment (Union[Unset, str]):
        participants_count (Union[Unset, int]):
        cisco_settings (Union[Unset, CiscoVCSSettingCreate]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        vinteo_settings (Union[Unset, VinteoVCSSettingCreate]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        external_settings (Union[Unset, ExternalVCSSettingCreate]): Промежуточная модель pydantic'а для унифицирования
            конфигов и удобного администрирования
        ended_at (Union[Unset, datetime.datetime]):  Example: 2024-11-27T20:32:19.794324.
        duration (Union[Unset, int]): Продолжительность ВКС в минутах
        is_governor_presents (Union[Unset, bool]): На данной ВКС присутствует губернатор Default: False.
        is_notify_accepted (Union[Unset, bool]): Получать уведомление о принявших приглашение на встречу Default: False.
        groups (Union[Unset, List['IdMixin']]): Идентификаторы групп, члены которой будут участниками ВКС
        recurrence (Union[Unset, MeetingRecurrenceCreate]): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования
        recurrence_update_type (Union[Unset, MeetingRecurrenceUpdateType]): An enumeration.
        is_virtual (Union[Unset, bool]): Является ли ВКС виртуально созданным объектом (флаг нужен для повторяющихся
            ВКС) Default: False.
        state (Union[Unset, MeetingStates]): Перечень состояний, в которых может находиться сущность ВКС
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default: MeetingBackend.CISCO.
        organized_by (Union['ParticipantCreate', 'ParticipantMock', Unset]): Организатор мероприятия. Можно указать
            идентификатор существующего пользователя, а также почту пользователя, которого нет в системе - в таком случае
            пользователь будет создан. Если указать почту существующего пользователя - будет взят первый найденный с такой
            почтой пользователь.
    """

    name: str
    send_notifications_at: Union[datetime.datetime, int]
    started_at: datetime.datetime
    participants: List[Union["ParticipantCreate", "ParticipantMock"]]
    attachments: Union[Unset, List[str]] = UNSET
    room_id: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    participants_count: Union[Unset, int] = UNSET
    cisco_settings: Union[Unset, "CiscoVCSSettingCreate"] = UNSET
    vinteo_settings: Union[Unset, "VinteoVCSSettingCreate"] = UNSET
    external_settings: Union[Unset, "ExternalVCSSettingCreate"] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    is_governor_presents: Union[Unset, bool] = False
    is_notify_accepted: Union[Unset, bool] = False
    groups: Union[Unset, List["IdMixin"]] = UNSET
    recurrence: Union[Unset, "MeetingRecurrenceCreate"] = UNSET
    recurrence_update_type: Union[Unset, MeetingRecurrenceUpdateType] = UNSET
    is_virtual: Union[Unset, bool] = False
    state: Union[Unset, MeetingStates] = UNSET
    backend: Union[Unset, MeetingBackend] = MeetingBackend.CISCO
    organized_by: Union["ParticipantCreate", "ParticipantMock", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.participant_mock import ParticipantMock

        name = self.name

        send_notifications_at: Union[int, str]
        if isinstance(self.send_notifications_at, datetime.datetime):
            send_notifications_at = self.send_notifications_at.isoformat()
        else:
            send_notifications_at = self.send_notifications_at

        started_at = self.started_at.isoformat()

        participants = []
        for participants_item_data in self.participants:
            participants_item: Dict[str, Any]
            if isinstance(participants_item_data, ParticipantMock):
                participants_item = participants_item_data.to_dict()
            else:
                participants_item = participants_item_data.to_dict()

            participants.append(participants_item)

        attachments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        room_id = self.room_id

        comment = self.comment

        participants_count = self.participants_count

        cisco_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cisco_settings, Unset):
            cisco_settings = self.cisco_settings.to_dict()

        vinteo_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vinteo_settings, Unset):
            vinteo_settings = self.vinteo_settings.to_dict()

        external_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_settings, Unset):
            external_settings = self.external_settings.to_dict()

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        duration = self.duration

        is_governor_presents = self.is_governor_presents

        is_notify_accepted = self.is_notify_accepted

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        recurrence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        recurrence_update_type: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence_update_type, Unset):
            recurrence_update_type = self.recurrence_update_type.value

        is_virtual = self.is_virtual

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        organized_by: Union[Dict[str, Any], Unset]
        if isinstance(self.organized_by, Unset):
            organized_by = UNSET
        elif isinstance(self.organized_by, ParticipantMock):
            organized_by = self.organized_by.to_dict()
        else:
            organized_by = self.organized_by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sendNotificationsAt": send_notifications_at,
                "startedAt": started_at,
                "participants": participants,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if cisco_settings is not UNSET:
            field_dict["ciscoSettings"] = cisco_settings
        if vinteo_settings is not UNSET:
            field_dict["vinteoSettings"] = vinteo_settings
        if external_settings is not UNSET:
            field_dict["externalSettings"] = external_settings
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_governor_presents is not UNSET:
            field_dict["isGovernorPresents"] = is_governor_presents
        if is_notify_accepted is not UNSET:
            field_dict["isNotifyAccepted"] = is_notify_accepted
        if groups is not UNSET:
            field_dict["groups"] = groups
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if recurrence_update_type is not UNSET:
            field_dict["recurrenceUpdateType"] = recurrence_update_type
        if is_virtual is not UNSET:
            field_dict["isVirtual"] = is_virtual
        if state is not UNSET:
            field_dict["state"] = state
        if backend is not UNSET:
            field_dict["backend"] = backend
        if organized_by is not UNSET:
            field_dict["organizedBy"] = organized_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cisco_vcs_setting_create import CiscoVCSSettingCreate
        from ..models.external_vcs_setting_create import ExternalVCSSettingCreate
        from ..models.id_mixin import IdMixin
        from ..models.meeting_recurrence_create import MeetingRecurrenceCreate
        from ..models.participant_create import ParticipantCreate
        from ..models.participant_mock import ParticipantMock
        from ..models.vinteo_vcs_setting_create import VinteoVCSSettingCreate

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

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:

            def _parse_participants_item(data: object) -> Union["ParticipantCreate", "ParticipantMock"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    participants_item_type_0 = ParticipantMock.from_dict(data)

                    return participants_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                participants_item_type_1 = ParticipantCreate.from_dict(data)

                return participants_item_type_1

            participants_item = _parse_participants_item(participants_item_data)

            participants.append(participants_item)

        attachments = cast(List[str], d.pop("attachments", UNSET))

        room_id = d.pop("roomId", UNSET)

        comment = d.pop("comment", UNSET)

        participants_count = d.pop("participantsCount", UNSET)

        _cisco_settings = d.pop("ciscoSettings", UNSET)
        cisco_settings: Union[Unset, CiscoVCSSettingCreate]
        if isinstance(_cisco_settings, Unset):
            cisco_settings = UNSET
        else:
            cisco_settings = CiscoVCSSettingCreate.from_dict(_cisco_settings)

        _vinteo_settings = d.pop("vinteoSettings", UNSET)
        vinteo_settings: Union[Unset, VinteoVCSSettingCreate]
        if isinstance(_vinteo_settings, Unset):
            vinteo_settings = UNSET
        else:
            vinteo_settings = VinteoVCSSettingCreate.from_dict(_vinteo_settings)

        _external_settings = d.pop("externalSettings", UNSET)
        external_settings: Union[Unset, ExternalVCSSettingCreate]
        if isinstance(_external_settings, Unset):
            external_settings = UNSET
        else:
            external_settings = ExternalVCSSettingCreate.from_dict(_external_settings)

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        duration = d.pop("duration", UNSET)

        is_governor_presents = d.pop("isGovernorPresents", UNSET)

        is_notify_accepted = d.pop("isNotifyAccepted", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = IdMixin.from_dict(groups_item_data)

            groups.append(groups_item)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[Unset, MeetingRecurrenceCreate]
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = MeetingRecurrenceCreate.from_dict(_recurrence)

        _recurrence_update_type = d.pop("recurrenceUpdateType", UNSET)
        recurrence_update_type: Union[Unset, MeetingRecurrenceUpdateType]
        if isinstance(_recurrence_update_type, Unset):
            recurrence_update_type = UNSET
        else:
            recurrence_update_type = MeetingRecurrenceUpdateType(_recurrence_update_type)

        is_virtual = d.pop("isVirtual", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, MeetingStates]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MeetingStates(_state)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, MeetingBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = MeetingBackend(_backend)

        def _parse_organized_by(data: object) -> Union["ParticipantCreate", "ParticipantMock", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organized_by_type_0 = ParticipantMock.from_dict(data)

                return organized_by_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            organized_by_type_1 = ParticipantCreate.from_dict(data)

            return organized_by_type_1

        organized_by = _parse_organized_by(d.pop("organizedBy", UNSET))

        meeting_create_validated = cls(
            name=name,
            send_notifications_at=send_notifications_at,
            started_at=started_at,
            participants=participants,
            attachments=attachments,
            room_id=room_id,
            comment=comment,
            participants_count=participants_count,
            cisco_settings=cisco_settings,
            vinteo_settings=vinteo_settings,
            external_settings=external_settings,
            ended_at=ended_at,
            duration=duration,
            is_governor_presents=is_governor_presents,
            is_notify_accepted=is_notify_accepted,
            groups=groups,
            recurrence=recurrence,
            recurrence_update_type=recurrence_update_type,
            is_virtual=is_virtual,
            state=state,
            backend=backend,
            organized_by=organized_by,
        )

        meeting_create_validated.additional_properties = d
        return meeting_create_validated

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

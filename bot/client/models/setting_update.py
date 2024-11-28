from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meeting_backend import MeetingBackend

T = TypeVar("T", bound="SettingUpdate")


@_attrs_define
class SettingUpdate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        backend (MeetingBackend): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        drop_ended_conference_after (int): Количество часов, по истечению которых после окончания конференции будет
            происходить удаление комнаты
        enable_conference_before (int): Количество часов, передначалом самой конференции, когда комната уже должна быть
            создана
        max_participants (int): Максимальное количество участников во всех конференциях в моменте
        max_conferences (int): Максимальное количество всех конференций в моменте
        max_private_license_conferences (int): Максимальное количество конференций с персональными лицензиями в моменте
        call_leg_profile_for_organizer (str): Идентификатор настроек (callLegProfile) для организаторов конференций
        private_licence_owner_jid (str): JID пользовтеля-владельца персональных лицензий
    """

    backend: MeetingBackend
    drop_ended_conference_after: int
    enable_conference_before: int
    max_participants: int
    max_conferences: int
    max_private_license_conferences: int
    call_leg_profile_for_organizer: str
    private_licence_owner_jid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backend = self.backend.value

        drop_ended_conference_after = self.drop_ended_conference_after

        enable_conference_before = self.enable_conference_before

        max_participants = self.max_participants

        max_conferences = self.max_conferences

        max_private_license_conferences = self.max_private_license_conferences

        call_leg_profile_for_organizer = self.call_leg_profile_for_organizer

        private_licence_owner_jid = self.private_licence_owner_jid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backend": backend,
                "dropEndedConferenceAfter": drop_ended_conference_after,
                "enableConferenceBefore": enable_conference_before,
                "maxParticipants": max_participants,
                "maxConferences": max_conferences,
                "maxPrivateLicenseConferences": max_private_license_conferences,
                "callLegProfileForOrganizer": call_leg_profile_for_organizer,
                "privateLicenceOwnerJid": private_licence_owner_jid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backend = MeetingBackend(d.pop("backend"))

        drop_ended_conference_after = d.pop("dropEndedConferenceAfter")

        enable_conference_before = d.pop("enableConferenceBefore")

        max_participants = d.pop("maxParticipants")

        max_conferences = d.pop("maxConferences")

        max_private_license_conferences = d.pop("maxPrivateLicenseConferences")

        call_leg_profile_for_organizer = d.pop("callLegProfileForOrganizer")

        private_licence_owner_jid = d.pop("privateLicenceOwnerJid")

        setting_update = cls(
            backend=backend,
            drop_ended_conference_after=drop_ended_conference_after,
            enable_conference_before=enable_conference_before,
            max_participants=max_participants,
            max_conferences=max_conferences,
            max_private_license_conferences=max_private_license_conferences,
            call_leg_profile_for_organizer=call_leg_profile_for_organizer,
            private_licence_owner_jid=private_licence_owner_jid,
        )

        setting_update.additional_properties = d
        return setting_update

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

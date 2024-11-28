from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meeting_backend import MeetingBackend
from ..models.vinteo_fps import VinteoFPS
from ..models.vinteo_resolutions import VinteoResolutions
from ..types import UNSET, Unset

T = TypeVar("T", bound="VinteoGlobalSettingUpdate")


@_attrs_define
class VinteoGlobalSettingUpdate:
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
        fps (Union[Unset, VinteoFPS]): An enumeration. Default: VinteoFPS.VALUE_60.
        resolution (Union[Unset, VinteoResolutions]): An enumeration. Default: VinteoResolutions.VALUE_3.
    """

    backend: MeetingBackend
    drop_ended_conference_after: int
    enable_conference_before: int
    max_participants: int
    fps: Union[Unset, VinteoFPS] = VinteoFPS.VALUE_60
    resolution: Union[Unset, VinteoResolutions] = VinteoResolutions.VALUE_3
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backend = self.backend.value

        drop_ended_conference_after = self.drop_ended_conference_after

        enable_conference_before = self.enable_conference_before

        max_participants = self.max_participants

        fps: Union[Unset, int] = UNSET
        if not isinstance(self.fps, Unset):
            fps = self.fps.value

        resolution: Union[Unset, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backend": backend,
                "dropEndedConferenceAfter": drop_ended_conference_after,
                "enableConferenceBefore": enable_conference_before,
                "maxParticipants": max_participants,
            }
        )
        if fps is not UNSET:
            field_dict["fps"] = fps
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backend = MeetingBackend(d.pop("backend"))

        drop_ended_conference_after = d.pop("dropEndedConferenceAfter")

        enable_conference_before = d.pop("enableConferenceBefore")

        max_participants = d.pop("maxParticipants")

        _fps = d.pop("fps", UNSET)
        fps: Union[Unset, VinteoFPS]
        if isinstance(_fps, Unset):
            fps = UNSET
        else:
            fps = VinteoFPS(_fps)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, VinteoResolutions]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = VinteoResolutions(_resolution)

        vinteo_global_setting_update = cls(
            backend=backend,
            drop_ended_conference_after=drop_ended_conference_after,
            enable_conference_before=enable_conference_before,
            max_participants=max_participants,
            fps=fps,
            resolution=resolution,
        )

        vinteo_global_setting_update.additional_properties = d
        return vinteo_global_setting_update

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

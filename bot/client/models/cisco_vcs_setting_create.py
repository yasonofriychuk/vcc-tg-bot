from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CiscoVCSSettingCreate")


@_attrs_define
class CiscoVCSSettingCreate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        is_microphone_on (bool):
        is_video_on (bool):
        is_waiting_room_enabled (bool):
        need_video_recording (Union[Unset, bool]): Необходимо ли осуществлять видеозапись ВКС. При выборе, запись буде
            автоматически начата и закончена в соответствии с указанным временем проведения ВКС. Записи будут доступны после
            завершения ВКС Default: False.
    """

    is_microphone_on: bool
    is_video_on: bool
    is_waiting_room_enabled: bool
    need_video_recording: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_microphone_on = self.is_microphone_on

        is_video_on = self.is_video_on

        is_waiting_room_enabled = self.is_waiting_room_enabled

        need_video_recording = self.need_video_recording

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isMicrophoneOn": is_microphone_on,
                "isVideoOn": is_video_on,
                "isWaitingRoomEnabled": is_waiting_room_enabled,
            }
        )
        if need_video_recording is not UNSET:
            field_dict["needVideoRecording"] = need_video_recording

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_microphone_on = d.pop("isMicrophoneOn")

        is_video_on = d.pop("isVideoOn")

        is_waiting_room_enabled = d.pop("isWaitingRoomEnabled")

        need_video_recording = d.pop("needVideoRecording", UNSET)

        cisco_vcs_setting_create = cls(
            is_microphone_on=is_microphone_on,
            is_video_on=is_video_on,
            is_waiting_room_enabled=is_waiting_room_enabled,
            need_video_recording=need_video_recording,
        )

        cisco_vcs_setting_create.additional_properties = d
        return cisco_vcs_setting_create

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

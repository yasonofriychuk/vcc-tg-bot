from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VinteoVCSSettingBare")


@_attrs_define
class VinteoVCSSettingBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):  Example: 1.
        need_video_recording (Union[Unset, bool]): Необходимо ли осуществлять видеозапись ВКС. При выборе, запись буде
            автоматически начата и закончена в соответствии с указанным временем проведения ВКС. Записи будут доступны после
            завершения ВКС Default: False.
    """

    id: int
    need_video_recording: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        need_video_recording = self.need_video_recording

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if need_video_recording is not UNSET:
            field_dict["needVideoRecording"] = need_video_recording

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        need_video_recording = d.pop("needVideoRecording", UNSET)

        vinteo_vcs_setting_bare = cls(
            id=id,
            need_video_recording=need_video_recording,
        )

        vinteo_vcs_setting_bare.additional_properties = d
        return vinteo_vcs_setting_bare

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

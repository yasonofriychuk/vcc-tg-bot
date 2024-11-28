from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_response_warning_info_item import StatusResponseWarningInfoItem


T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """Формат ответа для запросов, в которых не требуется отдавать данные

    Attributes:
        status (Union[Unset, str]):  Default: 'ok'.
        warning (Union[Unset, str]):
        warning_info (Union[Unset, List['StatusResponseWarningInfoItem']]):
    """

    status: Union[Unset, str] = "ok"
    warning: Union[Unset, str] = UNSET
    warning_info: Union[Unset, List["StatusResponseWarningInfoItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        warning = self.warning

        warning_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warning_info, Unset):
            warning_info = []
            for warning_info_item_data in self.warning_info:
                warning_info_item = warning_info_item_data.to_dict()
                warning_info.append(warning_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if warning is not UNSET:
            field_dict["warning"] = warning
        if warning_info is not UNSET:
            field_dict["warning_info"] = warning_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_response_warning_info_item import StatusResponseWarningInfoItem

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        warning = d.pop("warning", UNSET)

        warning_info = []
        _warning_info = d.pop("warning_info", UNSET)
        for warning_info_item_data in _warning_info or []:
            warning_info_item = StatusResponseWarningInfoItem.from_dict(warning_info_item_data)

            warning_info.append(warning_info_item)

        status_response = cls(
            status=status,
            warning=warning,
            warning_info=warning_info,
        )

        status_response.additional_properties = d
        return status_response

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_bare import MeetingBare


T = TypeVar("T", bound="MeetingList")


@_attrs_define
class MeetingList:
    """Формат выдачи для всех списков объектов (multiple get)

    Attributes:
        data (List['MeetingBare']):
        rows_per_page (Union[Unset, int]):
        page (Union[Unset, int]):
        rows_number (Union[Unset, int]):
        show_deleted (Union[Unset, bool]):  Default: False.
        sort_by (Union[Unset, str]):  Default: 'id'.
    """

    data: List["MeetingBare"]
    rows_per_page: Union[Unset, int] = UNSET
    page: Union[Unset, int] = UNSET
    rows_number: Union[Unset, int] = UNSET
    show_deleted: Union[Unset, bool] = False
    sort_by: Union[Unset, str] = "id"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        rows_per_page = self.rows_per_page

        page = self.page

        rows_number = self.rows_number

        show_deleted = self.show_deleted

        sort_by = self.sort_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if rows_per_page is not UNSET:
            field_dict["rowsPerPage"] = rows_per_page
        if page is not UNSET:
            field_dict["page"] = page
        if rows_number is not UNSET:
            field_dict["rowsNumber"] = rows_number
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meeting_bare import MeetingBare

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MeetingBare.from_dict(data_item_data)

            data.append(data_item)

        rows_per_page = d.pop("rowsPerPage", UNSET)

        page = d.pop("page", UNSET)

        rows_number = d.pop("rowsNumber", UNSET)

        show_deleted = d.pop("showDeleted", UNSET)

        sort_by = d.pop("sortBy", UNSET)

        meeting_list = cls(
            data=data,
            rows_per_page=rows_per_page,
            page=page,
            rows_number=rows_number,
            show_deleted=show_deleted,
            sort_by=sort_by,
        )

        meeting_list.additional_properties = d
        return meeting_list

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
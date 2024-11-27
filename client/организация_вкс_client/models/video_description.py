import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoDescription")


@_attrs_define
class VideoDescription:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (str):
        name (str):
        extension (str):
        created_at (datetime.datetime):
        size (Union[Unset, int]): размер в байтах
    """

    id: str
    name: str
    extension: str
    created_at: datetime.datetime
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        extension = self.extension

        created_at = self.created_at.isoformat()

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "extension": extension,
                "createdAt": created_at,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        extension = d.pop("extension")

        created_at = isoparse(d.pop("createdAt"))

        size = d.pop("size", UNSET)

        video_description = cls(
            id=id,
            name=name,
            extension=extension,
            created_at=created_at,
            size=size,
        )

        video_description.additional_properties = d
        return video_description

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

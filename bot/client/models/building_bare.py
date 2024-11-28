from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BuildingBare")


@_attrs_define
class BuildingBare:
    """Базовая модель для выдачи любого каталога

    Attributes:
        name (str):
        description (str):
        id (int):
        address (str):  Example: г.Ханты-Мансийск ул. Мира д.151.
        municipal_area_id (int):  Example: 1.
    """

    name: str
    description: str
    id: int
    address: str
    municipal_area_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        id = self.id

        address = self.address

        municipal_area_id = self.municipal_area_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "id": id,
                "address": address,
                "municipalAreaId": municipal_area_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        id = d.pop("id")

        address = d.pop("address")

        municipal_area_id = d.pop("municipalAreaId")

        building_bare = cls(
            name=name,
            description=description,
            id=id,
            address=address,
            municipal_area_id=municipal_area_id,
        )

        building_bare.additional_properties = d
        return building_bare

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

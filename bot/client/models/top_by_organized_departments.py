from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.department_brief import DepartmentBrief


T = TypeVar("T", bound="TopByOrganizedDepartments")


@_attrs_define
class TopByOrganizedDepartments:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        count (int):
        department (DepartmentBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
    """

    count: int
    department: "DepartmentBrief"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        department = self.department.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "department": department,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.department_brief import DepartmentBrief

        d = src_dict.copy()
        count = d.pop("count")

        department = DepartmentBrief.from_dict(d.pop("department"))

        top_by_organized_departments = cls(
            count=count,
            department=department,
        )

        top_by_organized_departments.additional_properties = d
        return top_by_organized_departments

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

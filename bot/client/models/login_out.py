from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_out_tutorials_progress import LoginOutTutorialsProgress
    from ..models.user_info_out import UserInfoOut


T = TypeVar("T", bound="LoginOut")


@_attrs_define
class LoginOut:
    """
    Attributes:
        token (str): JWT токен пользователя
        user (UserInfoOut): Перечень полей пользователя, передаваемых при авторизации вместе с JWT токеном
        tutorials_progress (Union[Unset, LoginOutTutorialsProgress]):
    """

    token: str
    user: "UserInfoOut"
    tutorials_progress: Union[Unset, "LoginOutTutorialsProgress"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        user = self.user.to_dict()

        tutorials_progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tutorials_progress, Unset):
            tutorials_progress = self.tutorials_progress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "user": user,
            }
        )
        if tutorials_progress is not UNSET:
            field_dict["tutorials_progress"] = tutorials_progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.login_out_tutorials_progress import LoginOutTutorialsProgress
        from ..models.user_info_out import UserInfoOut

        d = src_dict.copy()
        token = d.pop("token")

        user = UserInfoOut.from_dict(d.pop("user"))

        _tutorials_progress = d.pop("tutorials_progress", UNSET)
        tutorials_progress: Union[Unset, LoginOutTutorialsProgress]
        if isinstance(_tutorials_progress, Unset):
            tutorials_progress = UNSET
        else:
            tutorials_progress = LoginOutTutorialsProgress.from_dict(_tutorials_progress)

        login_out = cls(
            token=token,
            user=user,
            tutorials_progress=tutorials_progress,
        )

        login_out.additional_properties = d
        return login_out

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

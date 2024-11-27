from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_ldap_login_auth_ldap_login_post_fingerprint import BodyLdapLoginAuthLdapLoginPostFingerprint


T = TypeVar("T", bound="BodyLdapLoginAuthLdapLoginPost")


@_attrs_define
class BodyLdapLoginAuthLdapLoginPost:
    """
    Attributes:
        login (str):
        password (str):
        fingerprint (Union[Unset, BodyLdapLoginAuthLdapLoginPostFingerprint]):
    """

    login: str
    password: str
    fingerprint: Union[Unset, "BodyLdapLoginAuthLdapLoginPostFingerprint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        password = self.password

        fingerprint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fingerprint, Unset):
            fingerprint = self.fingerprint.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "password": password,
            }
        )
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.body_ldap_login_auth_ldap_login_post_fingerprint import BodyLdapLoginAuthLdapLoginPostFingerprint

        d = src_dict.copy()
        login = d.pop("login")

        password = d.pop("password")

        _fingerprint = d.pop("fingerprint", UNSET)
        fingerprint: Union[Unset, BodyLdapLoginAuthLdapLoginPostFingerprint]
        if isinstance(_fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = BodyLdapLoginAuthLdapLoginPostFingerprint.from_dict(_fingerprint)

        body_ldap_login_auth_ldap_login_post = cls(
            login=login,
            password=password,
            fingerprint=fingerprint,
        )

        body_ldap_login_auth_ldap_login_post.additional_properties = d
        return body_ldap_login_auth_ldap_login_post

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

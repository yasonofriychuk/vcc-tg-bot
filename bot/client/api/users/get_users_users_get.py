from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_list_out import UserListOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    show_deleted: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["rowsPerPage"] = rows_per_page

    params["showDeleted"] = show_deleted

    params["name"] = name

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserListOut]]:
    if response.status_code == 200:
        response_200 = UserListOut.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, UserListOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    show_deleted: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserListOut]]:
    """Get Users

     Просмотр всех пользователей в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        show_deleted (Union[Unset, bool]): отображать удалённых пользователей Default: False.
        name (Union[Unset, str]): ilike поиск по ФИО
        email (Union[Unset, str]): ilike поиск по email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserListOut]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        show_deleted=show_deleted,
        name=name,
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    show_deleted: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserListOut]]:
    """Get Users

     Просмотр всех пользователей в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        show_deleted (Union[Unset, bool]): отображать удалённых пользователей Default: False.
        name (Union[Unset, str]): ilike поиск по ФИО
        email (Union[Unset, str]): ilike поиск по email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserListOut]
    """

    return sync_detailed(
        client=client,
        page=page,
        rows_per_page=rows_per_page,
        show_deleted=show_deleted,
        name=name,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    show_deleted: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserListOut]]:
    """Get Users

     Просмотр всех пользователей в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        show_deleted (Union[Unset, bool]): отображать удалённых пользователей Default: False.
        name (Union[Unset, str]): ilike поиск по ФИО
        email (Union[Unset, str]): ilike поиск по email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserListOut]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        show_deleted=show_deleted,
        name=name,
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    show_deleted: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserListOut]]:
    """Get Users

     Просмотр всех пользователей в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        show_deleted (Union[Unset, bool]): отображать удалённых пользователей Default: False.
        name (Union[Unset, str]): ilike поиск по ФИО
        email (Union[Unset, str]): ilike поиск по email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserListOut]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            rows_per_page=rows_per_page,
            show_deleted=show_deleted,
            name=name,
            email=email,
        )
    ).parsed

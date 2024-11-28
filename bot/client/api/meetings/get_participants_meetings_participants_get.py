from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_list_brief import UserListBrief
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: Union[Unset, str] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["filter"] = filter_

    params["department_id"] = department_id

    params["page"] = page

    params["rowsPerPage"] = rows_per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/meetings/participants",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserListBrief]]:
    if response.status_code == 200:
        response_200 = UserListBrief.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, UserListBrief]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserListBrief]]:
    """Get Participants

     Просмотр всех участников, в системе.
    Под участниками понимаются все пользователи (зарегистрированные системы и ранее приглашённые в любую
    ВКС)

    Args:
        filter_ (Union[Unset, str]):
        department_id (Union[Unset, int]): департамент, в котором состоят пользователи
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserListBrief]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        department_id=department_id,
        page=page,
        rows_per_page=rows_per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserListBrief]]:
    """Get Participants

     Просмотр всех участников, в системе.
    Под участниками понимаются все пользователи (зарегистрированные системы и ранее приглашённые в любую
    ВКС)

    Args:
        filter_ (Union[Unset, str]):
        department_id (Union[Unset, int]): департамент, в котором состоят пользователи
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserListBrief]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        department_id=department_id,
        page=page,
        rows_per_page=rows_per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
) -> Response[Union[Any, HTTPValidationError, UserListBrief]]:
    """Get Participants

     Просмотр всех участников, в системе.
    Под участниками понимаются все пользователи (зарегистрированные системы и ранее приглашённые в любую
    ВКС)

    Args:
        filter_ (Union[Unset, str]):
        department_id (Union[Unset, int]): департамент, в котором состоят пользователи
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserListBrief]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        department_id=department_id,
        page=page,
        rows_per_page=rows_per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, str] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, UserListBrief]]:
    """Get Participants

     Просмотр всех участников, в системе.
    Под участниками понимаются все пользователи (зарегистрированные системы и ранее приглашённые в любую
    ВКС)

    Args:
        filter_ (Union[Unset, str]):
        department_id (Union[Unset, int]): департамент, в котором состоят пользователи
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserListBrief]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            department_id=department_id,
            page=page,
            rows_per_page=rows_per_page,
        )
    ).parsed
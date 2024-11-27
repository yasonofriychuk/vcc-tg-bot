from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.department_list import DepartmentList
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["rowsPerPage"] = rows_per_page

    params["name"] = name

    params["sortBy"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/catalogs/departments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DepartmentList, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = DepartmentList.from_dict(response.json())

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
) -> Response[Union[Any, DepartmentList, HTTPValidationError]]:
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
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Response[Union[Any, DepartmentList, HTTPValidationError]]:
    """Get Departments

     Получение всех департаментов, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        name (Union[Unset, str]): ilike поиск по названию
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DepartmentList, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        name=name,
        sort_by=sort_by,
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
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Optional[Union[Any, DepartmentList, HTTPValidationError]]:
    """Get Departments

     Получение всех департаментов, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        name (Union[Unset, str]): ilike поиск по названию
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DepartmentList, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        page=page,
        rows_per_page=rows_per_page,
        name=name,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Response[Union[Any, DepartmentList, HTTPValidationError]]:
    """Get Departments

     Получение всех департаментов, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        name (Union[Unset, str]): ilike поиск по названию
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DepartmentList, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        name=name,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Optional[Union[Any, DepartmentList, HTTPValidationError]]:
    """Get Departments

     Получение всех департаментов, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        name (Union[Unset, str]): ilike поиск по названию
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DepartmentList, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            rows_per_page=rows_per_page,
            name=name,
            sort_by=sort_by,
        )
    ).parsed

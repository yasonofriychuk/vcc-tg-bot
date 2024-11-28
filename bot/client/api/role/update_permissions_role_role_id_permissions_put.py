from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.role_bare import RoleBare
from ...types import Response


def _get_kwargs(
    role_id: int,
    *,
    body: List[str],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/role/{role_id}/permissions",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, RoleBare]]:
    if response.status_code == 200:
        response_200 = RoleBare.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, RoleBare]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: int,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Response[Union[Any, HTTPValidationError, RoleBare]]:
    """Update Permissions

     Получение информации о конкретной роли

    Args:
        role_id (int):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, RoleBare]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: int,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Optional[Union[Any, HTTPValidationError, RoleBare]]:
    """Update Permissions

     Получение информации о конкретной роли

    Args:
        role_id (int):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, RoleBare]
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    role_id: int,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Response[Union[Any, HTTPValidationError, RoleBare]]:
    """Update Permissions

     Получение информации о конкретной роли

    Args:
        role_id (int):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, RoleBare]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: int,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Optional[Union[Any, HTTPValidationError, RoleBare]]:
    """Update Permissions

     Получение информации о конкретной роли

    Args:
        role_id (int):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, RoleBare]
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            body=body,
        )
    ).parsed
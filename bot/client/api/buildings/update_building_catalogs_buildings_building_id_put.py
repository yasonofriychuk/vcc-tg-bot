from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.building_create import BuildingCreate
from ...models.building_full import BuildingFull
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    building_id: int,
    *,
    body: BuildingCreate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/catalogs/buildings/{building_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BuildingFull, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = BuildingFull.from_dict(response.json())

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
) -> Response[Union[Any, BuildingFull, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    building_id: int,
    *,
    client: AuthenticatedClient,
    body: BuildingCreate,
) -> Response[Union[Any, BuildingFull, HTTPValidationError]]:
    """Update Building

     Обновление информации о строении

    Args:
        building_id (int):
        body (BuildingCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BuildingFull, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        building_id=building_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    building_id: int,
    *,
    client: AuthenticatedClient,
    body: BuildingCreate,
) -> Optional[Union[Any, BuildingFull, HTTPValidationError]]:
    """Update Building

     Обновление информации о строении

    Args:
        building_id (int):
        body (BuildingCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BuildingFull, HTTPValidationError]
    """

    return sync_detailed(
        building_id=building_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    building_id: int,
    *,
    client: AuthenticatedClient,
    body: BuildingCreate,
) -> Response[Union[Any, BuildingFull, HTTPValidationError]]:
    """Update Building

     Обновление информации о строении

    Args:
        building_id (int):
        body (BuildingCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BuildingFull, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        building_id=building_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    building_id: int,
    *,
    client: AuthenticatedClient,
    body: BuildingCreate,
) -> Optional[Union[Any, BuildingFull, HTTPValidationError]]:
    """Update Building

     Обновление информации о строении

    Args:
        building_id (int):
        body (BuildingCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BuildingFull, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            building_id=building_id,
            client=client,
            body=body,
        )
    ).parsed
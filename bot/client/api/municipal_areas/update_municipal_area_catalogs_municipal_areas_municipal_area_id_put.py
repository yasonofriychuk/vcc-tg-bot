from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_element_bare import CatalogElementBare
from ...models.catalog_element_create import CatalogElementCreate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    municipal_area_id: int,
    *,
    body: CatalogElementCreate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/catalogs/municipal-areas/{municipal_area_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CatalogElementBare, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = CatalogElementBare.from_dict(response.json())

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
) -> Response[Union[Any, CatalogElementBare, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    municipal_area_id: int,
    *,
    client: AuthenticatedClient,
    body: CatalogElementCreate,
) -> Response[Union[Any, CatalogElementBare, HTTPValidationError]]:
    """Update Municipal Area

     Обновление информации о муниципальном образовании

    Args:
        municipal_area_id (int):
        body (CatalogElementCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CatalogElementBare, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        municipal_area_id=municipal_area_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    municipal_area_id: int,
    *,
    client: AuthenticatedClient,
    body: CatalogElementCreate,
) -> Optional[Union[Any, CatalogElementBare, HTTPValidationError]]:
    """Update Municipal Area

     Обновление информации о муниципальном образовании

    Args:
        municipal_area_id (int):
        body (CatalogElementCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CatalogElementBare, HTTPValidationError]
    """

    return sync_detailed(
        municipal_area_id=municipal_area_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    municipal_area_id: int,
    *,
    client: AuthenticatedClient,
    body: CatalogElementCreate,
) -> Response[Union[Any, CatalogElementBare, HTTPValidationError]]:
    """Update Municipal Area

     Обновление информации о муниципальном образовании

    Args:
        municipal_area_id (int):
        body (CatalogElementCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CatalogElementBare, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        municipal_area_id=municipal_area_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    municipal_area_id: int,
    *,
    client: AuthenticatedClient,
    body: CatalogElementCreate,
) -> Optional[Union[Any, CatalogElementBare, HTTPValidationError]]:
    """Update Municipal Area

     Обновление информации о муниципальном образовании

    Args:
        municipal_area_id (int):
        body (CatalogElementCreate): Базовая модель для любого каталога

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CatalogElementBare, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            municipal_area_id=municipal_area_id,
            client=client,
            body=body,
        )
    ).parsed

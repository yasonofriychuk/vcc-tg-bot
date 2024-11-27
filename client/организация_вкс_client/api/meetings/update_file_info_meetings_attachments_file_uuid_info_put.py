from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_create import FileCreate
from ...models.file_full import FileFull
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    file_uuid: UUID,
    *,
    body: FileCreate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/meetings/attachments/{file_uuid}/info",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FileFull, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FileFull.from_dict(response.json())

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
) -> Response[Union[Any, FileFull, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: FileCreate,
) -> Response[Union[Any, FileFull, HTTPValidationError]]:
    """Update File Info

     Получает информацию о файле

    Args:
        file_uuid (UUID):
        body (FileCreate): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FileFull, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_uuid=file_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: FileCreate,
) -> Optional[Union[Any, FileFull, HTTPValidationError]]:
    """Update File Info

     Получает информацию о файле

    Args:
        file_uuid (UUID):
        body (FileCreate): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FileFull, HTTPValidationError]
    """

    return sync_detailed(
        file_uuid=file_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    file_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: FileCreate,
) -> Response[Union[Any, FileFull, HTTPValidationError]]:
    """Update File Info

     Получает информацию о файле

    Args:
        file_uuid (UUID):
        body (FileCreate): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FileFull, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_uuid=file_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: FileCreate,
) -> Optional[Union[Any, FileFull, HTTPValidationError]]:
    """Update File Info

     Получает информацию о файле

    Args:
        file_uuid (UUID):
        body (FileCreate): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FileFull, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            file_uuid=file_uuid,
            client=client,
            body=body,
        )
    ).parsed

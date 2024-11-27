from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_full import MeetingFull
from ...models.meeting_update_validated import MeetingUpdateValidated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    meeting_id: int,
    *,
    body: MeetingUpdateValidated,
    force: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/meetings/virtuals/{meeting_id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, MeetingFull]]:
    if response.status_code == 200:
        response_200 = MeetingFull.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, MeetingFull]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    meeting_id: int,
    *,
    client: AuthenticatedClient,
    body: MeetingUpdateValidated,
    force: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, MeetingFull]]:
    """Update Virtual Meeting

    Args:
        meeting_id (int):
        force (Union[Unset, bool]): Флаг, позволяющий создавать ВКС, в обход оффлайн событий на
            площадке Default: False.
        body (MeetingUpdateValidated): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingFull]]
    """

    kwargs = _get_kwargs(
        meeting_id=meeting_id,
        body=body,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    meeting_id: int,
    *,
    client: AuthenticatedClient,
    body: MeetingUpdateValidated,
    force: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, MeetingFull]]:
    """Update Virtual Meeting

    Args:
        meeting_id (int):
        force (Union[Unset, bool]): Флаг, позволяющий создавать ВКС, в обход оффлайн событий на
            площадке Default: False.
        body (MeetingUpdateValidated): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingFull]
    """

    return sync_detailed(
        meeting_id=meeting_id,
        client=client,
        body=body,
        force=force,
    ).parsed


async def asyncio_detailed(
    meeting_id: int,
    *,
    client: AuthenticatedClient,
    body: MeetingUpdateValidated,
    force: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, MeetingFull]]:
    """Update Virtual Meeting

    Args:
        meeting_id (int):
        force (Union[Unset, bool]): Флаг, позволяющий создавать ВКС, в обход оффлайн событий на
            площадке Default: False.
        body (MeetingUpdateValidated): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingFull]]
    """

    kwargs = _get_kwargs(
        meeting_id=meeting_id,
        body=body,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    meeting_id: int,
    *,
    client: AuthenticatedClient,
    body: MeetingUpdateValidated,
    force: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, MeetingFull]]:
    """Update Virtual Meeting

    Args:
        meeting_id (int):
        force (Union[Unset, bool]): Флаг, позволяющий создавать ВКС, в обход оффлайн событий на
            площадке Default: False.
        body (MeetingUpdateValidated): Промежуточная модель pydantic'а для унифицирования конфигов
            и удобного администрирования

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingFull]
    """

    return (
        await asyncio_detailed(
            meeting_id=meeting_id,
            client=client,
            body=body,
            force=force,
        )
    ).parsed

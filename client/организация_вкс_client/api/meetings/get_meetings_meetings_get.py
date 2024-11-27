import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_backend import MeetingBackend
from ...models.meeting_list import MeetingList
from ...models.meeting_sorting_fields import MeetingSortingFields
from ...models.meeting_states import MeetingStates
from ...models.user_priority import UserPriority
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
    filter_: Union[Unset, str] = UNSET,
    priority: Union[Unset, UserPriority] = UNSET,
    building_id: Union[Unset, int] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    backend: Union[Unset, MeetingBackend] = UNSET,
    user_participant: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, MeetingSortingFields] = MeetingSortingFields.ID,
    state: Union[Unset, List[MeetingStates]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_datetime = from_datetime.isoformat()
    params["fromDatetime"] = json_from_datetime

    json_to_datetime = to_datetime.isoformat()
    params["toDatetime"] = json_to_datetime

    params["filter"] = filter_

    json_priority: Union[Unset, int] = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

    params["buildingId"] = building_id

    params["roomId"] = room_id

    params["page"] = page

    params["rowsPerPage"] = rows_per_page

    params["departmentId"] = department_id

    params["userId"] = user_id

    json_backend: Union[Unset, str] = UNSET
    if not isinstance(backend, Unset):
        json_backend = backend.value

    params["backend"] = json_backend

    params["userParticipant"] = user_participant

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_state: Union[Unset, List[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/meetings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, MeetingList]]:
    if response.status_code == 200:
        response_200 = MeetingList.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, MeetingList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
    filter_: Union[Unset, str] = UNSET,
    priority: Union[Unset, UserPriority] = UNSET,
    building_id: Union[Unset, int] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    backend: Union[Unset, MeetingBackend] = UNSET,
    user_participant: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, MeetingSortingFields] = MeetingSortingFields.ID,
    state: Union[Unset, List[MeetingStates]] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MeetingList]]:
    """Get Meetings

     Получение всех ВКС, доступных в системе, а также виртуальных ВКС на заданный период

    Args:
        from_datetime (datetime.datetime):
        to_datetime (datetime.datetime):
        filter_ (Union[Unset, str]): Поиск совпадений в имени или описании
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность
            резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся
            сеанс будет отменён)
        building_id (Union[Unset, int]): Идентификатор здания, в которой проводится ВКС
        room_id (Union[Unset, int]): Идентификатор комнаты в которой проводится ВКС
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):
        department_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        user_participant (Union[Unset, int]): Идентификатор пользователя, который является
            участником ВКС
        sort_by (Union[Unset, MeetingSortingFields]): An enumeration. Default:
            MeetingSortingFields.ID.
        state (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingList]]
    """

    kwargs = _get_kwargs(
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        filter_=filter_,
        priority=priority,
        building_id=building_id,
        room_id=room_id,
        page=page,
        rows_per_page=rows_per_page,
        department_id=department_id,
        user_id=user_id,
        backend=backend,
        user_participant=user_participant,
        sort_by=sort_by,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
    filter_: Union[Unset, str] = UNSET,
    priority: Union[Unset, UserPriority] = UNSET,
    building_id: Union[Unset, int] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    backend: Union[Unset, MeetingBackend] = UNSET,
    user_participant: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, MeetingSortingFields] = MeetingSortingFields.ID,
    state: Union[Unset, List[MeetingStates]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MeetingList]]:
    """Get Meetings

     Получение всех ВКС, доступных в системе, а также виртуальных ВКС на заданный период

    Args:
        from_datetime (datetime.datetime):
        to_datetime (datetime.datetime):
        filter_ (Union[Unset, str]): Поиск совпадений в имени или описании
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность
            резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся
            сеанс будет отменён)
        building_id (Union[Unset, int]): Идентификатор здания, в которой проводится ВКС
        room_id (Union[Unset, int]): Идентификатор комнаты в которой проводится ВКС
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):
        department_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        user_participant (Union[Unset, int]): Идентификатор пользователя, который является
            участником ВКС
        sort_by (Union[Unset, MeetingSortingFields]): An enumeration. Default:
            MeetingSortingFields.ID.
        state (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingList]
    """

    return sync_detailed(
        client=client,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        filter_=filter_,
        priority=priority,
        building_id=building_id,
        room_id=room_id,
        page=page,
        rows_per_page=rows_per_page,
        department_id=department_id,
        user_id=user_id,
        backend=backend,
        user_participant=user_participant,
        sort_by=sort_by,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
    filter_: Union[Unset, str] = UNSET,
    priority: Union[Unset, UserPriority] = UNSET,
    building_id: Union[Unset, int] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    backend: Union[Unset, MeetingBackend] = UNSET,
    user_participant: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, MeetingSortingFields] = MeetingSortingFields.ID,
    state: Union[Unset, List[MeetingStates]] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MeetingList]]:
    """Get Meetings

     Получение всех ВКС, доступных в системе, а также виртуальных ВКС на заданный период

    Args:
        from_datetime (datetime.datetime):
        to_datetime (datetime.datetime):
        filter_ (Union[Unset, str]): Поиск совпадений в имени или описании
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность
            резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся
            сеанс будет отменён)
        building_id (Union[Unset, int]): Идентификатор здания, в которой проводится ВКС
        room_id (Union[Unset, int]): Идентификатор комнаты в которой проводится ВКС
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):
        department_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        user_participant (Union[Unset, int]): Идентификатор пользователя, который является
            участником ВКС
        sort_by (Union[Unset, MeetingSortingFields]): An enumeration. Default:
            MeetingSortingFields.ID.
        state (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingList]]
    """

    kwargs = _get_kwargs(
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        filter_=filter_,
        priority=priority,
        building_id=building_id,
        room_id=room_id,
        page=page,
        rows_per_page=rows_per_page,
        department_id=department_id,
        user_id=user_id,
        backend=backend,
        user_participant=user_participant,
        sort_by=sort_by,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
    filter_: Union[Unset, str] = UNSET,
    priority: Union[Unset, UserPriority] = UNSET,
    building_id: Union[Unset, int] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = UNSET,
    department_id: Union[Unset, int] = UNSET,
    user_id: Union[Unset, int] = UNSET,
    backend: Union[Unset, MeetingBackend] = UNSET,
    user_participant: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, MeetingSortingFields] = MeetingSortingFields.ID,
    state: Union[Unset, List[MeetingStates]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MeetingList]]:
    """Get Meetings

     Получение всех ВКС, доступных в системе, а также виртуальных ВКС на заданный период

    Args:
        from_datetime (datetime.datetime):
        to_datetime (datetime.datetime):
        filter_ (Union[Unset, str]): Поиск совпадений в имени или описании
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность
            резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся
            сеанс будет отменён)
        building_id (Union[Unset, int]): Идентификатор здания, в которой проводится ВКС
        room_id (Union[Unset, int]): Идентификатор комнаты в которой проводится ВКС
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):
        department_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        user_participant (Union[Unset, int]): Идентификатор пользователя, который является
            участником ВКС
        sort_by (Union[Unset, MeetingSortingFields]): An enumeration. Default:
            MeetingSortingFields.ID.
        state (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingList]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            filter_=filter_,
            priority=priority,
            building_id=building_id,
            room_id=room_id,
            page=page,
            rows_per_page=rows_per_page,
            department_id=department_id,
            user_id=user_id,
            backend=backend,
            user_participant=user_participant,
            sort_by=sort_by,
            state=state,
        )
    ).parsed

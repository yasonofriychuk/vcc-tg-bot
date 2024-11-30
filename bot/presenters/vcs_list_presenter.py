from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from client.models import MeetingBare
from presenters.date import present_date, format_duration
from services.auth import TokenData


def present_vcc_msg(
        page: int,
        total: int,
        meeting: MeetingBare,
        meeting_more: dict,
) -> str:
    msg_parts = [
        f"Встреча <i>{page}</i> из {total}.",
        "",
        f"<u>Название:</u> {meeting.name}",
        f"<u>Дата и время:</u> {present_date(meeting.started_at, meeting.ended_at)}",
        f"<u>Продолжительность:</u> {format_duration(meeting.duration) if meeting.duration else 'Не указана'}",
        f"<u>Платформа:</u> {meeting_more.get('backend', 'Внешняя платформа')}",
        ""
    ]

    participant_list = []
    for participant in meeting_more.get('participants', []):
        full_name = " ".join(filter(lambda i: i, [
            participant.get('lastName'),
            participant.get('firstName'),
            participant.get('middleName'),
        ]))

        approved_text = "✅" if participant.get("isApproved") else "❌"
        participant_text = f"{full_name} {approved_text}"
        if "email" in participant:
            participant_text = f"<a href='mailto:{participant.get('email')}'>{full_name}</a> {approved_text}"

        participant_list.append(participant_text)

    if participant_list:
        msg_parts.append(f"<u>Участники:</u>")
        msg_parts.extend(participant_list)

    return "\n".join(msg_parts)


def need_ics(token: TokenData, meeting_more: dict) -> bool:
    for participant in meeting_more.get('participants', []):
        if participant.get("id", -1) == token.user.id:
            return True

    if meeting_more.get("createdUser", {}).get("id", -1) == token.user.id:
        return True

    if meeting_more.get("organizedUser", {}).get("id", -1) == token.user.id:
        return True


def present_vcc_buttons(
        key: str,
        token: TokenData,
        page: int,
        total: int,
        meeting: MeetingBare,
        meeting_more: dict,
) -> InlineKeyboardMarkup:
    buttons_row_1 = []
    if need_ics(token, meeting_more):
        buttons_row_1.append(InlineKeyboardButton(text="Добавить в календарь", callback_data=f"get_ics:{meeting.id}"))

    if "organizerPermalink" in meeting_more:
        buttons_row_1.append(InlineKeyboardButton(text="Ссылка", url=meeting_more.get("organizerPermalink")))
    elif "permalink" in meeting_more:
        buttons_row_1.append(InlineKeyboardButton(text="Ссылка", url=meeting_more.get("permalink")))

    buttons_row_2 = []
    if page > 1:
        buttons_row_2.append(InlineKeyboardButton(text="⬅️", callback_data=f"show_meet:{page - 1}:{key}"))

    if page < total:
        buttons_row_2.append(InlineKeyboardButton(text="➡️", callback_data=f"show_meet:{page + 1}:{key}"))

    return InlineKeyboardMarkup(inline_keyboard=[
        buttons_row_1,
        buttons_row_2
    ])

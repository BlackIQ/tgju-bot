# Libs
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update  # Telegram
from telegram.ext import ContextTypes  # Telegram
import requests  # Requests

# Application
from core.settings import settings  # Settings
from data.flags import flags  # Data


def attach_flag(value: str) -> str:
    code = value.split("_")[1].upper()
    flag = flags.get(code)

    return flag or "🏳️"


# Currency
async def currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(text="🏡 بازگشت به خانه", callback_data="home"),
        ]
    ]

    response = requests.get(
        f"{settings.base_url}/price/currency",
        headers={
            "X-Request-ID": "TGJU_BOT",
        },
    )

    if not response.ok:
        message = "متاسفانه عملات انجام نشد و نتونستم قیمت‌ها رو برات بیارم..."

        reply_markup = InlineKeyboardMarkup(keyboard)

        return await query.edit_message_text(text=message, reply_markup=reply_markup)

    currencies = response.json()

    messages: list[str] = []

    for currency in currencies:
        messages.append(
            f"{attach_flag(currency["key"])} {currency["title"]}: {currency["price"]}"
        )

    message = "\n".join(messages)

    reply_markup = InlineKeyboardMarkup(keyboard)

    return await query.edit_message_text(text=message, reply_markup=reply_markup)

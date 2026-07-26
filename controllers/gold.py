# Telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Requests
import requests

# Application
from core.settings import settings  # Settings


# Gold
async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(text="🏡 بازگشت به خانه", callback_data="home"),
        ]
    ]

    response = requests.get(f"{settings.base_url}/price/gold")

    if not response.ok:
        message = "متاسفانه عملات انجام نشد و نتونستم قیمت‌ها رو برات بیارم..."

        reply_markup = InlineKeyboardMarkup(keyboard)

        return await query.edit_message_text(text=message, reply_markup=reply_markup)

    golds = response.json()

    messages: list[str] = []

    for index, gold_category in enumerate(golds):
        messages.append(gold_category["title"])

        for gold in gold_category["prices"]:
            messages.append(f"{gold["title"]}: {gold["price"]}")
            
        if index != len(golds):
            messages.append("")

    message = "\n".join(messages)

    reply_markup = InlineKeyboardMarkup(keyboard)

    return await query.edit_message_text(text=message, reply_markup=reply_markup)

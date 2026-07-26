# Telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


# Home
async def home(update: Update, context: ContextTypes.DEFAULT_TYPE, start: bool):
    message = "\n".join(
        [
            "🚀 به ربات قیمت لحظه ای خوش اومدی!",
            "",
            "با این ربات میتونی هر لحظه ای که بخوای قیمت طلا و دلار رو دریافت کنی!",
            "",
            "برای شروع، یکی از گزینه‌های زیر رو انتخاب کن 👇",
        ]
    )

    keyboard = [
        [
            InlineKeyboardButton(text="🥇 قیمت طلا", callback_data="gold"),
            InlineKeyboardButton(text="💸 قیمت ارز", callback_data="currency"),
        ],
        [
            InlineKeyboardButton(text="درباره ما", callback_data="about"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if start:
        return await update.message.reply_text(text=message, reply_markup=reply_markup)
    else:
        query = update.callback_query
        await query.answer()

        return await query.edit_message_text(text=message, reply_markup=reply_markup)

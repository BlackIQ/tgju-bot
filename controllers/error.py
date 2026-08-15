# Libs
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update  # Telegram
from telegram.ext import ContextTypes  # Telegram


# Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    message = "متاسفانه درخواست عجیب غریبی دادی و من نتونستم درک کنم! شایدم درست بوده و من هنگ کردم... آخه با این قیمتا آدم واقعا رد میده!"

    keyboard = [
        [
            InlineKeyboardButton(text="🏡 بازگشت به خانه", callback_data="home"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return await query.edit_message_text(text=message, reply_markup=reply_markup)

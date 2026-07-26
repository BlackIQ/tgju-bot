# Telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


# About
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    message = "\n".join(
        [
            "این بات یک پروژه اوپن سورس میباشد که توسط امیرحسین محمدی نوشته شده است.",
            "",
            "https://github.com/BlackIQ/tgju-bot",
            "",
            "",
            "همچنین این بات از یک API استفاده میکند که توسط شخص سازنده این بات ساخته شده است.",
            "",
            "https://github.com/BlackIQ/tgju-bot",
            "",
            "",
            "ارتباط با توسعه دهنده: hi@amirhossin.info",
            "",
            "",
            "Made with ❤️ bu amirhossein.ino",
        ]
    )

    keyboard = [
        [
            InlineKeyboardButton(text="🏡 بازگشت به خانه", callback_data="home"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return await query.edit_message_text(text=message, reply_markup=reply_markup)

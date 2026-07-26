# Telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Application
from core.settings import settings  # Settings
from controllers.home import home  # Home Controller
from controllers.about import about  # About Controller
from controllers.currency import currency  # Currency Controller
from controllers.gold import gold  # Gold Controller
from controllers.error import error  # Error Controller


# Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await home(update, context, True)


# Query Router
async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    match query.data:
        case "home":
            await home(update, context, False)
        case "about":
            await about(update, context)
        case "currency":
            await currency(update, context)
        case "gold":
            await gold(update, context)
        case _:
            await error(update, context)


# App
def app() -> None:
    # Build BOT
    bot = Application.builder().token(settings.bot_token).build()

    # Handler
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CallbackQueryHandler(query_handler))

    # Run BOT
    bot.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    app()

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not found. Please set it in Railway variables.")

MAX_REACTIONS = 40
EMOJI_LIST = ["🔥","❤️","👍","⚡","💎","🚀","😍","👏","👿","😎"]

async def on_startup(app):
    print("Hello Alone Bot is Active 🔥")

async def add_reactions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post or update.message
    total = 0

    while total < MAX_REACTIONS:
        await asyncio.sleep(120)

        for _ in range(2):
            if total >= MAX_REACTIONS:
                return
            try:
                await context.bot.set_message_reaction(
                    chat_id=message.chat_id,
                    message_id=message.message_id,
                    reaction=[EMOJI_LIST[total % len(EMOJI_LIST)]]
                )
                total += 1
            except Exception as e:
                print(e)

app = ApplicationBuilder().token(TOKEN).post_init(on_startup).build()

app.add_handler(MessageHandler(filters.ALL, add_reactions))

app.run_polling()
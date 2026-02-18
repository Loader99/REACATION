import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

MAX_REACTIONS = 40
EMOJI_LIST = ["🔥","❤️","👍","⚡","💎","🚀","😍","👏","👿","😎"]

async def on_startup(app):
    print("Hello Alone Bot is Active 🔥")

async def add_reactions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post or update.message
    total = 0

    while total < MAX_REACTIONS:
        await asyncio.sleep(120)  # 2 minute delay

        for _ in range(2):  # 2 reactions every 2 minutes
            if total >= MAX_REACTIONS:
                return
            try:
                await context.bot.set_message_reaction(
                    chat_id=message.chat_id,
                    message_id=message.message_id,
                    reaction=[EMOJI_LIST[total % len(EMOJI_LIST)]]
                )
                total += 1
            except:
                pass

app = ApplicationBuilder().token(TOKEN).post_init(on_startup).build()

app.add_handler(MessageHandler(filters.ALL, add_reactions))

app.run_polling()
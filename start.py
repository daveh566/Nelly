from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_START = """
Hello, I am Nelly , An Intelligent ChatBot by @KayAspirerProjecr. If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@bot.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    )
    buttons.add(
        InlineKeyboardButton(
            "👸🏼 Add Nelly to your group",
            url=f"https://telegram.me/nellyvbot?startgroup=true",
        await bot.send_message(chat_id = message.chat.id, text = BOT_START, reply_markup = InlineKeyboardMarkup(buttons))

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton

BOT_START = """
Hello, I am Nelly [リュキア], An Intelligent ChatBot. If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Lycia", switch_inline_query_current_chat="lycia "), InlineKeyboardButton("Github", url = "https://github.com/Red-Aura/Lyciachatbot")]
              ]
    await BOT.send_message(chat_id = message.chat.id, text = BOT_START, reply_markup = InlineKeyboardMarkup(buttons))

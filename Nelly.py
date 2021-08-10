print("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")
import re
from asyncio import (gather, get_event_loop, sleep)

from aiohttp import ClientSession
from pyrogram import filters
from Python_ARQ import ARQ

from config import bot, BOT_TOKEN, ARQ_API_KEY, ARQ_API_BASE_URL, LANGUAGE
bot_token= BOT_TOKEN

print("[INFO]: Checking... Your Details")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: Code running by master Prince Op")
arq = None


async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Luna", "Nelly")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Nelly")
    else:
        responsess = responsee
    if "Who is Tiana?" in responsess:
        responsess2 = responsess.replace("Who is Nelly?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def bot(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        aspirer = msg
        aspirer = aspirer.replace("Nelly", "Aco")
        aspirer = aspirer.replace("Nelly", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Nelly")
        result = result.replace("Eliza", "@NellyVBot")
        result = result.replace("Hi~", "Hello Friend I Am @NellyVbot")
        result = result.replace("My dear great botmaster, @KayAspirerProject Nellybot Team.", "I was created by @Techno_Ocean Team")
        result = result.replace("Have the control right.", "My Father Is @madepranav")
        result = result.replace("I was created by @KayAspirerProject Team.", "I was created by @Techno_Ocean Team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        try:
            await bot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            lan = translator.detect(rm)
        aspirer = rm
        if not "en" in lan and not lan == "":
            aspirer = translator.translate(aspirer, lang_tgt="en")

        aspirer = aspirer.replace("Nelly", "Aco")
        aspirer = aspirer.replace("Nelly", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {aspirer},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Nelly")
        result = result.replace("Eliza", "@NellyVBot")
        result = result.replace("Hi~", "Hello Friend I Am @NellyVBot")
        result = result.replace("My dear great botmaster, @KayAspirerProject Nellybot Team.", "Made By @madepranav")
        result = result.replace("Have the control right.", "My Father Is @madepranav")
        result = result.replace("I was created by Nellybot Team.", "I was created by @Techno_Ocean Team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(red, lang_tgt=lan[0])
        try:
            await LYCIA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)



@bot.on_message(filters.text & filters.private & ~filters.reply & ~filters.bot)
async def bot(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aura = rm
    if not "en" in lan and not lan == "":
        aspirer = translator.translate(aspirer, lang_tgt="en")

   
    aspirer = aspirer.replace("Nelly", "Aco")
    aspirer = aspirer.replace("Nelly", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aspirer},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Nelly")
    result = result.replace("Eliza", "@NellyVBot")
    result = result.replace("Hi~", "Hello Friend I Am @NellyVBot")
    result = result.replace("My dear great botmaster, @KayAspirerProject Nellybot Team.", "Made By @madepranav")
    result = result.replace("Have the control right.", "My Father Is @madepranav")
    result = result.replace("I was created by Nellybot Team.", "I was created by @Techno_Ocean Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    been = result
    if not "en" in lan and not lan == "":
        been = translator.translate(been, lang_tgt=lan[0])
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(been)
    except CFError as e:
        print(e)


@LYCIA.on_message(
    filters.regex("Nelly|nelly|NELLY")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
)
async def aspirerbeen(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aspirer = rm
    if not "en" in lan and not lan == "":
        aspirer = translator.translate(aspirer, lang_tgt="en")


    aspirer = aspirer.replace("Nelly", "Aco")
    aspirer = aspirer.replace("Nelly", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aspirer},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Nelly")
    result = result.replace("Eliza", "@NellyVBot")
    result = result.replace("Hi~", "Hello Friend I Am @NellyVBot")
    result = result.replace("My dear great botmaster, @KayAspirerProject Nellybot Team.", "Made By @madepranav")
    result = result.replace("Have the control right.", "My Father Is @madepranav")
    result = result.replace("I was created by Nellybot Team.", "I was created by @Techno_Ocean Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        been = translator.translate(been, lang_tgt=lan[0])
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(been)
    except CFError as e:
        print(e)
        
       

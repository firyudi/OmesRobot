import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot

yinzver = "2.0.22"
PHOTO = "https://te.legra.ph/file/b79197c46db56a987571d.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm OMESROBOT.** \n\n"
  TEXT += "✨ **I'm Working Properly** \n\n"
  TEXT += f"✨ **Oᴡɴᴇʀ : [𝙼𝙰𝙽𝙳𝙾𝚁](https://t.me/omesnakal)** \n\n"
  TEXT += f"✨ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ    :** `{telever}` \n\n"
  TEXT += f"✨ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ   :** `{tlhver}` \n\n"
  TEXT += f"✨ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += f"✨ **Omes Vᴇʀsɪᴏɴ :** `{yinzver}` \n\n"
  TEXT += "**🔥 Thanks For Adding Me Here 🔥**"
  BUTTON = [[Button.url("Help", "https://t.me/Assistenomesrobot?start=help"), Button.url("✨ sᴜᴩᴩᴏʀᴛ ✨", "https://t.me/NewEraID")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

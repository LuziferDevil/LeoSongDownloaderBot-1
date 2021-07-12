# Leo Projects <https://t.me/leosupportx>
# @Naviya2 🇱🇰

import os
import time
import psutil
import shutil
import string
import asyncio
import config
from asyncio import TimeoutError
from helper.database.access_db import db
from helper.broadcast import broadcast_handler
from helper.database.add_user import AddUserToDatabase
from helper.display_progress import humanbytes
from pyrogram import Client
from helper.forcesub import ForceSub
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from LeoSongDownloaderBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from LeoSongDownloaderBot import LeoSongDownloaderBot as app
from LeoSongDownloaderBot import LOGGER

pm_start_text = """
Hello [{}](tg://user?id={}) 👋

I'm Leo Song Downloader Bot 🇱🇰

You can download any song within a shortime with this Bot 🙂

If you want to know how to use this bot just
touch on this command " /help " 🙂

Leo Projects 🇱🇰
"""

help_text = """
You should know the following commands to use this bot 🙂

⭕️ /song <song name>: Download songs from all sources 😏

⭕️ Send youtube url to me directly i can download it to your telegram database in audio format 🙂


Made By : @naviya2 🇱🇰
Support Group : @leosuppportx 🇱🇰
Updates Channel : @new_ehi 🇱🇰
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         text="Updates Channel🗣", url="https://t.me/new_ehi"
                    ),
                    InlineKeyboardButton(
                        text="Support Group👥", url="https://t.me/leosupportx"
                    ),
                ],
                    
                [
                    InlineKeyboardButton(
                        text="Developer🧑‍💻", url="https://t.me/naviya2"
                    ),
                    InlineKeyboardButton(
                        text="Rate us ★", url="https://t.me/tlgrmcbot?start=leosongdownloaderbot-review"
                    ),     
                ],
                
                [
                    InlineKeyboardButton(
                        text="➕ Add me to your group ➕", url="t.me/leosongdownloaderbot?startgroup=true"
                    ),
                ],
            ],
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await AddUserToDatabase(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    await message.reply(help_text)

@app.on_message(filters.private & filters.command("broadcast") & filters.user(config.BOT_OWNER) & filters.reply)
async def _broadcast(client, message):
    await broadcast_handler(event)


@app.on_message(filters.private & filters.command("status") & filters.user(config.BOT_OWNER))
async def show_status_count(client, message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await event.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`\n\n@leosongdownloaderbot 🇱🇰",
        parse_mode="Markdown",
        quote=True
    )

app.start()
LOGGER.info("LeoSongDownloaderBot is online.")
idle()

import os
from LeoSongDownloaderBot.translation import Translation
import config
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_callback_query()
async def button(client, message):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)
    elif message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention),
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await message.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "info":
        await message.message.edit_text(
            text=Translation.INFO_TEXT.format(username=message.from_user.username, first_name=message.from_user.first_name, last_name=message.from_user.last_name, user_id=message.from_user.id, mention=message.from_user.mention),
            reply_markup=Translation.INFO_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await message.message.delete()

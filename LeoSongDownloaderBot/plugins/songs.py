# Plugin by @Naviya2
# Leo Projects <https://t.me/new_ehi>

import os
import requests
import aiohttp
import youtube_dl
from LeoSongDownloaderBot import LeoSongDownloaderBot as app
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@app.on_message(filters.command('song'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    shed = message.reply('🔎 I am Searching Your Song Please Wait ...\n@leosongdownloaderbot 🇱🇰')
    ydl_opts =  {
       "format": "bestaudio[ext=m4a]",
       "geo-bypass": True,
       "nocheckcertificate": True,
       "outtmpl": "downloads/%(id)s.%(ext)s",
       }
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        channel = results[0]["channel"]
    except Exception as e:
        shed.edit(
            "❌ Nothing Found {}☹️\n\nPlease spell it properly😊".format(message.from_user.mention)
        )
        print(str(e))
        return
    shed.edit("Now I am Downloading Your Song 😊\n\n@leosongdownloaderbot 🇱🇰")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = 'Downloaded By : @leosongdownloaderbot 🇱🇰'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur, performer=str(yt.author))
        shed.delete()
    except Exception as e:
        shed.edit('An error occured {} ☹️ please ask in our [Support Group](https://t.me/leosupportx)'.format(message.from_user.mention))
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

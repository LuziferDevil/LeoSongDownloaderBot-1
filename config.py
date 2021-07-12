# Leo Projects <https://t.me/leosupportx>

import os
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoSongDownloaderBot")
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
MONGODB_URI = os.environ.get("MONGODB_URI", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

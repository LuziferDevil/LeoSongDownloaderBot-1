# Leo Projects <https://t.me/leosupportx>

import os
API_ID = int(os.getenv("API_ID", 2158704))
API_HASH = os.getenv("API_HASH", "227f3bd8c1d7fc3ecfa243e1a85dd2fa")
BOT_TOKEN = os.getenv("BOT_TOKEN", "1745816793:AAGzEcqMoAwUOyYznx4qGQjAcLixNliSO-A")
UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL", -1001231683570))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "testleonvibot")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoSongDownloaderBot")
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001560862542))
ARQ_API_KEY = os.getenv("ARQ_API_KEY", None)

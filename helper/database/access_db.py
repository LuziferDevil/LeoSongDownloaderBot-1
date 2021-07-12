import config
from helper.database.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)

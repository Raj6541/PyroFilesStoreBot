# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("8179798", "0"))
	API_HASH = os.environ.get("78a1bfb49887007ad2760a2394b063c4")
	BOT_TOKEN = os.environ.get("1728493515:AAH2KFi_G9-s2Pv3qMT7PJoGLxD9zL9eKMM")
	BOT_USERNAME = os.environ.get("RDX_HQ_MOVIES_BOT")
	DB_CHANNEL = int(os.environ.get("-1001536870740", "-100"))
	BOT_OWNER = int(os.environ.get("901527936", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("-1001443287481")
	LOG_CHANNEL = os.environ.get("-1001536870740", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Jai_Hanuman_bot

👥 **Support Group:** [Linux Repositories](https://t.me/rdxhqmovies)

📢 **Updates Channel:** [Discovery Projects](https://t.me/rdxhqmovies)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @jai_hanumanbot

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.t.me/jai_hanumanbot) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""

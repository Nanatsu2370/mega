# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [Safone](https://t.me/ImSafone)

👥 **Support Group:** [AsmSupport](https://t.me/AsmSupport)

"""

  HELP_USER = """


Este bot puede descargar archivos y videos de Mega Links y subirlos a Telegram. Simplemente envíe cualquier enlace de Mega.nz y vea la magia. También puede agregar o cambiar el subtítulo: simplemente seleccione un archivo / video cargado o reenvíeme cualquier archivo de Telegram y luego escriba el texto que desea que esté subtitulado en el archivo como respuesta a ese archivo y el texto que escribió se adjuntará como subtítulo 😁!
"
"""

  START_TEXT = """
👋🏻 **Hola** {user_mention},

Soy **{bot_name}**
Puedo descargar archivos y videos de Mega.nz Links y subirlos a Telegram. ¡Consulte la ayuda para obtener más información 😉! 
**Maintained By: {bot_owner}**❤️!
"""

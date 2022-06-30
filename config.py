from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = "5439555827:AAElCvsZouahPVKrMuEU1_qNox587CY-HNQ"
API_ID = "3188376"
API_HASH = "4c187a62bc008363b48f7aa3ed38e56b"
API_ID1 = int(environ.get("API_ID1"))
API_HASH1 = environ.get("API_HASH1")
SUDO_USERS_ID = environ.get("SUDO_USERS_ID")
LOG_GROUP_ID = "-1001174927319"
BASE_DB = environ.get("BASE_DB")
MONGO_URL = "mongodb+srv://Athenabetta:Athenabetta@cluster0.gsgt15j.mongodb.net/?retryWrites=true&w=majority"
ARQ_API_URL = environ.get("ARQ_API_URL")
ARQ_API_KEY = "VIXRLF-UTDWJU-LMTAIW-FMHCLU-ARQ"
COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES")
F_SUB_CHANNEL = "Tamilcoders"

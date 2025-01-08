from os import getenv

from dotenv import load_dotenv
from pyrogram import filters



API_ID = int(getenv("API_ID", "22926746"))
API_HASH = getenv("API_HASH", "ffd91926f59e55fb08b3e1a4f5b99b1d")
BOT_TOKEN = getenv("BOT_TOKEN", "5624068661:AAEXObnqRAujlX74hsjZWR2xXhx11Syh2ZM")
STRING_SESSION = getenv("STRING_SESSION", "BQFd1ZoABI7htcsZ22dLCbd7BFglPFCyT5JAbF9nxGwkV-DR3hs_sOe1QOGAtGfEaPY0BMitePR1RnW2b2_uzWFGteR15iHtz4gQoFEHKmg99tidegZ_0lQ8u9iW-sePaB-2LQ1eLMo4smN0GYPvx7Y4i03T1xbiQ_UfMbULHbWTl7eXi65l1uY2voYFLL9B64c8aZQein7vVIQqjF3IysjFLLiVzvc4G4Fde0Ja0zT5Q_RTn-X5MUdB0i_YVwFh79ZCWvRNYZBIO1kIgEsVF9qZ4vRABwaZK8eT7NDhApHXUbfWIis3e05pgiw5xd9Huqyp7LsuK1O43N68y9o8dDRmK42iQwAAAAHS5JCGAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "7758957839"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002488687891"))
START_IMAGE_URL = getenv("START_IMAGE_URL", "https://telegra.ph/file/a62273c43c95ad07ada61.jpg")
STATS_IMAGE_URL = getenv("STATS_IMAGE_URL", "https://graph.org//file/99a8a9c13bb01f9ac7d98.png")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

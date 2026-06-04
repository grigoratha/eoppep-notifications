import os

from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

TO_EMAILS = os.getenv("TO_EMAILS", "").split(",")

ARCHIVE_FILE = "archive.json"

URL = "https://eoppep.gr/index.php/el/pistopoiiseis-eksetaseis/apofoitoi-saek/anakoinoseis-exetaseon-pistopoiisis-saek"
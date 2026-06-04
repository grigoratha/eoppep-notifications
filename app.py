from logger import *

from config import *
from api import fetch_announcements
from archive import load_archive, update_archive
from email_service import send_email

def main():
    logger.info("Fetching announcements...")

    data = fetch_announcements()

    archive = load_archive(ARCHIVE_FILE)

    updated_archive = set(archive)

    new_items = []

    for item in data:
        uid = item["url"]

        if uid not in updated_archive:

            new_items.append({
                "title": item["title"],
                "url": item["url"]
            })

            updated_archive.add(uid)

    update_archive(ARCHIVE_FILE, updated_archive)

    if new_items:
        send_email(subject="Νέες Ανακοινώσεις ΕΟΠΠΕΠ", items=new_items)
        logger.info(f"Found {len(new_items)} new announcements, e-mail was sent")

    else:
        logger.info("No new announcements found")

if __name__ == "__main__":
    main()
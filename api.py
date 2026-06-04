import requests

from config import URL
from logger import logger
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def fetch_announcements():
    logger.info("Fetching announcements from {}", URL)

    try:
        response = requests.get(
            URL,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30,
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logger.exception("Failed to fetch announcements: {}", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    announcements = []

    for item in soup.select("#tm-main .el-item"):
        title_link = item.select_one(".el-title a")

        if not title_link:
            continue

        title = title_link.get_text(strip=True)
        href = urljoin(URL, title_link.get("href"))

        announcements.append({
            "title": title,
            "url": href,
        })

    logger.info("Fetched {} announcements", len(announcements))

    return announcements
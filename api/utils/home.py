from .parsing import Parsing
from urllib.parse import urlparse
import re
import logging
from typing import Dict, List, Optional, Any, Union
from bs4 import BeautifulSoup, Tag

# Configure logging
logger = logging.getLogger(__name__)


class Home(Parsing):
    def __init__(self, page: int = 1) -> None:
        super().__init__()
        self.__page: int = page
        logger.info(f"Initialized Home scraper for page: {page}")

    def __get_card(self, item: Tag) -> Optional[Dict[str, Union[str, int, None]]]:
        """Extract card information from a home page item."""
        try:
            # Ambil judul dari teks atau atribut
            title_tag = item.find("h2") or item.find("h3") or item.find("a")
            title = title_tag.text.strip() if title_tag else "Unknown Title"
            if title_tag and title_tag.get("title"):
                title = title_tag.get("title").strip()

            # Extract type
            type_div = item.find("div", {"class": "typez"}) or item.find("span", {"class": "type"})
            anime_type = type_div.text.strip() if type_div else "Donghua"

            # Extract episode count
            eps_span = item.find("span", {"class": "epx"}) or item.find("div", {"class": "epz"})
            eps = None
            if eps_span:
                eps_text = eps_span.text.strip()
                eps_numbers = re.sub("[^0-9]", "", eps_text)
                eps = int(eps_numbers) if eps_numbers else None

            # Extract thumbnail
            thumbnail_img = item.find("img", {"src": True})
            thumbnail = ""
            if thumbnail_img:
                thumbnail = (
                    thumbnail_img.get("data-lazy-src") or thumbnail_img.get("data-src") or thumbnail_img.get("src") or ""
                )

            # Extract URL and slug
            url_link = item if item.name == "a" else item.find("a", {"href": True})
            if not url_link or not url_link.get("href"):
                return None

            url = url_link.get("href")
            slug_path = urlparse(url).path
            slug = (
                slug_path.split("/")[-2]
                if slug_path.endswith("/")
                else slug_path.split("/")[-1]
            )

            card_data = {
                "title": title,
                "type": anime_type,
                "headline": title,
                "eps": eps,
                "thumbnail": thumbnail,
                "slug": slug,
                "url": url
            }
            return card_data
        except Exception as e:
            logger.error(f"Error extracting card data: {e}")
            return None

    def __get_home(
        self, data: BeautifulSoup
    ) -> Dict[str, Union[List[Dict[str, Any]], int, str]]:
        """Extract home page content from the data."""
        cards = []
        try:
            # Ambil semua elemen kartu anime/donghua langsung dari situs
            box_items = data.find_all("div", {"class": "bs"})
            if not box_items:
                box_items = data.find_all("article")

            logger.info(f"Found {len(box_items)} raw items in home page")
            section_items = []

            for item in box_items:
                card = self.__get_card(item)
                if card:
                    section_items.append(card)

            if section_items:
                cards.append({"section": "donghua_terbaru", "cards": section_items})

            result = {
                "results": cards,
                "page": self.__page,
                "total": len(cards),
                "source": self.history_url,
            }
            return result

        except Exception as e:
            logger.error(f"Error extracting home page content: {e}")
            return {
                "results": [],
                "page": self.__page,
                "total": 0,
                "source": self.history_url,
                "error": str(e),
            }

    def get_details(self) -> Dict[str, Union[List[Dict[str, Any]], int, str]]:
        """Get home page details."""
        try:
            url = ""
            if self.__page > 1:
                url = f"/page/{self.__page}/"

            data = self.get_parsed_html(url)
            if not data:
                return {
                    "results": [],
                    "page": self.__page,
                    "total": 0,
                    "source": self.history_url,
                    "error": "Failed to fetch home page",
                }

            return self.__get_home(data)
        except Exception as e:
            return {
                "results": [],
                "page": self.__page,
                "total": 0,
                "source": self.history_url,
                "error": str(e),
            }
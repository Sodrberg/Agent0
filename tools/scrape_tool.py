import requests
from bs4 import BeautifulSoup
from crewai_tools import BaseTool
from typing import List


class Scraper(BaseTool):
    name: str = "WebScraper"
    description: str = "Scrapes the content of multiple websites"

    def _run(self, urls: List[str]) -> str:
        """
        Scrape the content of multiple websites.

        :param urls: A list of URLs to scrape.
        :return: A dictionary where keys are URLs and values are the scraped content.
        """
        scraped_content = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        for url in urls:
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    text = soup.get_text(separator='\n', strip=True)
                    scraped_content[url] = text
                else:
                    print(
                        f"Failed to fetch {url}: Status code {response.status_code}")
            except requests.RequestException as e:
                print(f"Error scraping {url}: {e}")

        return scraped_content

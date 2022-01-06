import requests
import sys
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

    # Get Page from given url
    # :return: BeautifulSoup object or None
    def get_page(self, url):
        try:
            req = self.session.get(url, headers=self.headers)
        except Exception as e:
            print(e)
            sys.exit('an error has occur while requesting a session')

        bs = BeautifulSoup(req.text, "html.parser")

        return bs
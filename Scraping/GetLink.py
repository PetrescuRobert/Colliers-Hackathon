# Documentation available on https://www.kdnuggets.com/2018/02/web-scraping-tutorial-python.html
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as Soup
import requests
import re
import re
import csv

class ScrapingService:
    def OLXScraping(self, page_link):

        #fetch the content from url
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        # extract all html elements from page
        prices = page_content.find_all(attrs={'class':'visible-xs mobile-container-url'});

        l = list(iter(prices));
        result = []
        for s in l:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(s))
            result.append(str(urls[0]))

        return result;
sc = ScrapingService()
print(sc.OLXScraping("https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov/bragadiru"))

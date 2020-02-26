# Documentation available on https://www.kdnuggets.com/2018/02/web-scraping-tutorial-python.html
from bs4 import BeautifulSoup
import requests

s = "https://www.olx.ro/imobiliare/apartamente-garsoniere-de-vanzare"

class ScrapingService:
    def OLXScraping(self, page_link):
    
        #fetch the content from url
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        # extract all html elements from page
        prices = page_content.find_all(attrs={'class':'price'});
        l = list(iter(prices));
        
        return l;

    def CELScraping(self, page_link):
    
        #fetch the content from url
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        # extract all html elements from page
        prices = page_content.find_all(attrs={'class':'productPrice'});
        aux1 = str(prices)
        i1 = aux1.index('productprice="1">')
        aux2 = aux1[i1+17:]
        i2 = aux2.index('<')
        result = aux2[0:i2];
        return float(result);

    def FLANCOScraping(self, page_link):
        #fetch the content from url
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        # extract all html elements from page
        prices = page_content.find_all(attrs={'class':'produs-price'});
        #print(prices);
        aux1 = str(prices)
        i1 = aux1.index('content="')
        aux2 = aux1[i1+9:]
        i2 = aux2.index('" ')
        result = aux2[0:i2];
        return float(result);


city = raw_input("Please enter city: ")
search = raw_input("Please enter search log: ")

sv = ScrapingService();
print(sv.OLXScraping("https://www.olx.ro/imobiliare/" + city + "/q-" + search));
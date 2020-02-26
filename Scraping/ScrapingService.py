# Documentation available on https://www.kdnuggets.com/2018/02/web-scraping-tutorial-python.html
from bs4 import BeautifulSoup
import requests
import re
import csv

number_columns = 13;

class ScrapingService:

    def GetLinks(self, page_link):

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

    def IMOBILIAREScraping(self, page_link):

        to_write_in_excel = []

        #fetch the content from url
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        # extract all html elements from page
        extract = page_content.find_all(attrs={'class':'col-lg-9 col-md-9 col-sm-9 col-xs-12' })
        #supraf = page_content.find_all(attrs={'class':'caracteristici'})

        #l2 = list(iter(supraf))
        l = list(iter(extract))
        city = str(l).split("> ")[1].split("<span")[0].split(", ")[0]
        to_write_in_excel.append(city)
        # area = str(l).split("> ")[1].split("<span")[0].split(", ")[1]
        #to_write_in_excel.append(area)

        extract = page_content.find_all(attrs={'class':'lista-tabelara' })
        l = list(iter(extract))
        tabel = str(l)

        supraf = re.findall(r'[0-9]*\,?[0-9]*\ mp', tabel)
        to_write_in_excel.extend(supraf)

        try:
            an_constructie = tabel.split("An construc\u0163ie:<span>")[1].split("</")[0]
            to_write_in_excel.append(an_constructie)
        except:
            print(2)

        extract = page_content.find("h4", text="Finisaje")

        if extract:
            extract = page_content.find("h4", text="Finisaje").find_next_sibling("ul")

            Finisaje = str(extract)
            Finisaje = Finisaje.replace("<span>", "")
            Finisaje = Finisaje.replace("</span>", "")
            Finisaje = Finisaje.replace("<li>", "")
            Finisaje = Finisaje.replace("</li>", " ; ")
            Finisaje = Finisaje.replace("<ul class=\"utilitati\">", "")
            Finisaje = Finisaje.replace("</ul>", "")

            to_write_in_excel.append(Finisaje)

        with open("baza_date.csv", "ab") as file:
            writer = csv.writer(file)
            writer.writerow(to_write_in_excel)

        return 1

sv = ScrapingService();

links = sv.GetLinks("https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov/bragadiru");
for el in links:
    sv.IMOBILIAREScraping(el)

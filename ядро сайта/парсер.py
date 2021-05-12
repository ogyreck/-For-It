import requests
from bs4 import BeautifulSoup
import csv


URL = "https://habr.com/en/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
           'accept': '*/*'}

def get_html(url, params=None):
   r = requests.get(url,headers = HEADERS, params = params)
   return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='post__title_link')

    links = []
    for item in items:
        links.append(
            item.get("href")
        )

    return links

def parse():
     html = get_html(URL)

     if html.status_code == 200:

        links = get_content(html.text)
        return links

     else:
        print("ОЩИБКА")



link_array = parse()

for i in link_array:
    URL = i
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
               'accept': '*/*'}

    print(i)
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r


    def get_content(html):
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find('div', class_='post__text').get_text(strip=True)

        return items

        # print(text_site)


    def csv_read(data, filename="data.txt"):
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(item)


    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            result = get_content(html.text)
            csv_read(result)

        else:
            print("ОЩИБКА")




    parse()

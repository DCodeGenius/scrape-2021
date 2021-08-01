from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://www.maala.org.il/%D7%93%D7%99%D7%A8%D7%95%D7%92-%D7%9E%D7%A2%D7%9C%D7%94/%d7%93%d7%99%d7%a8%d7%95%d7%92-%d7%9e%d7%a2%d7%9c%d7%94-2021/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = BeautifulSoup(webpage, "html.parser")
def get_company_url():
    main = page_soup.find('div',id="ct", class_="companies-table")
    details = main.find('div', class_="companies")
    links = details.find('div', class_='slider')
    counter = 0
    links_com = []
    for link in links.findAll('a'):
        if counter < 79:
            links_com.append(link.get('href'))
        counter += 1
    return links_com





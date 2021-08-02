from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from get_company_url import get_company_url

links_com = []
i = 0
links_com = get_company_url()
for x in links_com:
    url = 'https://' + urllib.parse.quote(links_com[i][8::])
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = BeautifulSoup(webpage, "html.parser")
    head = page_soup.find('div', id="content")
    details = head.find('div', class_="company-details clearfix")

    for title in head.findAll('div',class_="company-title"):
        if title is not None:
            f = open("fiverr.txt", "a")
            f.write(f"\n {title.text} ")
            f.close()

    for det in details.findAll('div'):
        if det is not None:
            f = open("fiverr.txt", "a")
            f.write(f"\n {det.text} ")
            f.close()

    table = page_soup.find("table")

    for tr in table.findAll('tr'):
        counter = 1
        para = tr.find('td', class_="parameter")
        percent = tr.find('td', class_="percent")
        if para is not None and percent is not None:
            f = open("fiverr.txt", "a")
            f.write(f"\n \n תחום ומשקל יחסי באחוזים: \n {para.text} \n  {percent.text}\n\n מה נבדק : ")
            f.close()
        for td in tr.find_all('li'):
            f = open("fiverr.txt", "a")
            f.write(f"\n - {td.text} ")
            f.close()
        for gr in tr.find_all('td'):
            if counter == 4:
                grade = gr.text
                f = open("fiverr.txt", "a")
                f.write(f"\n ציון: {grade} ")
                f.close()
            counter += 1
    i += 1

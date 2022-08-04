from bs4 import BeautifulSoup
import requests
from gen_link import link_generator
import datetime as dt
import xlsxwriter

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}


def req_zakupki_gov(keyword):

    workbook = xlsxwriter.Workbook('Тендеры.xlsx')
    worksheet = workbook.add_worksheet()

    end = dt.datetime.now() + dt.timedelta(days=3)
    url = link_generator(keyword, "10", "100000000",
                         end.strftime("%d.%m.%Y"), 1)
    resp = requests.get(url, headers=HEADERS)
    print(url)
    bs = BeautifulSoup(resp.text, "html.parser")
    all_tenders = bs.findAll("div", class_="row no-gutters registry-entry__form mr-0")
    for tender in all_tenders:
        fz = " ".join(tender.find("div", class_="col-9 p-0 registry-entry__header-top__title text-truncate").text.split()).strip()
        teg_id = tender.find("div", class_="registry-entry__header-mid__number").find("a")

        url_tender = teg_id.get_attribute_list("href")[0].strip()
        name = tender.find("div", class_="registry-entry__body-value").text.strip()

        teg_customer = tender.find("div", class_="registry-entry__body-href")
        customer_a = teg_customer.find("a")
        customer_name = customer_a.text.strip()
        customer_url = customer_a.get_attribute_list("href")[0].strip()

        price = tender.find("div", class_="price-block__value").text.strip()

        end_tender = tender.findAll("div", class_="data-block__value")[-1].text.strip()

        print(fz, "https://zakupki.gov.ru" + url_tender, name, customer_name, customer_url, price, end_tender, sep=" | ")

req_zakupki_gov("Конференция")
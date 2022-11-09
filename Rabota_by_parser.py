import re

from flask import Flask
import requests
from bs4 import BeautifulSoup
from pprint import pprint

app = Flask(__name__)


url = "https://rabota.by/vacancies/podrabotka?area=2237&clusters=true&page=0"
hdrs = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0), Gecko/20100101 Firefox/93.0",
    "Accept": "*/*"
        }

page = requests.get(url, headers=hdrs)

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

all_vac_premium = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy vacancy-serp__vacancy_premium"})
# pprint(all_vac_premium)
# pprint(f"len(all_vac_premium) = {len(all_vac_premium)}")
all_vac_standard = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy vacancy-serp__vacancy_standard"})
# pprint(all_vac_standard)
# pprint(f"len(all_vac_standard) = {len(all_vac_standard)}")
all_vac_standard_plus = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus"})
# pprint(all_vac_standard_plus)
# pprint(f"len(all_vac_standard_plus) = {len(all_vac_standard_plus)}")

print(f"Count of vacancies per page is: {len(all_vac_premium)+len(all_vac_standard)+len(all_vac_standard_plus)}")

print(all_vac_premium[0].prettify())


print("------------------------------------------")

all_vacancies = soup.find_all("a", {"data-qa": "vacancy-serp__vacancy-title"})
for i in all_vacancies:
    vacancy_salary = i.find_parent(class_="vacancy-serp-item__row vacancy-serp-item__row_header").\
        find("span", {"data-qa": "vacancy-serp__vacancy-compensation"})
    if vacancy_salary is not None:
        print(f"{i.text}, {vacancy_salary.text}, {i.get('href')}")
    else:
        print(f"{i.text}, No salary, {i['href']}")


@app.route('/')
def hello_world():
    pass


if __name__ == '__main__':
    app.run()

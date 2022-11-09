import re

from flask import Flask
import requests, random, time
from bs4 import BeautifulSoup as bs

from pprint import pprint


app = Flask(__name__)


def create_search_url_by_request():
    query_input = input("\nEnter keywords by space here: ").split()
    if len(query_input) != 0:
        search_query = query_input
    else:
        return "Please enter keyword"

    url_add = "".join([f"%20{i}" if len(search_query) > 1 else i for i in search_query]).strip("%20")
    search_url = f'https://jobs.dev.by/?&filter%5Bsearch%5D={url_add}'
    return search_url


def is_exists(item):            # Checking if any field in vacancy exists
    try:
        result = item.next_element.text
    except AttributeError:
        result = "N/A"
    return result


def get_descr(bs):    # Getting description walking string by strings
    descr_raw = bs.find("div", class_="text")
    if descr_raw == None:
        return f"Description not specified"
    descr_edited = ""
    for i in descr_raw.descendants:
        if isinstance(i, str):
            # regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            # url = re.findall(regex, str(i.previous_sibling))      # ===== Checking if URL in the text ===== #
            # if url:
            #     descr_edited += f"{i.strip()} {url}\n"
            if str(i.previous_element.name) == "li":
                descr_edited += f"\n\u30FB{i.strip()}"
            else:
                descr_edited += f"{i.strip()}\n"
    descr_fine = "\n".join([stng.rstrip() for stng in descr_edited.splitlines() if stng.strip()])
    return descr_fine

search_url = create_search_url_by_request()
print(f"\nSearch link is: {search_url}\n")
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
        }

req = requests.get(url=search_url, headers=headers)
page = bs(req.text, "lxml")
all_vacs = page.findAll("div", class_="vacancies-list-item")    # All vacancies as bs's elements

vac_num = 1
for vac in all_vacs:
    premium_vac_banner = vac.find("a", class_="button--link")
    email_vac_service = vac.find("div", class_="vacancies-item-banner")
    if not (premium_vac_banner or email_vac_service):
        link = "https://jobs.dev.by" + vac.find("a", class_="vacancies-list-item__link_block").get("href")
        vac_req = requests.get(url=link, headers=headers)
        vac_bs = bs(vac_req.text, "lxml")
        pos = is_exists(vac_bs.find("h1", class_="title"))
        spec = is_exists(vac_bs.find(text="Специализация: "))
        level = is_exists(vac_bs.find(text="Уровень: "))
        expir = is_exists(vac_bs.find(text="Опыт: "))
        english = is_exists(vac_bs.find(text="Уровень английского: "))
        salary = is_exists(vac_bs.find(text="Зарплата: "))
        loc = is_exists(vac_bs.find(text="Город: "))
        sched = is_exists(vac_bs.find(text="Режим работы: "))
        cows = is_exists(vac_bs.find(text="Размер команды: "))
        comp_size = is_exists(vac_bs.find(text="Размер компании: "))
        remote = is_exists(vac_bs.find(text="Возможна удалённая работа: "))
        skills_in_tags = vac_bs.find_all("div", class_="vacancy__tags__item")
        skills = ", ".join([i.next_element.text for i in skills_in_tags if skills_in_tags])
        descr = get_descr(vac_bs)

        print(f"{vac_num}/{len(all_vacs)-2}\nPosition: {pos}\nSpecialization: {spec}\nLevel: {level}\nExpirience: {expir}"
              f"\nEnglish level: {english}\nSalary: {salary}\nLocation: {loc}\nSchedule: {sched}\nCo-workers: {cows}"
              f"\nCompany size: {comp_size}\nRemote: {remote}\nSkills: {skills}\nDescription: {descr}\nLink: {link}\n")
        vac_num += 1
        # time.sleep(random.randrange(1, 3))

print("All vacancies are presented")


@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run()

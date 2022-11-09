import re

from flask import Flask
import requests, random, time
from bs4 import BeautifulSoup
from bs4 import NavigableString, Comment
from pprint import pprint


app = Flask(__name__)


def create_search_url_by_request():
    query_input = input("Enter keywords by space here: ").split()
    if len(query_input) != 0:
        search_query = query_input
    else:
        print("Please enter keyword")
        exit()

    url_add = "".join([f"%20{i}" if len(search_query) > 1 else i for i in search_query]).strip("%20")
    search_url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + url_add
    print(f"Search link is: {search_url}\n")
    return search_url


search_url = create_search_url_by_request()
headers = {
    "Accept": "image/avif,image/webp,*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36"
        }

req = requests.get(url=search_url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

pages_by_url = soup.find("div", {"data-test": "page-x-of-y"}).text.split()[-1]      # Getting max quantity of pages
last_page_by_url = search_url + "&p=" + pages_by_url                                # by searching request
print("Last page by request is: ", last_page_by_url, "\n")


def is_exists(item):            # Checking if any field (Position, Salary, Location) exists
    try:
        result = item.text
    except AttributeError:
        result = "N/A"
    return result


def get_descr(link, headers):    # Getting description walking string by strings
    vac_req = requests.get(url=link, headers=headers)
    vac_soup = BeautifulSoup(vac_req.text, "lxml")
    big_div = vac_soup.find("div", class_="ecgq1xb4")
    if big_div == None:
        return f"Description not specified"

    # from bs4 import NavigableString, Comment          # ===== Must try this =====
    # print
    # ''.join(unicode(child) for child in hit.children
    #         if isinstance(child, NavigableString) and not isinstance(child, Comment))


    descr_raw = ""
    for i in big_div.descendants:
        if isinstance(i, str):
            if str(i.previous_element.name) == "li":  # set(tag.name for tag in BeautifulSoup(html_cal, 'html.parser').find_all())
                descr_raw += f"\u30FB{i.strip('Â').strip()}\n"
            else:
                descr_raw += f"{i.strip('Â').strip()}\n"
    descr_fine = "\n".join([stng.rstrip() for stng in descr_raw.splitlines() if stng.strip()])
    return descr_fine

page_num = 0
all_id = []
for i in range(int(pages_by_url)):
    search_url_one_page = search_url + "&p=" + str(page_num)
    req = requests.get(url=search_url_one_page, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")

    all_vacs_per_page = soup.find_all("li", class_="react-job-listing")

    # for i, vac in enumerate(all_vacs_per_page):                                     # Output all vacancy's positions
    #     print(i + 1, vac.find("a", {"data-test": "job-link"}).find("span").text,    # and locations (to find error)
    #           vac.find("span", {"class": "css-1buaf54"}).text)                      # This list not equal as in a browser
    # print()

    count = page_num*30
    for vac in all_vacs_per_page:                                                   # Output vacancy information0
        pos = is_exists(vac.find("a", {"data-test": "job-link"}).find("span"))                       # Position
        sal = is_exists(vac.find("span", {"data-test": "detailSalary"}))                             # Salary
        comp = is_exists(vac.find("div", {"class": "flex-nowrap"}).find_previous_sibling())          # Company
        loc = is_exists(vac.find("span", {"class": "css-1buaf54"}))                                  # Location
        vac_id = vac.get("data-id")                                                                  # Vacancy ID
        linkv = "https://www.glassdoor.com" + vac.find("a", {"data-test": "job-link"}).get("href")   # Link
        descr = get_descr(linkv, headers)

        count += 1
        print(f'"{count}  Position: {pos}\n  Salary: {sal}\n  Company: {comp}\n  Location: {loc}\n  ID: {vac_id}\n  '
              f'Link: {linkv}\n  Description: {descr}"')

        # time.sleep(random.randrange(1, 3))
        all_id.append(vac_id) if vac_id not in all_id else print("This vacancy already exists")

    page_num += 1


@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run()

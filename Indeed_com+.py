from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests
import time, random
from flask import Flask
from fake_useragent import UserAgent

app = Flask(__name__)

# # Search by one-string request
# def create_search_url_by_request():
#     query_input = input("\nEnter keywords of position(1) and location(2) (only USA) by space here: ").split()
#     print("Len=", len(query_input))
#     if len(query_input) < 2:
#         print("Incorrect request")
#         exit()
#     # search_url = f"https://www.indeed.com/q-{query_input[0]}-l-{query_input[1]}-jobs"
#     search_url = f"https://www.indeed.com/jobs?q={query_input[0]}&l={query_input[1]}"
#     return search_url

def create_search_url_by_request():
    query_position = "=" + "%20".join(input("\nEnter keywords of position here: ").split())
    query_location = "=" + input("Enter keywords of location (only USA and only ONE word) here: ")
    if not query_position or not query_location:
        print("Incorrect request")
        exit()
    # search_url = f"https://www.indeed.com/q-{query_input[0]}-l-{query_input[1]}-jobs"
    search_url = f"https://www.indeed.com/jobs?q{query_position}&l{query_location}"
    return search_url

def vac_data(soup, count):
    vacs_div = soup.find("div", {"id": "mosaic-zone-jobcards"})
    all_vacs_per_page = vacs_div.findAll("a", {"data-hide-spinner": "true"})
    vacs_links_list_per_page = ["https://www.indeed.com" + vac.get("href") for vac in all_vacs_per_page]

    # Get all information from link page
    for vac_link in vacs_links_list_per_page:
        vac_resp = requests.get(url=vac_link, headers=headers)
        vac_soup = bs(vac_resp.text, "lxml")
        vs = vac_soup
        title = vs.find(class_="icl-u-xs-mb--xs").text
        company = vs.find("div", class_="icl-u-xs-mr--xs").text

        location = vs.find("div", class_="jobsearch-DesktopStickyContainer-companyrating").find_next_sibling()
        if location.find_next_sibling() and location.find_next_sibling().text.lower() == "remote":
            location = f"{location.text}; {location.find_next_sibling().text}"
        else:
            location = location.text

        try:
            schedule = vs.find("span", class_="jobsearch-JobMetadataHeader-item").text
        except:
            schedule = "N/A"

        # Description with original markup
        description = vs.find("div", {"id": "jobDescriptionText"}).text.strip()

        # Description wothout blank lines
        description = "".join([s for s in description.splitlines(True) if s.strip("\r\n")])

        # try:  ===ПРАЦУЮЧЫ===
        #     location = vs.find("div", class_="jobsearch-JobMetadataHeader-item").find_previous().text
        #     if location == 'Remote':
        #         location = vs.find("div", class_="jobsearch-JobMetadataHeader-item").find_previous().find_previous().text + f" + {location}"
        # except:
        #     location = "N/A"

        count += 1
        print(f"{count} {'*'*30}\nTitle: {title}\nCompany: {company}\nlocation: {location}\nSchedule: {schedule}"
              f"\nlink: {vac_link}\nDescription:\n{description}\n")

        time.sleep(1)

search_url = create_search_url_by_request()
print(f"Search url: {search_url}")
useragent = UserAgent()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "referer": f"{search_url}",
    "upgrade-insecure-requests": "1",
    "User-Agent": f"{useragent.random}"
}
resp = requests.get(url=search_url, headers=headers)

# soup = bs(resp.text, "lxml")
# vacs_div = soup.find("div", {"id": "mosaic-zone-jobcards"})
# all_vacs_per_page = vacs_div.findAll("a", {"data-hide-spinner": "true"})
# vacs_links_list_per_page = ["https://www.indeed.com" + vac.get("href") for vac in all_vacs_per_page]

pages_count = 0
count = 0
while True:
    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "User-Agent": f"{useragent.random}"
    }
    url = f"{search_url}&start={pages_count*10}"
    print(f"Current url: {url}")
    resp = requests.get(url=url, headers=headers1)

    soup = bs(resp.text, "lxml")
    count += 15 * pages_count
    if soup.find("a", {"aria-label": "Next"}):
        vac_data(soup, count)
        pages_count += 1
        print(f"Page {pages_count+1} exists\n")
        time.sleep(random.randrange(1, 2))
    else:
        vac_data(soup, count)
        print(f"There are only {pages_count+1} pages by your request")
        break








@app.route("/")
def funct():
    pass

if __name__ == "__main__":
    app.run()
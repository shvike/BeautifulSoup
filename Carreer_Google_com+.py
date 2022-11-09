from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests, re
import time, random
from flask import Flask
from fake_useragent import UserAgent


app = Flask(__name__)





def create_search_url_by_request(page):
    query_position = "%20".join(input("\nEnter keywords of position here: ").split())
    if not query_position:
        print("Incorrect request")
        exit()
    else:
        search_url = f"https://careers.google.com/api/v3/search/?distance=50&page=1&q={query_position}"


        # search_url = f"https://careers.google.com/jobs/results/?distance=50&q={query_position}"

    # <<< For further development we have to khow if location input is necessary >>>
    # query_location = input("Enter keywords of location (only USA and only ONE word) here: ")
    # if not query_location:
    #     search_url = f"https://careers.google.com/jobs/results/?distance=50&q={query_position}"
    # else:
    #     search_url = "Location value in <NOT NULL>! Need to be developed with Selenuim due the city_state value"
    #     # "https://careers.google.com/jobs/results/?distance=50&location=Los%20Angeles,%20CA,%20USA&q=python"
    #     # search_url = f"https://careers.google.com/jobs/results/?distance=50&location={query_location}&q={query_position}"
    return search_url


for i in range(1, 10):
    search_url = create_search_url_by_request(i)
    if i == 1:
        print(f"Search url: {search_url}")
#
# search_url = "https://careers.google.com/api/v3/search/?distance=50&page=1&q=python"
# print(f"Search url: {search_url}")
    useragent = UserAgent()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/"
                  "signed-exchange;v=b3;q=0.9",
        "upgrade-insecure-requests": "1",

        "User-Agent": f"{useragent.random}"
    }
    resp = requests.get(url=search_url, headers=headers)

    # with open("Carr.json", "a", encoding="utf-8") as file:
    #     file.write(resp.text)

    def clear_text(text):
        return "".join([re.sub('<[^<]+?>', '', s) for s in text.splitlines(True) if s.strip("\r\n")]).strip("\n")

    count = (i-1)
    num = 1
    data = resp.json()
    for item in data["jobs"]:
        cv_number = count*10 + num
        position = item["title"]
        link = item["apply_url"]
        skills = item["qualifications"]
        skills = "".join([re.sub('<[^<]+?>', '', s) for s in item["qualifications"].splitlines(True) if s.strip("\r\n")])
        company_name = item["company_name"]
        remote = "; Remote" if item["has_remote"] else ""
        location = "; ".join([i["display"] for i in item["locations"]]) + remote
        descriptions = clear_text(item["description"])
        responsibilities = clear_text(item["responsibilities"])
        description = descriptions + responsibilities
        print(f"\n>>>>> {cv_number}\nPosition: {position}\nLink: {link}\nSkills: {skills}\nCompany: {company_name}\n"
              f"Location: {location}\nDescription: {description}\n")

        num += 1
        time.sleep(random.randrange(1, 3))






@app.route("/")
def funct():
    pass

if __name__ == "__main__":
    app.run()
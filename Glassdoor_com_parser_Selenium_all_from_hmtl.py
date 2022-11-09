import re

from flask import Flask
import requests, random, time
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Comment
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


app = Flask(__name__)

"""
def prepare_search_input(query_input):
    if len(query_input) != 0:
        search_query = query_input
    else:
        return "Please enter keyword"
    url_add = "".join([f"%20{i}" if len(search_query) > 1 else i for i in search_query]).strip("%20")
    return url_add


def create_search_url_glassdoor():
    query_input = input("\nGlassdoor.com\nEnter keywords by space here: ").split()
    url_add = prepare_search_input(query_input)
    search_url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + url_add
    return search_url


def is_exists_glassdoor(item):  # Checking if any field (Position, Salary, Location) exists
    try:
        result = item.text
    except AttributeError:
        result = "N/A"
    return result




def get_descr(link, headers):    # Getting description walking string by strings
    vac_req = requests.get(url=link, headers=headers)
    vac_soup = bs(vac_req.text, "lxml")
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


search_url = create_search_url_glassdoor()
headers = {
    "Accept": "image/avif,image/webp,*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36"
        }

req = requests.get(url=search_url, headers=headers)
soup = bs(req.text, "lxml")

pages_by_url = soup.find("div", {"data-test": "page-x-of-y"}).text.split()[-1]      # Getting max quantity of pages
last_page_by_url = search_url + "&p=" + pages_by_url                                # by searching request
print("Last page by request is: ", last_page_by_url, "\n")

page_num = 0
all_id = []
# for i in range(int(pages_by_url)):
for i in range(1):
    search_url_one_page = search_url + "&p=" + str(page_num)
    req = requests.get(url=search_url_one_page, headers=headers)
    soup = bs(req.text, "lxml")

    all_vacs_per_page = soup.find_all("li", class_="react-job-listing")

    # for i, vac in enumerate(all_vacs_per_page):                                     # Output all vacancy's positions
    #     print(i + 1, vac.find("a", {"data-test": "job-link"}).find("span").text,    # and locations (to find error)
    #           vac.find("span", {"class": "css-1buaf54"}).text)                      # This list not equal as in a browser
    # print()

    count = page_num*30
    for vac in all_vacs_per_page:                                                   # Output vacancy information0
        # pos = is_exists(vac.find("a", {"data-test": "job-link"}).find("span"))                       # Position
        # sal = is_exists(vac.find("span", {"data-test": "detailSalary"}))                             # Salary
        # comp = is_exists(vac.find("div", {"class": "flex-nowrap"}).find_previous_sibling())          # Company
        # loc = is_exists(vac.find("span", {"class": "css-1buaf54"}))                                  # Location
        # vac_id = vac.get("data-id")                                                                  # Vacancy ID
        # descr = get_descr(linkv, headers)
        linkv = "https://www.glassdoor.com" + vac.find("a", {"data-test": "job-link"}).get("href")   # Link
        print(linkv)
        # vac_req = requests.get(url=linkv, headers=headers)
        # soup = bs(vac_req.text, "lxml")

        # print(vac_req.text)
        # with open(f"Vac_{count}.html", "w", encoding="utf-8") as file:
        #     file.write(vac_req.text)

        get_info_selenium(linkv)

        count += 1

        # print(f'"{count}  Position: {pos}\n  Salary: {sal}\n  Company: {comp}\n  Location: {loc}\n  ID: {vac_id}\n  '
        #       f'Link: {linkv}\n  Description: {descr}"')

        # time.sleep(random.randrange(1, 3))
        # all_id.append(vac_id) if vac_id not in all_id else print("This vacancy already exists")

    page_num += 1
"""



# def get_info_selenium(linkv):
def get_comptype_sector_selenium():
    headers = {
        "Accept": "image/avif,image/webp,*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.81 Safari/537.36"
    }

    # # FIREFOX
    # options = webdriver.FirefoxOptions()
    # options.set_preference("general.useragent.override",
    #                        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
    #
    # # Start headless mode
    # options.add_argument("--headless")
    #
    # driver = webdriver.Firefox(
    #     executable_path="C:\\BeautifulSoup\\geckodriver.exe",
    #     options=options
    # )


    # CHROME
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40")
    options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    options.add_argument("upgrade-insecure-requests=1")
    options.add_argument("accept-encoding=gzip, deflate, br")
    options.add_argument("accept-language=en-GB,en;q=0.9,en-US;q=0.8")
    options.add_argument("cache-control=max-age=0")
    # options.add_argument("cookie=gdId=a1d6c0f2-2e27-40a2-ae66-2df8d9d419f3; trs=direct:direct:direct:2021-10-25+12:16:31.63:undefined:undefined; indeedCtk=1fise418eu5dk801; _gid=GA1.2.1331093537.1635189398; _optionalConsent=true; _gcl_au=1.1.67833082.1635189399; _fbp=fb.1.1635189399421.366325899; __gads=ID=d25f399b5c8fb22c-2299095400cb00bf:T=1635189400:S=ALNI_MaGF9YMdEYnjMupC-4tHLtgwvzG4g; G_ENABLED_IDPS=google; ki_r=; fpvc=3; ki_u=ecb1f108-2013-2dd5-5c78-d455; ki_s=218147:1.0.0.0.2; uc=8013A8318C98C5175FDE25CA4FFA611CE882096A5D6D2F742BE2D692F7C131461917F16DEA2637FD695EBE8185A2CB1EB4B7AB9B112CADF171B12F25A113E6C41EA1A2B469B4581A257AFB2B4950BC4A54298AB7CEC03D92FB824D3F5A87F39FB7D72E1C0EB4735411C662CD026ECFC9FE9AB44B2803AB304705838F43D7D892B858053E6FDB6D01002833466BF81EC8; ki_t=1635283654088;1636193361655;1636193365664;8;14; JSESSIONID=0D9A48345EC57CD14A1BAF181A8CA822; asst=1636231494.0; GSESSIONID=undefined; JSESSIONID_JX_APP=93A8B27BFA167E51A465E0C066C47AB5; _GA_Job_Session=true; cass=2; __cf_bm=.yAN.qJNKcDh79Sj_4JyUExei7DkSr12Pgy9W4OxBs0-1636233151-0-ATkItVjtp0cyAAWAfYahqNWfVESkGUqm1kF8aW/4+ruLRRtGgMTRwdUUNiL37tTO5NTRL1qCyCQkyUDF7CwwHcs=; _ga=GA1.2.387389572.1635189398; OptanonConsent=isIABGlobal=false&datestamp=Sun+Nov+07+2021+00:13:16+GMT+0300+(Moscow+Standard+Time)&version=6.8.0&hosts=&consentId=e6bfa58b-3c35-420c-bc85-fa6b5451fdbb&interactionCount=1&landingPath=NotLandingPage&groups=C0001:1,C0003:1,C0002:1,C0004:1,C0017:1&AwaitingReconsent=false; _ga_RC95PMVB3H=GS1.1.1636232450.46.1.1636233486.60; AWSALB=w2aNHdjykTwrzWUjlQ9xC9QxNNJ9z1v8e7QcOv5ZL6mgZxZHFiZC9E/ng0mYE7L6Q5WNktI7/w+0jb8mBBj3YnoS9J3zc/qZ30p/WEFve2R+ymIOQFNKoT1Tnqb7KFJ73TvyB3DM1bIowsTNfYpru+iKHyV0STWNtVy2OOd5K/CLvvkmjPalJOry+nGAXA==; AWSALBCORS=w2aNHdjykTwrzWUjlQ9xC9QxNNJ9z1v8e7QcOv5ZL6mgZxZHFiZC9E/ng0mYE7L6Q5WNktI7/w+0jb8mBBj3YnoS9J3zc/qZ30p/WEFve2R+ymIOQFNKoT1Tnqb7KFJ73TvyB3DM1bIowsTNfYpru+iKHyV0STWNtVy2OOd5K/CLvvkmjPalJOry+nGAXA==; ADRUM_BTa=R:0|g:27bd3ad1-fe14-4f83-a547-a7d069f08344|n:glassdoor_17d346a0-2ec1-4454-86b0-73b3b787aee9; SameSite=None; gdsid=1636231494720:1636233749368:EB5B888B4190A39DA6DCA7E8467052AB; at=9Zj1BkBogDvXjN_FjNCu18gEIB_fqbY2W50TOKw-CYNlGyb8lqmRTkPa80pTuHNAUpcKeMCII29mqR5zhKLUcwnskYYTHgDwDQjGliqQPbqwgBPJfEcunN9y_4n--aebyRZqVPvQuvT1IdivJqnJt0z7Yy7M0dSJK1xTMshbv9UCawgK3vGU08Y7FaK8Wb6k0TovqCO2-cx378TeDvfGhS16dy8Zr5TtiXrK6H3NiK82fEQmkVRyuaeqFrgHtyKlV6RyDBJ64NGb8sE_ssX-WQX66aZbnomTVEQiR4l0xvMm2c7lrP5n4_z3iTXtZkRyjG29bm2EW7a2W2csDAGy7M9bTZaddGcTvdDeyYEjHfiJ3OMh8ZHjvvhk8ars7SAb9ihDt4t1Is2cnww4CLjHzcXAaB1AwZtmGjhoKu7QSjKSQo3f6NhH0gh1VNsIPUF_kFCGOBf1sYnoc3Di099EXwlWkWuPFPARPgtlosrqpB5hWe7ZJ0GoT-TMGjBHWiGC7no9elqIisrrVpYOKrYSugEyMEkYvF_CRDJbfZu_11TsFPsbEfn0fbXKAdZ6WBpCwSRRbeecyYURq2b7XK6iMk1Vh0Nu62xTokQQIpjxkKhoPdWE_u-0CbjsKAKC4g6z6qDogODkF9msAeFHOdHDapGePzpSgIVyUXcUIivbBognFNTg0kkdX1QDcSdgc--ogzBiWaEbFGj3hcwQDgjB6tsQxZ3oR1x80O5anIAF7azTmbpWriml1vqo7vNH-O3lRHqNMPoa9sJ3Bz5jiAk4FyEWu7ofjYcmc2P3-M_SExwcquBxSLNO0NGRgENBzr-9BheHN6WDobQgPy9xQ7SN-JccNb4T2__ddKhBKaVJTXg7Pp67QtGuS6fzNtlUf9o; bs=Xc4hJAHfNqBLVI7DastRYw:9Z0_VWSNmEqAa9HqeC5joTKmDrJvxQUTLOf3no9m-TSd4eXCNGn0TKhU4-EJshMtBU95yoXarivQk5UWhvh9GwfUEpper084Zg-mutUbsrY:QhTW5hvVsNE_IhzreQ-VNLwXk3nBMawmxUR_VgHVUEY")
    options.add_argument("sec-fetch-user=?1")
    # options.add_argument("jl: 1007362108821")

    # To forbid opening Chrome (all actions are hidden)
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path="C:\\BeautifulSoup\\chromedriver.exe",
        options=options
    )

    try:
        # link = "https://www.glassdoor.com/job-listing/software-engineer-i-disney-streaming-JV_IC1147401_KO0,19_KE20,36.htm?jl=1007412721022&pos=111&ao=1136043&s=58&guid=0000017cecc747f38232909e80de0358&src=GD_JOB_AD&t=SR&vt=w&uido=A5FF8CD622EE46F24E5F1F50B218BBE2&cs=1_0f1d5016&cb=1636060056850&jobListingId=1007412721022&jrtk=3-0-1fjmcei1au516801-1fjmcei1rhimm800-e6b0a70cad98adb6-&ctt=1636060626394"
        # link = "https://www.glassdoor.com/job-listing/python-developer-shuup-commerce-JV_KO0,16_KE17,31.htm?jl=1007399602250&pos=103&ao=1136043&s=58&guid=0000017cecc747f38232909e80de0358&src=GD_JOB_AD&t=SR&vt=w&uido=A5FF8CD622EE46F24E5F1F50B218BBE2&cs=1_1888c65a&cb=1636060056846&jobListingId=1007399602250&jrtk=3-0-1fjmcei1au516801-1fjmcei1rhimm800-f9534ae0091f5310-&ctt=1636060102129"
        # link = "https://www.glassdoor.com/job-listing/jr-python-developer-comcast-JV_IC1152672_KO0,19_KE20,27.htm?jl=1007386662429&pos=103&ao=1136043&s=58&guid=0000017cec95f5ecaeecfa7e7b0314da&src=GD_JOB_AD&t=SR&vt=w&cs=1_346df1e0&cb=1636056824768&jobListingId=1007386662429&jrtk=3-0-1fjm9btmru4rk801-1fjm9btndu34r800-34d27ea6c2e8a66b-&ctt=1636056908473"
        link = "https://www.glassdoor.com/job-listing/jr-python-developer-futrend-technology-JV_IC1153899_KO0,19_KE20,38.htm?jl=1007354450649&pos=121&ao=1136043&s=58&guid=0000017cf4b935cfbd2ac7484eafdea7&src=GD_JOB_AD&t=SR&vt=w&uido=A5FF8CD622EE46F24E5F1F50B218BBE2&cs=1_e662b49d&cb=1636193352282&jobListingId=1007354450649&jrtk=3-0-1fjqbidhlu4p7801-1fjqbidi3u1ck800-5e3410c1d37f8e00-&ctt=1636193484978"
        # link = "https://www.glassdoor.com/job-listing/python-react-front-end-developer-azul-partners-JV_IC1128808_KO0,32_KE33,46.htm?jl=1007362108821&pos=104&ao=1136043&s=58&guid=0000017cec95f5ecaeecfa7e7b0314da&src=GD_JOB_AD&t=SR&vt=w&cs=1_ba627b8f&cb=1636056824768&jobListingId=1007362108821&jrtk=3-0-1fjm9btmru4rk801-1fjm9btndu34r800-007d9e472d67cdb0-&ctt=1636059851553"
        driver.get(link)
        time.sleep(2)
        result = []
        names = driver.find_elements_by_class_name("e1eh6fgm0")   # clicks the elements
        for i in names:                                           # after "Job"
            # i.click()                                           #
            # time.sleep(2)                                       #
            print(i.get_attribute("data-tab-type"))
            # if i.get_attribute("data-tab-type") not in names:
            #     print("There is no element 'overview'")
            if i.get_attribute("data-tab-type") == "overview":
                i.click()
                time.sleep(3)

                # attr = driver.execute_script(  # find out all element attributes
                #         'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
                #         i)
                # print(attr)

                def get_field_type(pause=3):
                    try:
                        field_type = driver.find_element_by_xpath(
                        '//*[@id="PageBodyContents"]/div[3]/div/div/div/div/div[1]/div/div[4]/span'
                    )
                        print(f"=====Company type from def: {field_type.text}=====\n")
                        return field_type
                    except Exception as ex:
                        print(ex.__class__)
                        if pause < 10:
                            print(f"Attempt failed, pause={pause}")
                            time.sleep(pause)
                            get_field_type(pause=(pause + 10))
                        else:
                            time.sleep(60)
                            get_comptype_sector_selenium()

                    




                    # return field_type


                field_type = get_field_type()

                # XPath to the "Company type" value
                # field_type = driver.find_element_by_xpath(
                #     '//*[@id="PageBodyContents"]/div[3]/div/div/div/div/div[1]/div/div[4]/span'
                # )
                # print(f"=====Company type: {field_type.text}=====\n")
                result.append(field_type.text)

                # XPath to the "Sector" value
                field_sector = driver.find_element_by_xpath('// *[ @ id = "InfoFields"] / div[6] / span')
                print(f"=====Sector: {field_sector.text}=====\n")
                result.append(field_sector.text)
                break



        return result



    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



company_data = get_comptype_sector_selenium()
if company_data and len(company_data) > 1:
    print(f"Company type: {company_data[0]},\nSector: {company_data[1]}")
else:
    company_data = ["There is no information about Company type and Sector"]
    print(company_data)

# with open("namestest.txt", "a") as file:
#     for i in names:
#         file.write(str(i))

# with open("namestest.txt") as file:
#     src = file.read()
#
# print(len(src))


@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run()

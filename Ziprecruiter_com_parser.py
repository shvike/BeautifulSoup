# from flask import Flask
# import requests
# from bs4 import BeautifulSoup
# from bs4 import NavigableString, Comment
# from pprint import pprint
#
#
# url = "https://www.ziprecruiter.com/candidae/search?search=developer&location=USA&page=1"
# hdrs = {
#     "Accept": "image/avif,image/webp,*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/94.0.4606.81 Safari/537.36"
#         }
#
# # page = requests.get(url, headers=hdrs)
# # pprint(page.status_code)
# # soup = BeautifulSoup(page.text, "html.parser")
# # # print(soup)
# # print()
#
#
# session = requests.Session()
# paggge = session.post(url, headers=hdrs, data={"email": "s@tyt.be"})
#
# print(paggge)
#
# reggge_url2 = "https://www.ziprecruiter.com/candidae/search?search=developer&location=USA&page=1"
#
# sent = session.get(reggge_url2, params=payload, headers=hdrs)
#
# soup = BeautifulSoup(paggge.text, "lxml")
# pprint(soup)
#
#
#
# # vac_per_page = soup.find_all("div", class_="job_content")
# #
# # pprint(vac_per_page)
#
#
# # all_vac_standard_plus = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus"})
# # pprint(all_vac_standard_plus)
# # pprint(f"len(all_vac_standard_plus) = {len(all_vac_standard_plus)}")
#
# # print(f"Count of vacancies per page is: {len(all_vac_premium)+len(all_vac_standard)+len(all_vac_standard_plus)}")
# #
# # print(all_vac_premium[0].prettify())
#
#
# print("------------------------------------------")
#
# # all_vacancies = soup.find_all("a", {"data-qa": "vacancy-serp__vacancy-title"})
# # for i in all_vacancies:
# #     vacancy_salary = i.find_parent(class_="vacancy-serp-item__row vacancy-serp-item__row_header").\
# #         find("span", {"data-qa": "vacancy-serp__vacancy-compensation"})
# #     if vacancy_salary is not None:
# #         print(f"{i.text}, {vacancy_salary.text}, {i.get('href')}")
# #     else:
# #         print(f"{i.text}, No salary, {i['href']}")
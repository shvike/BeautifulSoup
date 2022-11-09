import fake_useragent
from flask import Flask
import requests, random, time, cfscrape
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Comment
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


app = Flask(__name__)

"""
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    # "host": "www.ziprecruiter.com",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
    # "cache-control": "max-age=0",
    # "if-modified-since": "Mon, 08 Nov 2021 20:44:52 GMT",
    # # "sec-ch-ua": '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    # # "cookie": "__cf_bm=HbyeaRfwGEjlTmxXK3FpIppS1GlZx7uQCUNgU4g9vR8-1636404202-0-Ab3um8wvtcILeitSTHACu7cwV8jShoyL/TR2QPLtBv4id2H9smbrZagIa5+8nyQZ/J5bLLGJQcQm4AWE65X2K8/9gaLJjJlNZf++B+giFuA6; ziprecruiter_browser=46.216.32.148_1636404202_364055724; usprivacy=1YNY; zglobalid=3865d9d0-dd5f-45a8-beb1-3a49e7687f27.a69088a8aac5.61898bea; ziprecruiter_session=7c039b7053520b2753f95b9ef452ff1cf7e5c55f; uspmeta={"ce":1636404202}; SAFESAVE_TOKEN=f017aa8cbaba7c2cf0bca6a11d488cd5525c4ec2; zva=100000000;vid:YYmL6s3JLnaJ8kOB; _ga=GA1.2.729743523.1636404204; _gid=GA1.2.1317321926.1636404204; experian_campaign_visited=1; _gcl_au=1.1.1103709334.1636404206; _uetsid=85985b2040d411ec8d4e1b6d8553b443; _uetvid=8598a3a040d411ecad9ac3d281479e4f; fpcid=3526343822448710797_FPD; __pdst=268baf96b10c429da59fa0dd43dfe815; IR_gbd=ziprecruiter.com; ki_r=; ki_s=220840:0.0.0.0.0; _fbp=fb.1.1636404216753.1769736535; job-seeker-overlay-test=1; first_page_view=first_page_view={"js_podsights":1,"js_ott_tradr":1,"js_artsai":1}; google_signup_am=1; cto_bundle=7y50Jl9pNjNxVVBBYXNmVmJHQ254Q3JXQnBVNThxbHVRZmN4elRBb0hZZGZEUXdEb3FjTSUyQmwlMkJ1c0RaZEJTRzdwWDZKRUNRUXdEcWRnNXRFTCUyQmNkdnRkZjV5dng0cFhaN3MxUmtUMmhBRzdUZ1phQ0VxeTBGRXJDVVZIZXdoSnBrVXFldTMlMkZyaUJCTjRRWU9oNlM1eXlmaU9zUSUzRCUzRA; last_js_u=https://www.ziprecruiter.com/candidate/search?radius=500&search=python&location=usa; IR_10589=1636404294091|0|1636404294091||; ki_t=1636404206481;1636404206481;1636404294105;1;7",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "Windows",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "none",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    # # "referer": "https://www.ziprecruiter.com"
}

params = {
    "radius": "500",
    "search": "python",
    "location": "usa"
}

# def get_session():
#     session = requests.Session()
#     session.headers = {
#         # 'Host':'www.artstation.com',
#         # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
#         # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         # 'Accept-Language':'ru,en-US;q=0.5',
#         # 'Accept-Encoding':'gzip, deflate, br',
#         # 'DNT':'1',
#         # 'Connection':'keep-alive',
#         # 'Upgrade-Insecure-Requests':'1',
#         # 'Pragma':'no-cache',
#         # 'Cache-Control':'no-cache'
#         "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
#                   "application/signed-exchange;v=b3;q=0.9"
# }
#     return cfscrape.create_scraper(sess=session)
#
# session = get_session() # Дальше работать как с обычной requests.Session
# request = session.get(url=url, headers=headers, params=params)

url = "https://www.ziprecruiter.com/candidate/search?radius=5000&search=python&location=usa"
req = requests.get(url=url)
print(req.cookies)
print("=======ses_req=======")



req = requests.get(url=url, headers=headers)
print(req.status_code)
print(1)

# session = requests.Session()
# req = session.get(url=url, headers=headers, params=params)
# print(req.status_code)

print(2)
# r = requests.get('{}#!{}'.format(url, 'meme'), headers=headers)
# print(r.status_code)
"""


"""2 попытка 
url = "https://www.ziprecruiter.com/candidate/search?search=python&location=usa"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    # "host": "www.ziprecruiter.com",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
    # "cache-control": "max-age=0",
    # "if-modified-since": "Mon, 08 Nov 2021 20:44:52 GMT",
    # # "sec-ch-ua": '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    # # "cookie": "__cf_bm=HbyeaRfwGEjlTmxXK3FpIppS1GlZx7uQCUNgU4g9vR8-1636404202-0-Ab3um8wvtcILeitSTHACu7cwV8jShoyL/TR2QPLtBv4id2H9smbrZagIa5+8nyQZ/J5bLLGJQcQm4AWE65X2K8/9gaLJjJlNZf++B+giFuA6; ziprecruiter_browser=46.216.32.148_1636404202_364055724; usprivacy=1YNY; zglobalid=3865d9d0-dd5f-45a8-beb1-3a49e7687f27.a69088a8aac5.61898bea; ziprecruiter_session=7c039b7053520b2753f95b9ef452ff1cf7e5c55f; uspmeta={"ce":1636404202}; SAFESAVE_TOKEN=f017aa8cbaba7c2cf0bca6a11d488cd5525c4ec2; zva=100000000;vid:YYmL6s3JLnaJ8kOB; _ga=GA1.2.729743523.1636404204; _gid=GA1.2.1317321926.1636404204; experian_campaign_visited=1; _gcl_au=1.1.1103709334.1636404206; _uetsid=85985b2040d411ec8d4e1b6d8553b443; _uetvid=8598a3a040d411ecad9ac3d281479e4f; fpcid=3526343822448710797_FPD; __pdst=268baf96b10c429da59fa0dd43dfe815; IR_gbd=ziprecruiter.com; ki_r=; ki_s=220840:0.0.0.0.0; _fbp=fb.1.1636404216753.1769736535; job-seeker-overlay-test=1; first_page_view=first_page_view={"js_podsights":1,"js_ott_tradr":1,"js_artsai":1}; google_signup_am=1; cto_bundle=7y50Jl9pNjNxVVBBYXNmVmJHQ254Q3JXQnBVNThxbHVRZmN4elRBb0hZZGZEUXdEb3FjTSUyQmwlMkJ1c0RaZEJTRzdwWDZKRUNRUXdEcWRnNXRFTCUyQmNkdnRkZjV5dng0cFhaN3MxUmtUMmhBRzdUZ1phQ0VxeTBGRXJDVVZIZXdoSnBrVXFldTMlMkZyaUJCTjRRWU9oNlM1eXlmaU9zUSUzRCUzRA; last_js_u=https://www.ziprecruiter.com/candidate/search?radius=500&search=python&location=usa; IR_10589=1636404294091|0|1636404294091||; ki_t=1636404206481;1636404206481;1636404294105;1;7",
    "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "Windows",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    # "referer": "https://www.ziprecruiter.com/candidate/search?search=python&location=usa"
}

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40")
# options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="C:\\BeautifulSoup\\chromedriver.exe",
    options=options
)
driver.maximize_window()

try:
    driver.get(url)
    time.sleep(1)
    try:
        # email_input = driver.find_element_by_name("email_address")
        # email_input.clear()
        # email_input.send_keys("itcoty.bel@gmail.com")
        # button = driver.find_element_by_name("select-menu-menu").click()
        # button = driver.find_element_by_name("create_alert_from_search").click()

        elem = driver.find_element_by_name("submit")
        ac = ActionChains(driver)
        ac.move_to_element(elem).move_by_offset(-350, 0).click().perform()

        session = requests.Session()
        req = session.get(url=url, headers=headers)
        print(req.status_code)

        time.sleep(50)
    except:
        pass
    driver.find_element_by_class_name("skip_to_content").click()
    time.sleep(5)
except Exception as ex:
    print(ex)
    print(ex.__class__)
finally:
    driver.close()
    driver.quit()
"""

""" 3 попытка
session = requests.Session()

# На странице авторизации вводим любые данные. В отправленном запросе открываем инсперктирование страницы,
# ищем ссылку для авторизации (url) (по ней проверяются вводимые данные в БД),
# затем "form-data"/"данные форм" и отправленные данные (логин/пароль) (data{...})
url = "https://www.ziprecruiter.com/candidate/create-from-search"
data = {"email_address": "itcoty.bel@gmail.com"}
user = fake_useragent.UserAgent().random
headers = {
    "user-agent": user
}

resp = session.post(url, data=data, headers=headers)
print(resp)

# Авторизуемся на сайте, чтобы получить "cookies"
site_url = "https://www.ziprecruiter.com/candidate/search?search=python&location=usa"
site_response = session.get(site_url, headers=headers)
print(site_response.status_code)

cookies_dict = [{"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
                for key in site_response.cookies]
print(cookies_dict)

# Создаем новую независимую сессию, куда подкидываем авторизованные "cookies", чтобы заходить уже без авторизации
session2 = requests.Session()
for cooks in cookies_dict:
    session2.cookies.set(**cooks)

resp2 = session2.get(url, headers=headers)
print(resp2.text)
"""

# auth_url = "https://www.ziprecruiter.com/authn/login"
auth_url = "https://www.google.com/recaptcha/api2/userverify?k=6LftIzsUAAAAALrl2_LzkYnBF0ngWRQUtkN7bNBU"

# captcha_url = "http://www.google.com/recaptcha/api2/userverify?k=6LftIzsUAAAAALr12_LzkYnBF0ngWRQUtkN7bNBU"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}

# data = {
#     "email": "itcoty.bel@gmail.com",
#     "password": "pass123*",
#     "next_url": "",
#     "submitted": "1",
#     "_token": "v1:U2FsdGVkX191WABk2zZ0w0ZyTRNim32YSFp-gbNWSla0zM4xdLEJRVg1GrPJlN_yvtP35EzXq76hVOFz76_w0lm0_uvsB0EI",
#     "g-recaptcha-response": "03AGdBq27IxOms9FvXlKrHEVkLXly98w5n6tR_C2L2lmPwoKcXaNzxCpZ8xb4P8lFZvIG-V8Z4lAlwGt3vDgSGmUzLwzoJijn7RH0qEl018tL9DJLkZN9Xpqohuuwe9lhMzLYNV4rla-vTscPAjua4oTto0TWlxprSadADRbx7-FwkIMjz_Uh3k1Xs0LCyW2N2IIm-mVDHPeNIBugmu8D9On1dgmzGQfK7XDIZY34mIQBtuT5lBLV9gv44OfEP-eyh6eVtTzQbMiY5PRdI8VtRvJYOmMoTrtLwbMEJvG9t3Yn4WW9FOkH3jAjAN5zhHPwZlRMiqWfT83yYORh03lrGqFwJXSCEATRpX95CCdnuyI9USrArUDETXqpzu6n9LoFSeZi5ApZNYSYiQX5sbc3sACGGG0tJxStIAWKHbCdpTRO3-VWjC3BvZ-_1ZOENSG1XJFWDPZbC90TmnF2Q8vpNLIw49yNCLdcpdA",
#     "_safesave": "e588cc95a7fd028c985d9d9dc56cc0ff853b0caa"
# }


#Or another form-data after loggIn
data = {
    "v": "yZguKF1TiDm6F3yJWVhmOKQ9",
    "c": "03AGdBq26uA3PYvOHrkPy9ARTx6YSbDeN-uQJNCduol-FeuTsougBxgU3nfPVYmOE0w5zWjZsSAKN_XFAIUzvVKnZ1duuU1W70pSwxkaQ1qDn9d7YwYOj-kIZafAABwfEBfTsM-ASoFCEV30yre_Q4X9cfOtQcE78lRMlI5VzmGDen8uLYNrZyOT8qpUQuMvvXtUTlCXiiLmJIMoVg8yND36SBXU1mxNYNeElW92dXN51JBpqOzjdwmXla3JK5XiLo9ycQx0qMlFA3OrwyG6FMgqUMl4tKsDlghMOIWS7NiUvZB7ZKr-zCvBEHo-OjRTbonOvjIFs3s10ibG2C2-O55lV3nwidS-7mJI-lWnq4WalliSam8sFvWMPCxfHccLXkjPyOfoX758n2eGj0jy4c_-ttLRKsYUDNyGbiHsreYmfp2FsWPDIuFoCpVq39fuiZxMejBHm1gU4359u2qRhRt20b3t3WrLhmahcQAcgXj_tMvHmauYVztKoGlx-3mcCmKQL4L827Q1Sy-Yo39YAdSIv11_s-THAm8aR8ipnJ8XQiSevDkgFBLh9v-Bmqy5GqmMpPLlgK_rSBsERq06BWj1cOP6YTf8oJzGfq-FsQKX9le81COi7mVcPrCo8Lh3gTZEuOld3s9Y8kF-_wLrTYbW34mAqeokvLhhohEts4kP1Z2Y39OSii5HtUNLxhkr3BI0vYgCn8abZvtnn9mg9R48uHLiDTmym2UqUsFJTfLo1F0SK1N7qsQyro8u31XCFXmp-4Wt0nRV0Uj_vtDRlbbEMP1NcYjpdz6HzaDav869JyoOtfur7atNN1KaXVIRDPKHDWzJKZS297ZJMjM-siA3lFom709WdPqtBoJ0Y1wcCIhFs4vmYuZK94velzuRtEQQLVr72bP0pCvMjwdlXTj0DvWH-c9LY5BfNg5l0JtvjM101NrxNMUzs1y6w-RGLQGKh34W_I0IDE3oU6EmXnZGvZG5n_lsw-lsC8FRDrQOpBSyesU3REontDihHG2pqfIl_aaovH5_NQGQywT8RFei6Dp-k_s-iMLZ2CxjUlvvtbkJ2EwyoU2rbSyoaiMnG3GLjJTlnZVXszSfW4gndoopfvZa-lPGdHfHDOfSMOknKX4Qw8s-dfYEvB47WlzQapzHPFLH9iqx1-wTUlS5IpB9T5dF51U3dgt4EWH4V2R6v0gb6zAbz8XMEUTqW0apg7cvjDzWscYEAX5qTkiZZfDdkGdYaPa15dji4NfBl_di6I69xiPxPIuGKaWJyUqmstHyLmGPmFbLlbR05D-bNTBqfKHaLOP0NvjIyEMUdPTKq8HQf93gbOPSN2jveTNlnLer4fVIwrpsVANUqO2vMCi8GxSBWC_sdHdX7nuPTm9_bMT0vUT1dqfXtxIZb5CRqZPx9TAIZnRCafT-mxuSUqRrsWxwuztch-19jJO0XdXRWT6LeljgDHF4Z7VCIooMawdJ7tawfsTXLOpw3XaSmRG3vKg7f3GLwUBqfzy32a-SmPzaQrya8U_MxL_9DKhmqWGqqiZ7n4E_N_mX4Icd9zWQ5mRgn9SHaVfkl85R-3X5VAnJIsAkMbUPtvY7tFYM2SBqB2OtnhlrYkRURZFmByRPSKXD3BODZupSsTRVfSYH_C_z5pRRs2AkXH8N2MaKs_-vFnMjRuFt_c_BrVe1jg8n1trwWNnNW1fn-iii_NPWlbjWlvTSHhtggH8Yd5Zx3yQNSH-EaK07lgm3nSXcfPruMT49RtwikDYpXK8zAnEwNjZ8l0oxPBUCZ3wZXkFHqnO1nRlhxlP49gLctDgCv2z3wKbnUSjn55XQn4L7HoHQzgrY6372W0IjJuxF77fz4PLU3S139R-JijmJ1AAOfFGEEolZip9Z9euEemPM8HcxeVrOGyMzOo-jcGNNujMjcfQAKv2bcs85NJAJa0VZEKrxtCxMc3V_04lZUQpOMwGjgJrL_eKISBeLWZmsqm-cEhTAAiBhT3ZofOKjezjRQu4E8gbue_kY4NxjOdcHFKWaZcpeGmTDw5COru7fIkqKvWt43swSz0LAMbSKhhhYzELjUpBmwP9y_trgyieC9p0pwZYxaMATqAPTBVK1-M4EqR_CI5rU0pyrYkYWVpFku1NlZEBx66rp09UEUhPv4pkKqBE4XLS4t_WgsReuZK1Ho9d1qg7umFbOybTgjkhmV2uDuSUosA1mAh9GCVdPSTU4BWKmXQuroCtSBjbJZHjZI1YlkJmhmhaybIBZ3F9g7CaMjK1c8kuQQiu-Xx2c4fMKOoyCSeBq-lUOB6m6_DYAMwRC7nuWy4XNecNd8J5inPTS4g2u6VZ1Xulp6Wp8EyGgDI4VQJeuLScUADecu3-B_JIWwXoyKR-wBWFzUqRRuPPg7T3uerIow0PbyhTdjTMs-3z-fXj06jJJriobUCuHjn-VGcBc-7zMR556VwXdG2cWTCnYEo5wGE3FjYhyNZqGDfBh7p3x0i71gytoLAh-4azmZPYH3g7rWeULbR4_CoKo9q20xmw9FVtta6pPWF-6t79slDqGvKdISrmywFSs73WTQx8WpVE5zBCt30QXkzpO4ZgYRyD4CJKzm0gtarhUrDMMorumRrXLU404e-5TnHyuuiT6TX9XzzbXcrgSS_KV8wzfXfhXN1Hq7iJtY4RIV1CB31J8A0QRbaEVvcA1RfjALXsHCaXQ1XZuvAUGNyz9_uoLjwOo2mdbRnBqVyqfeCc1PaP2gBP4lgbXCxONDCMGX2d0g4KzHOIT9xEON5tuGcDmkRHEx4BoGSNA2q0Zn3HZL3o2Kk9i1ZAfPQdc2kaghjSarFEhcZJnigS11UTcr-pK196gHBP0j2OhoEfs4NWF80n_kETMiBqkRduDLP32Gd3O84EcKc",
    "response": "eyJyZXNwb25zZSI6IiIsInMiOiIiLCJlIjoiYlcxdkNLZyJ9",
    "t": "20219",
    "ct": "20219",
    "bg": "!qK6grqsKAAYeA6U8AABtAQecCAIwwJ1ysti3N7hVShDXuRl2nFqXXI0uznLqUpORHZJVon1ckWGPHvxrNVjr8_cCmXPxTC3s50v9TBIEBoHLudOTBXICYUqWbWMHAEfOsN_DNuXEdZox0rH7fKdFdPEY1R7C97NaUo9hmKgycneOHtvq4hgBrvDg_NVq7HArsg1ETd3ByYeEz4m-qWBoi4gRxlckAzzOd6l7w2BZDAIX7TiJVMIf01regeB4LdcG9lcfXHTCZhCYebnY01KF8LjJq61-RQwe2YL00EyvHYg2atkFfi5EMYp9dfTPzFep6dKgtWmghauC_p-rVL_us7J3xmZycDldnPlG_rOcP0zY5izaqWdWKIfVqMw-ph6IdsS7FhdK9Vumv1OKb9AE1nNiiQjdHfRbTqdU6dTuZ85Wfxc4w4Atv_VgL_HwSz8aFtW8cudYYd6XpnZzyGzqtSSozladgJM2ozn3WQgqjyxLh9chUeNfxR1pHdUB-DdmB6BtmRG6zbcknwwVu8rva77M0XBgbfClt-2gZDwgILZT66mrlWAseVhoyw2X8kOBSqdDZrc2fJpZJ8AmE17n-9kY4S0tkl4Qc4t4ZKi95r-s4R2jla03JxmnSfqi6_h5I_eSnEaSAY_6NJDEfe_WN3Kr18Hpie0ZIB856iLO8ISiNQJ7B3p2RsdNVMuFgvo7CX1FIjg7AjD-UBDSQ2k-t3ELxD8zTCVjpvqBqvLCQ-nmd2brXWOVVECEa56TKqQvFg8kr3vdi8rUAPw_CZnfKfdWgWdMMVqnylIIWo16CfzuVpafmttNyCueqCoT6Qw3s_oUFoBPr3YG4ReZ8QtwSFy6HnI2aAMdbwrol0rTal5CJi3u_Yf_ru65Dnf_UrQaHunOelmCJ-oCVh1FKj5J6is3lmOWw6U2ktFYKhRaWmbU-uu2u4GENS_fSjERW4j5CaomNAerx7tLW0GR1LHNHOhZviygjaQ8mRP4x1Si0mFgWR_jkE1UzIq6fTSXk1iTsVsBaqSH6xoFDdbcdsiFJCRJ2EO8wKZXE80VkKLwjo1-USnbPzrrv5qTPsjhODPnNawZKsLdG25lP8HJU1uODhS-ktc2OYmcAj_oAfQjNhMAxYssB0nKdMXzkW0K4K7bzn2miAx_4HaRLG92_R4iffE2OTsqpNJ8lvyhPejO8emchkw0gUgmcDHZ6lr1TFI0XTjcvDGim9AozXeCr_iZqBYWGpMiWfVOXon1A_rb52QHAVESwIMgespkqFgKnzfrMzeh22am3LsxO5BOX_zrsNu495j66QoXbOhQ7ffPCiygkoV7A4CfET0C22-4MvHaIXLYbmeRVT_PqTnISMuI-Hm4q75wr3tI7ZAscBcTkTXVDtL47IIEkW_VeC1OlWZbpHKIREq__j7EaYHbRU90EZi9fb5eFyD4CSANJyEhIOk3wt1EiwCChXr-kTE0lTGP_ShPqkeoja3oOQZG2gOFWU8U56Cv75KARSz3DW_G2AW64x1Ofem7aCMrwnO7FvYcx9UlktdJiCt0xmyJFzNa-zCPp1MWFvy7KNIEititMULzL4HGy25tDVjLSKPktMCU0XI97q_6RidiErsVduNgozMt377FTrdL2wWMRYlksfm8J2LUeuzojr5ASBanMNRk_egv7BQIMYUCPaEpDRZIfH6T6uFgDBcKBoO3aVWT2WLglXQN6QG6zlKW2kvVqWkrdKN7D3rJTWvct2oOw4_D1aJ6lL4FvPfzaRWLNlnLk9MNMnnG29o_AEI-r7v52MJwObz-rP6T_vVqCKqzhn8zlM1ghcF4yhgCCC_STk9tZSYsS5SkCIa1jcu3_NNssM23plCD0mINdzQZ2cmL63jgvWrpE9FWXdhoRfTGuAaQxKZyMuDxlx2xIhOulw0hVuf_0iLItP8GJru8ftYDy5Frfg7HrVeP3V5cNYjvE-gZj0v9h-rhrrrZp7XIQguU5wvvU02Kj0oEtYNaLul7A_h7U3456Oj_445s-uu_bYsmAxdRlhjj2I1TPKWJ_30gdWdNo8sg7Ioi0WtPGtn5AqiTJsLOZTZFODFp1qWpEtOG17PLAStZNeF54hCPijvVQzjKKDA9mE8PgmtnOf5gasqiG75v-OvTcLK2VCh6wPLdjVfbFcFNaEA3_F8ra5t9Al1-Es1jgVHJSzsq_2yxnklsDf60av2NfdHjwcfivJgJHutr6bLr3fNuj-6mwNEWpMbzKGENu2dvsmklXbETtP6fhkckBmp3fKqyqa0TWHlUGvKbNzP-YHH3MUh60M2O6gQVqCMX1iJ0w_KKfdyNjj2sftUVurwMKa2r7YYq7Iax4OPwrf1fjffrvPC2hBQz-Hc3HCHgPunAHIon2ihIVh9p-BoJzi9QT5DVYqLd4F4LDx6tAmDkyjQI83J7gLHA_gONTR0FsM8uYhCJmJ4VDb-N3MKwikw1gI9hLDn1zf3Dp7aNfeYWCqGPcy8k_NtbFHW0bfmohJ0KnHvc6gXkORakcVCXU2Q8LP1BtFopTkS_Xw7ChpB-r4oheKFGK1zYCoqJiIjVNewpsUZ0fZYXwiAiZLna6zqrSkYcsgQ_dyFlhJT6S0blVOolCl518oBi9kbpTA_Yljy_xTMyFt9DYE9fNM5sFPdo8NhwcaLP1Uc915VGqQ4yzO7oINMb7_3GQ-yGGg8OhBrzAXvOfxb2CEKXl5cODLFkQwuY2RS3C-CvhKSxtaCXpIaLQaqCCGhJzW5x_10Tea67"
}

session = requests.Session()

resp = session.post(auth_url, data=data, headers=headers)
print("hoh")
print(resp.status_code)
print(resp.json())
print(resp.content)
# with open("Zip.html", "w", encoding="utf-8") as file:
#     file.write(resp.text)





@app.route('/')
def hello_world():
    pass

if __name__ == '__main__':
    app.run()

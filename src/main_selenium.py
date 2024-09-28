from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd

# params definition -------------------------------------

chrome_pathexe = r'C:/Users/alencar/Documents/DataScience/chrome_driver/chromedriver-win64/chromedriver.exe'
url = "https://www.caesb.df.gov.br/portal-servicos/app/publico/consultarfaltadagua?execution=e1s1"
elem_xpath = '/html/body/div[4]/div/div/div/main/article/div/section[2]/div[2]/div[3]/div/div[1]/form'

#--------------------------------------------------------

service = Service(executable_path=chrome_pathexe)

options = webdriver.ChromeOptions()
options.add_argument('--hedless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome(service=service, options=options)
wd.get(url)
wd.find_element(By.XPATH, elem_xpath)
time.sleep(1)

html = wd.page_source
time.sleep(1)

table = pd.read_html(html)

table[0].to_csv("data.csv", encoding="utf-8")

wd.quit()
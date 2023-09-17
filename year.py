import time

import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://scholar.google.com/citations?user=hX78XJsAAAAJ&hl=ko&oi=ao'

# 논문 정보 크롤링
response = requests.get(url)
html_text = response.text
html = BeautifulSoup(html_text, 'html.parser')

# 발행 연도 list
year_list = html.find_all("span", {"class": "gsc_oph"})
year = []

for c in year_list:
    year.append(c.find('a').text)

list_len = len(year)
for i in range(list_len):
    print(year[i])
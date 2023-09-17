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

# 논문 제목 list
title_list = html.find_all("td", {"class": "gsc_a_t"})
title = []

for c in title_list:
    title.append(c.find('a').text)

list_len = len(title)
for i in range(list_len):
    print(title[i])
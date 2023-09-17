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

# 논문 저자 & 발행 기관 list
author_list = html.find_all("div", {"class": "gs_gray"})
author_list1 = {""}

author = []
publisher = []
count = 1
for c in author_list:
    if(count%2):
        author.append(c.text)
    else:
        publisher.append(c.text)
    count += 1

list_len = len(author)
for i in range(list_len):
    print(author[i])
print()
for i in range(list_len):
    print(publisher[i])
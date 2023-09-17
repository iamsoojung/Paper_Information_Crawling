import time

import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://scholar.google.com/citations?user=hX78XJsAAAAJ&hl=ko&oi=ao'

# 창 숨기는 옵션 추가
options = webdriver.ChromeOptions()
options.add_argument("headless")
# 구글 드라이버 경로 설정
driverPath = "/home/soojung/PycharmProjects/google_schoolar_crawling/chromedriver"
driver = webdriver.Chrome(driverPath, options=options)
# chromedriver 실행 시 홈페이지 내 데이터 로딩 시간 기다리기 설정
driver.implicitly_wait(2)
driver.get(url=url)
# 스크롤 내리기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.implicitly_wait(5)
# 버튼 클릭
driver.find_element_by_xpath("//*[@id='gsc_bpf_more']/span").click()

# 논문 정보 크롤링
response = requests.get(url)
html_text = response.text
html = BeautifulSoup(html_text, 'html.parser')

title_list = html.find_all("td", {"class": "gsc_a_t"})
info_list = html.find_all("div", {"class": "gs_gray"})

title = []
info = []

for t in title_list:
    title.append(t.find('a').text)
for a in info_list:
    info.append(a.text)

title_len = len(title)
info_len = len(info)
#for i in range(title_len):
#    print(i)
#    print(title[i])

for i in range(info_len):
    print(info[i])
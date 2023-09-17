import requests
import pymysql
from bs4 import BeautifulSoup
from datetime import datetime

def board_write(board, subject, content, mb_id, nickname):
    # MySQL connection 및 cursor를 생성합니다.
    conn = pymysql.connect(host='127.0.0.1', user='sj', password='tnwjd1211', db='homepage', charset='utf8')
    curs = conn.cursor()

    # wr_num을 구한 후 작성글을 INSERT 합니다.
    sql = f"select wr_num from g5_write_{board}"
    curs.execute(sql)
    wr_num = str(int(curs.fetchone()[0]) - 1)
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S') # 그누보드의 날짜 형식 준수 (ex: 2021-04-05 23:45:15)
    sql = f"insert into g5_write_{board} set wr_num = {wr_num}, \
          wr_reply = '', wr_comment = 0, ca_name = '', wr_option = 'html1', wr_subject = '{subject}', \
          wr_content = '{content}', wr_link1 = '', wr_link2 = '', \
          wr_link1_hit = 0, wr_link2_hit = 0, wr_hit = 1, wr_good = 0, wr_nogood = 0, \
          mb_id = '{mb_id}', wr_password = '', wr_name = '{nickname}', wr_email = '', wr_homepage = '', \
          wr_datetime = '{now}', wr_last = '{now}', wr_ip = '111.111.111.111', \
          wr_1 = '', wr_2 = '', wr_3 = '', wr_4 = '', wr_5 = '', \
          wr_6 = '', wr_7 = '', wr_8 = '', wr_9 = '', wr_10 = '', \
          wr_comment_reply = '', wr_facebook_user = '', wr_twitter_user = ''"
    curs.execute(sql)

    # wr_id를 구한 후 부모 아이디에 UPDATE 합니다.
    sql = f"select wr_id from g5_write_{board}"
    curs.execute(sql)
    wr_id = str(curs.fetchall()[-1][0])
    sql = f"update g5_write_{board} set wr_parent = {wr_id} where wr_id = {wr_id}"
    curs.execute(sql)

    # 새 글을 INSERT 합니다.
    sql = f"insert into g5_board_new ( bo_table, wr_id, wr_parent, bn_datetime, mb_id ) values \
          ( '{board}', '{wr_id}', '{wr_id}', '{now}', '{mb_id}' )"
    curs.execute(sql)

    # 게시글을 1 증가시킵니다.
    sql = f"select bo_count_write from g5_board where bo_table = '{board}'"
    curs.execute(sql)
    bo_count_write = str(int(curs.fetchone()[0]))
    sql = f"update g5_board set bo_count_write = {bo_count_write} + 1 where bo_table = '{board}'"
    curs.execute(sql)

    # MySQL connection 닫기
    conn.close()
    return

# 논문 정보 크롤링
url = 'https://scholar.google.com/citations?user=hX78XJsAAAAJ&hl=ko&oi=ao'
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

board = 'free_board'
mb_id = 'soojung'
nickname = 'SJ'

title_len = len(title)
for i in range(title_len):
    subject = title[i]
    content = info[i]
    board_write(board, subject, content, mb_id, nickname)
# 네이트 판 (https://pann.nate.com/)
# 베스트 댓글, 일반 댓글
# https://pann.nate.com/talk/348996118
# import requests
from urllib.request import urlopen  # url 접속
from bs4 import BeautifulSoup

url = 'https://pann.nate.com/talk/348996118'
soup = BeautifulSoup(urlopen(url).read(), 'html.parser')

# 베스트 댓글
print("=== 베스트 댓글 ===")
comment_best = soup.find("div", class_ = "cmt_best")
# print(comment_best.get_text())
comment_best = comment_best.find_all('dd', class_ = "usertxt")
# print(comment_best)
for comment in comment_best:
    print("="*80)
    print(comment.get_text().strip())
print("="*80, "\n")

# 일반 댓글
print("=== 일반 댓글 ===")
commemt_list = soup.find('div', class_ = "cmt_list")
# print(commemt_list.get_text())
commemt_list = commemt_list.find_all('dd', class_ = "usertxt")
# print(commemt_list)
for comment in commemt_list:
    print("="*80)
    print(comment.get_text().strip())
print("="*80, "\n")


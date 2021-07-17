# 멜론(https://www.melon.com/)
import requests
from bs4 import BeautifulSoup

# request = requests.get('https://www.melon.com/chart/index.htm')
# print(request) # <Response [406]> : 헤더정보를 읽을 수 없습니다. 페이지 연결 실패
# https://kkyunstory.tistory.com/95
# 헤더 정보 때문에 웹 사이트 데이터를 가져오지 못하는 경우
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
request = requests.get('https://www.melon.com/chart/index.htm', headers = header)
# print(request)
html = request.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
title = soup.findAll('div', {'class': 'rank01'})
# print(title)
artist = soup.findAll('span', {'class': 'checkEllipsis'})


for i in range(len(title)):
    titles = title[i].text.strip()
    artists = artist[i].text.strip()
    # print(titles)
    # print(artists)
    print('{0:3d}위 {1} - {2}'.format(i+1, artists, titles))


"""
file = open('melonTop100.txt', 'w', -1, 'UTF-8')

for i in range(len(title)):
    titles = title[i].text.strip()
    artists = artist[i].text.strip()
    data = '{0:3d}위 {1} - {2}'.format(i+1, artists, titles)
    file.write(data + '\n')
print("파일 쓰기 완료!!")
file.close()

file = open('melonTop100.txt', 'r', -1, 'UTF-8')
lines = file.readlines()
print("멜론뮤직 TOP 100")
for line in lines:
    print(line, end='')
file.close()
"""
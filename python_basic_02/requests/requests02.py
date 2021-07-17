# 벅스뮤직(https://music.bugs.co.kr/)
import requests
from bs4 import BeautifulSoup

request = requests.get('https://music.bugs.co.kr/chart')
# print(request)
html = request.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
title = soup.findAll('p', {'class':'title'})
# print(title)
artist = soup.findAll('p', {'class':'artist'})
# print(artist)

file = open('bugsTop100.txt', 'w', -1, 'UTF-8')
for i in range(len(title)):
    # strip() : 문자열 앞/뒤의 불필요한 빈 칸을 제거합니다.
    # split() : 인수로 지정된 구분자를 이용해서 문자열을 분리합니다.
    artists = artist[i].text.strip().split('\n')[0]
    # print(artists)
    titles = title[i].text.strip()
    # print(titles)
    data = '{0:3d}위 {1} - {2}'.format(i+1, artists, titles)
    # print(data)
    file.write(data + '\n')
print('파일 쓰기 완료!!')
file.close()

file = open('bugsTop100.txt', 'r', -1, 'UTF-8')
lines = file.readlines()
print('벅스뮤직 TOP 100')
for line in lines:
    print(line, end='')
file.close()


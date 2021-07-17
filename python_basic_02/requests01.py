"""
웹 크롤러(Web Crawler)
자동화된 방법으로 웹에서 다양한 정보를 수집하는 소프트웨어를 말합니다.
html 문서를 파싱하려면 파싱할 웹 사이트의 url에 접속할 때 사용하는 requests 모듈과 url에 접속한 후
파싱에 사용할 BeautifulSoup 모듈을 설치해야 합니다.
open in terminal에서
pip install requests
pip install beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup

def getSubject():
    print("getSubject() 함수 호출!")
    # 파싱된 데이터를 저장해서 리턴시킬 빈 List를 만듭니다.
    subjects = []
    # 파싱할 페이지를 요청합니다.
    request = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    print(request)  # <Response [200]> 정상적인 연결
    # 요청한 페이지 정보 중에서 문자열만 저장합니다.
    html = request.text
    # print(html)
    # BeautifulSoup(파싱할 html소스, 파싱에 사용될 파서) 파서종류 -> html문서(html.parser), xml문서(xml.parser)
    soup = BeautifulSoup(html, 'html.parser')
    print(type(soup))
    # findAll() : 인수로 지정된 모든 태그를 리턴합니다. 결과는 list타입입니다.
    # findAll(tag, attributes) # <태그 속성="값">
    # tag : 파싱할 태그 이름을 씁니다.
    # attributes : {"속성이름":"속성값"} 형태로 사용하며 특정 속성이 지정된 태그만 파싱합니다.
    # <p id="a">안녕하세요.</p>
    # class="클래스값" -> class="클래스값1 클래스값2"
    # <p class="a">안녕하세요</p>
    # <h1 class="a">반갑습니다.</h1>
    # 파싱할 데이터의 범위를 설정합니다.
    divs = soup.findAll('div', {'class':'thrv-columns'})
    # print(divs)
    for div in divs:
        # <div> 태그 내부에 모든 <a> 태그를 읽어옵니다.
        links = div.findAll('a')
        # print(links)
        for link in links:
            # <a> 태그 내부의 텍스트만 읽어와서 리턴할 list에 저장합니다.
            # print(link.text)
            subjects.append(link.text)
    return subjects

if __name__ == '__main__':
    subjects = getSubject()
    # print(subjects)
    # 1. print() 함수에서 출력할 데이터를 , 로 구분하면 , 로 구분된 데이터 사이가 한칸씩 떨어져 출력됩니다.
    print('총', len(subjects), '개의 대화를 찾았습니다.')
    # 2. 따옴표 안에 출력 서식을 지정하고 '%'뒤에 출력할 데이터를 지정하면 C나 JAVA에서 printf() 함수를
    # 사용한 것 처럼 출력됩니다.
    print('총 %d 개의 대화를 찾았습니다.' % len(subjects))
    # 3. 따옴표 안에 출력할 데이터의 위치를 {}로 지정하면 format() 함수의 데이터가 대입되어 출력됩니다.
    print('총 {} 개의 대화를 찾았습니다.'.format(len(subjects)))
    # 4. 2번째 3번째 형식을 섞어서 사용할 수 있습니다.
    print('총 {0:d} 개의 대화를 찾았습니다.'.format(len(subjects)))
    for i in range(len(subjects)):
        print('{0:2d}. {1:s}'.format(i+1, subjects[i]))
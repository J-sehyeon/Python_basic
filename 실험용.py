# 모듈을 읽어 들입니다.
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")   # url은 한 줄로 이어서 입력해야 한다.

# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")

a = 0
# location 태그를 찾습니다.
for location in soup.select("location"):
    print(location)
    a += 1
    if a == 2:
         break
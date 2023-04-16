# 모듈을 읽어 들입니다.
from urllib import request      # request 또한 모듈이다.

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")  # request도 모듈이므로 request 모듈 내부에 있는 urlopen() 함수를 
                                                # request.urlopen() 형태로 사용한다.
output = target.read()  

# 출력합니다.
print(output)

# b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko">
# <head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
# <meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title>

# 실행 결과의 맨 앞에 'b'라는 글자가 있다. 이는 바이너리 데이터(binary data)를 의미한다.
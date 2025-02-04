# 표준 모듈

# 모듈(module)   / import 모듈 이름  / 코드를 분리하고 공유하는 기능     / 표준 모듈(파이썬에 기본적으로 내장되어 있음)과 
# 외부 모듈(다른 사람들이 만들어서 공개한 모듈)로 구분  / 모듈 이름으로 파일을 만들면 오류가 발생한다. ex) random.py

# 모듈 사용의 기본: math 모듈
import math
print(math.sin(1))
print(math.floor(2.5))
print(math.ceil(2.5))
print(math.log(256, 2))
for i in range(5):
    print(round(0.5 + i))   # round() 함수는 파이썬 내장 함수이다.  / 이는 정수부분이 홀수이냐 짝수이냐에 따라 반올림 방법이 다르다.

# from 구문 / from 모듈 이름 import 가져오고 싶은 변수 또는 함수    / 모듈 이름을 함수 앞에 붙이지 않아도 함수를 사용할 수 있도록 한다.
from math import sin, cos, tan, floor, ceil
print(sin(1), cos(1), tan(1), floor(2.5), ceil(2.5))
# 모두 가져오기  / from 모듈 이름 import *   / 다만 이는 식별자 이름에서 충돌이 발생할 수 있다.

# as 구문   / import 모듈 as 사용하고 싶은 식별자   / 모듈의 이름을 변경하여 사용
import math as m

# random 모듈   / import random
# module_random.py

# sys 모듈  / 시스템과 관련된 정보를 가지고 있다.   / 명령 매개변수를 받을 때 많이 사용한다.
# module_sys.py

# os 모듈   / 운영체제와 관련된 기능을 가지고 있다. 
# module_os.py

# datetime 모듈 / 날짜와 관련된 처리
# module_datetime.py, module_datetime_add.py

# time 모듈 / 주로 유닉스 타임을 구하거나 특정 시간 동안 코드 진행을 정지할 때 사용
# module_time.py

# urllib 모듈   / URL을 다루는 라이브러리이다.  / URL이란 'Uniform Resource Locator'를 의미한다.    / 인터넷 주소를 활용할 때 사용
# module_urllib.py

# operator.itemgetter() 함수
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

def 가격추출함수(book):
    return book["가격"] 

print(min(books, key=가격추출함수))                # '가격추출함수'가 무엇인지 함수를 찾아봐야함
print(min(books, key=lambda book: book["가격"]))   # 람다 개념 자체를 모르는 파이썬 개발자들도 존재함
# 이러한 문제가 있어 operator 모듈을 사용한다.
from operator import itemgetter

books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

print("# 가장 저렴한 책")
print(min(books, key=itemgetter("가격")))
print() 
# 외부 모듈 / Beautiful Soup, Flask

# 모듈 설치하기 / pip install 모듈 이름 / window + R 키를 눌러 프로그램 실행 창을 띄우고 cmd 를 입력하면 나타나는 명령 프롬프트 창에서 실행
# pip는 파이썬 패키지 관리 시스템이다.

# 모듈 찾아보기
# 방법 1: 책을 통한 모듈 정보 수집
# 방법 2: 파이썬 커뮤니티를 통한 정보 수집
# 방법 3: 웹서핑    / 'Python'이라는 키워드 옆에 '내가 원하는 것'을 더해서 검색

# Beautiful Soup 모듈    / 웹 페이지 분석 모듈
# beautiful_weather.py

# flask 모듈/ 작은 기능만을 제공하는 웹 개발 프레임워크     / Django는 매우 다양한 기능을 제공하는 웹 개발 프레임워크이다. 
# flask_basic.py
# Flask 코드 실행 방법
# $env:FLASK_APP="파일 이름"    / 명령 프롬프트에서는 set FLASK_APP=파일 이름 으로 입력 
# flask run     / $env:FLASK_APP="Chapter07\Chapter07-2\flask_basic"
# beautiful_flask.py

# 라이브러리(library)와 프레임워크(framework)   / 큰 구분이 없이 사용하지만 확실히 구분하자면 
# 제어 역전(IoC: Inversion of Control)여부에 따라 달라진다. / 라이브러리: 정상적인 제어를 하는 모듈, 프레임워크: 제어 역전이 발생하는 모듈
# 라이브러리    / 개발자가 모듈의 기능을 호출하는 형태의 모듈   / from math import sin 과 같은 형태
# 프레임워크    / 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈    / flask_basic.py 에서 개발자는 함수만 정의하고 
# 이를 Flask 모듈 내부에서 스스로 실행

# 데코레이터    / "@" 로 시작하는 구문을 뜻한다.    / 함수 데코레이터와 클래스 데코레이터가 있다.
# 함수 데코레이터   / 함수에 사용되는 데코레이터이다.   / 함수의 앞뒤에 꾸밀 부가적인 내용, 혹은 반복할 내용을 데코레이터로 정의한다. 
# func_deco.py
# 데코레이터를 사용하면 functools라는 모듈을 사용할 수 있다.

# 모듈을 사져옵니다.
from functools import wraps

# 함수로 데코레이터를 생성합니다.
def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        print("인사가 시작되었습니다.")
        function(*arg, **kwargs)
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()

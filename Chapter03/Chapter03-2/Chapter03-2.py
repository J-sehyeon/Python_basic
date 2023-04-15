# if ~ else 와 elif 구문

# else 조건문의 활용
if "조건":
    "조건이 참일 때 실행할 문장"
else:
    "조건이 거짓일 때 실행할 문장"
# condition04.py

# elif 구문
if "조건A":
    "조건A가 참일 때 실행할 문장"
elif "조건B":
    "조건B가 참일 때 실행할 문장"
elif "조건C":
    "조건C가 참일 때 실행할 문장"  
# ...
else:
    "모든 조건이 거짓일 때 실행할 문장"
# condition05.py
# if 조건문의 효율적 사용    / else 구문과 elif 구문은 이전의 조건이 맞지 않을 때 넘어오는 부분이므로 위에서 이미 한번 비교한 것은 제외하고 작성 
# condition06.py (비효율적), condition07.py (효율적)

# False로 변환되는 값    / None, 숫자 0, 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플 등) 이 외에는 모두 True로 변환
# false_value.py

# pass 키워드    / 프로그래밍의 골격(조건문, 반복문, 함수, 클래스 등)을 만들 때 알고있는 오류를 없애기 위한 도구 / 
# 대신 0을 입력해도 결과는 같은 듯하다. / '곧 개발하겠음'이라는 의미와 유사
if "zero" == 0:
    "빈 줄 삽입"
else:
    "빈 줄 삽입"
# pass_keyword.py, pass_keyword01.py
# raise NotImplementedError: pass는 구현하지 않은 부분의 오류를 발생시키지 않지만, 이는 오류를 강제로 발생시킨다.
# raise_NowImplementedError.py

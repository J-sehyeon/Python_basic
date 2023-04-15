# 불 자료형과 if 조건문

# 불 만들기: 비교 연산자 / ==: 같다, !=: 다르다, <: 작다, >: 크다, <=: 작거나 같다, >=: 크거나 같다  / 불을 만들 때 사용
print(10 == 20)     # 조건식: 10 == 20, 의미: "10과 20은 같다", 결과: False
# 문자열에도 비교 연산자를 적용할 수 있다.
print("apple" < "banana")       # True   / 알파벳 순서로 앞에 있는 것이 작은 값을 갖는다.
print("가방" == "가방", "가방" != "하마", "가방" < "하마", "가방" < "가마")     # True True True False   / 한글은 사전 순서(가나다순)로 앞에
# 있는 것이 작은 값을 갖는다.
x = 25
print(10 < x < 30)      # True
# 불 연산하기: 논리 연산자   / not(아니다): 불을 반대로 전환, and(그리고): 피연산자 두 개가 모두 참일 때 True, 그 외는 False, 
# or(또는): 피연산자 두 개 중에 하나만 참이라도 True, 그 외는 False
    # 단항 연산자와 이항 연산자: 단항 연산자는 피연산자를 한 개, 이항 연산자는 피연산자를 두 개 필요로 한다. / 부호 연산자: 단항 연산자
    # 숫자 연산자: 이항 연산자
# not 연산자(단항 연산자)
print(not True)     # False
print(not False)    # True
# boolean.py
# and 연산자와 or 연산자
T = True
F = False
print(T and T, T and F, F and T, F and F, T or T, T or F, F or T, F or F)

# if 조건문: 조건에 따라 코드 실행의 흐름을 변경(조건 분기)  /   if 불 값이 나오는 표현식 : 
#                                                            ....불 값이 참일 때 실행할 문장    / if문 다음 문장은 4칸 들여쓰기 후 입력
if True:
    print("A")
if False:
    print("B")
# condition.py
# 날짜/시간 활용하기 /import datetime, datetime.datetime.now()   / 모듈 기능
# date.py, date01.py, date02.py, date03.py
# condition01.py, condition02.py, condition03.py


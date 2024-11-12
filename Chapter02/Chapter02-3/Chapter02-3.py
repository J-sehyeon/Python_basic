# 변수와 입력

# 파이썬에서는 변수를 생성하는 그 자체가 사용하겠다고 선언하는 것이다. 변수에는 모든 자료형의 값을 저장할 수 있다.
# 변수는 값을 저장할 때 사용하는 식별자이다. 
# "파이는 원주율을 의미하고 그 값은 3.14159265...이다." = 파이: '변수', 3.141592...: '자료형'
pi = 3.14159265 # pi는 pi를 "사용하겠다"라고 선언하는 것이다.    / =기호는 '같다'는 의미가 아니라 우변의 값을 좌변에 '넣겠다',
# '할당하겠다'를 의미한다.   / 원의 넓이를 구하기 위해 pipi*r**2과 같이 쓸 때에 pi의 구체적인 값을 입력하지는 않는다. 
# 이는 그 안에 있는 값을 쓰겠다는 의미이다. 이처럼 변수 안에 있는 값을 사용하는 것을 "변수 참조"라고 한다. 
pi  # >>> pi
    # 3.14159265
# 변수 = 값: 값을 변수에 할당
# pi는 숫자 자료형에 이름을 붙인 것이므로 숫자 연산을 모두 수행할 수 있다.
pi + 2
pi / 2
pi**pi
# pi + "문자열"_TypeError: unsupported operand type(s) for +: 'float' and 'str'  / operand: 피연산자
# variable.py

# 복합 대입 연산자: 변수를 활용할 때 기존의 연산자와 조합해서 사용할 수 있는 연산자이다. / 자료형에 적용하는 기본 연산자와 =연산자를 함께 사용
# 자료형에는 문자열과 숫자가 있다.
# a += 10 == a = a + 10 
# 숫자에 적용할 수 있는 복합 대입 연산자: +=, -=, *=, /=, %=, **=    / '연산자'= : 숫자 '연산자' 후 대입
number = 100
number += 10
number += 20
number += 30
print("number =",number)    # number = 160
A = 10
A %= 3
print("A =", A) # A = 1
# 문자열 복합 대입 연산자: +=(문자열 연결 후 대입), *=(문자열 반복 후 대입)
string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)    # string: 안녕하세요!!
string *= 2 
print("string:", string)    # string: 안녕하세요!!안녕하세요!!
# string *= "문자열"_TypeError: can't multiply sequence by non-int of type 'str'

# 사용자 입력: input()   / 사용자로부터 데이터를 입력받을 때 사용
input("인사말을 입력하세요> ")  # "인사말을 입력하세요> "라는 문자열이 뜨고 프로그램이 실행 도중에 잠시 멈추는 '블록'상태가 된다. 
string = input("인사말을 입력하세요> ")
print(string)
# 리턴값: input과 같이 함수의 결과로 나오는 값
# input()함수의 입력 자료형
print(type(string)) # string에 숫자를 대입해도 자료형은 문자열로 나온다. 이는 string에 True 나 False와 같은 불(boolean)값을 대입해도 같다.
# 인사말을 입력하세요> 273
# 273
# <class 'str'>

# 캐스트(cast): 객체의 유형을 다른 유형으로 바꾸는 프로그래밍 문법이다.  / 문자열 -> 숫자: int(), float()    / 숫자 -> 문자열: str()
# 문자열을 숫자로 바꾸기 / int("정수"), float("실수")
# int_convert.py, int_float01.py, int_float02.py 
# ValueError 예외
# 1. 숫자가 아닌 것을 숫자로 변환하려고 할 때    / float("안녕하세요")_ValueError: could not convert string to float
# 2. 소수점이 있는 숫자 형식의 문자열을 int()함수로 변환하려고 할 때 / int("52.273")_ValueError: invalid literal for int() with base 10
# 숫자를 문자열로 바꾸기 / str(다른 자료형)
print(type(str(True)), str(True))
# str.py

# inch 단위를 cm 단위로 치환하기
# inch_to_cm.py
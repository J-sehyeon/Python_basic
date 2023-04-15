# 함수 고급

# 튜플   / 함수와 함께 많이 사용되는 리스트와 비슷한 자료형으로, 리스트와 다른 점은 한번 결정된 요소는 바꿀 수 없는 것이다.
# 람다   / 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 공간 낭비라는 생각이 들 때 간단하고 쉽게 선언하는 방법이다.

# 튜플   /(데이터, 데이터, 데이터, ...)
tuple_test = (10, 20, 30)
print(tuple_test[0], tuple_test[1], tuple_test[2])
# tuple_test[0] = 1_TypeError: 'tuple' object does not support item assignment
# 요소를 하나만 가지는 튜플
tuple_one_element = (273, )     # (273) (X) / (273)은 숫자로 인식함
# 괄호 없는 튜플
# tuple_basic.py, tuple_use01.py, tuple_use02.py
# 튜플과 함수    / 여러 개의 값을 리턴하고 할당할 수 있음
# tuple_return.py
# 튜플도 리스트처럼 +와 *연산자 등을 활용할 수 있다.    / 리스트와 의 양상이 같다.
# 튜플을 리턴하는 함수의 예  / enumerate(), divmod()     / divmod() 함수는 몫과 나머지 두 값을 리턴한다.     
a, b = 97, 40
print(divmod(a, b))

# 람다   / lambda 매개변수: 리턴값   / '간단한 함수를 쉽게 선언하는 방법'이다.
# 콜백 함수  / 함수의 매개변수에 사용하는 함수
# func_as_param.py
# map() 함수와 filter() 함수     / map(함수, 리스트), filter(함수, 리스트)   
# map() 함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해 주는 함수이다. 
# filter() 함수는 리스트의 요소를 함수에 넣고 리턴된 값이 true인 것으로, 새로운 리스트를 구성해 주는 함수입니다.
# call_with_func.py, lambda01.py, lambda02.py

# 파일 처리  / 텍스트 파일, 바이너리 파일    / '텍스트 파일'과 관련된 내용만 살펴보겠다.
# 파일 열고 닫기 / 파일이 항상 켜져있는 프로그램일 경우 파일을 닫는 것이 중요하다.
# 파일 열기  / 파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)
# 모드   /w(write), a(append), r(read)   / 새로 쓰기, 뒤에 이어서 쓰기, 읽기 모드
# 파일 닫기  / 파일 객체.close() 
# file_open.py
# with 키워드    / with open(문자열: 파일 경로, 문자열: 모드) as 파일 객체:  / 파일을 열고서 닫지 않는 실수 방지
#                     문장
# file_with.py
# 텍스트 읽기    / 파일 객체.read()
# file_read.py
# 텍스트 한 줄씩 읽기    / CSV, XML, JSON    / CSV는 Comma Separated Values 의 줄임말로, 쉼표로 구분된 값들을 의미한다.
# for 한 줄을 나타내는 문자열 in 파일 객체:
#    처리
# 이름, 키, 몸무게   / 헤더
# 정세현, 177, 75    / 데이터 
# 윤인성, 176, 62    / 데이터
# file_write.pt, file_readlines.py


# 제너레이터(generator) / 이터레이터를 직접 만들 때 사용하는 코드이다.   / 함수 내부에 yield 키워드를 사용하면 해당 함수는 
# 제너레이터 함수가 되며, 함수를 호출해도 함수 내부의 코드가 실행되지 않습니다.  / 실제 사용은 제너레이터 객체를 통해 이루어짐
# generator.py
# 제터레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행한다. 이때 yield 키워드 부분까지만 실행하며,
# next() 함수의 리턴값으로 yield 키워드 뒤에 입력한 값이 출력된다.
# generator01.py
# 제너레이터 객체는 함수의 코드를 조금씩 실행할 때 사용한다. 이는 메모리의 효율성을 위해서이다.
def reverse(x):
    for i in range(len(x)):
        yield x[-i - 1]
list_a = [1, 2, 3, 4, 5, 6]
gen_object = reverse(list_a)             # gen_object 는 제너레이터(reverse() 함수) 객체이다.

for j in range(len(list_a)):
    print(next(gen_object), end="")     # 654321
print()

# 딕셔너리에서의 min() 함수와 max() 함수의 사용  / 두 함수에 '어떤 값으로 비교'할 것인지 나타내는 key라는 키워드 매개변수를 지정할 수 있다.
# func_as_keyparam.py, lambda03.py, lambda04.py

# 스택, 힙   / Frames, objects
# 기본 자료형과 객체 자료형
# 기본 자료형에는 숫자, 문자열, 불이 있다.   / 이 셋을 제외한 자료형들은 모두 객체 자료형이다. (리스트와 딕셔너리가 대표적이다.)
# 스택이란 기본 자료형들이 차곡차곡 정리되어 있는 공간을 말한다. (가볍고 정량화된 자료형이기 때문)
# 힙이란 객체 자료형들이 저장되어 있는 거대한 창고를 말한다.     (무겁고 크기가 정형화되어 있지 않기 때문)
# 파이썬에선 힙에 저장된 자료들을 쉽게 찾기 위해 자료의 위치를 스택에 기록한다. 이 위치를 컴퓨터 과학에서는 
# 0x01, 0x06과 같은 형태의 16진수 숫자로 표현한다. 앞에 붙어 있는 0x는 '이 숫자는 16진수로 특별한 값이다'를 나타낸다.
# 이처럼 창고의 어떤 위치에 저장했는지를 주소 또는 레퍼런스라고 부른다.

# 함수의 값 복사와 레퍼런스 복사
# 함수를 호출할 때 함수 내부 코드를 실행하기 위해 함수 내부의 변수를 저장할 스택을 추가로 만듭니다.
def 함수(b):
    c = 10

a = 10      # 이는 가장 외각에 있는 스택에 저장되는데, 이 스택을 전역 스택(global stack)이라고 한다.
함수(a)     # 전역 스택_a: 10    / 함수 스택_b: 10, c:공란   / a와 b 각각의 스택에 들어있는 변수는 완전 별개의 것이다.
# 기본 자료형 복사
def primitive_change(b):
    b = 20

a = 10

print(a)                # 전역 스택_a: 10    / 함수 스택_b: 10
primitive_change(a)     # 전역 스택_a: 10    / 함수 스택_b: 20
print(a)

# 객체 자료형 복사
def object_change1(d):
    d.append(4)

c = [1, 2, 3]       # 변수 c에 들어있는 값은 힙에 존재하는 리스트의 위치를 나타내는 주소이다.

print(c)            # 전역 스택_c: 0x01  / 힙_0x01: [1, 2, 3]
object_change1(c)   # 전역 스택_c: 0x01  / 함수 스택_d: 0x01 / 힙_0x01: [1, 2, 3, 4]
print(c)            # 전역 스택_c: 0x01  /함수가 종료되면 함수 내부 변수는 더 이상 의미가 없으므로 함수 스택이 사라진다.

def object_change2(f):
    f = [4, 5, 6]

e = [1, 2, 3]   
print(e)            # 전역 스택_e: 0x01  / 힙_0x01: [1, 2, 3]
object_change2(e)   # 전역 스택_e: 0x01  / 함수 스택_f: 0x02 / 힙_0x01: [1, 2, 3], 0x02: [4, 5, 6]
print(e)

# global 키워드  / 1. 함수 내부에서 함수 외부의 변수의 값을 활용한 후(print(a))  2. 스택에 있는 값을 교체하려고 할 때 사용(a = 20)
a = 10

def 함수():
    print(a)
    a = 20

# 함수()_UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
# a는 스택에 저장되어 있고 함수 내부에서 외부에 있는 변수 a의 값을 "활용한 후" "교체"하려 하므로 오류 발생
a = [1, 2, 3, 5]   

def 함수():
    print(a)
    a.append(4)     # 힙에 있는 리스트를 변경하는 것이므로 오류 발생 x

함수()
print(a)

a = [1, 2, 3, 5]   

def 함수():
    print(a)
    a = [4, 5, 6]    

# 함수()_UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
# 스택에 있는 변수 a의 값(주소) 자체를 수정하려 하므로 오류 발생      
print(a)
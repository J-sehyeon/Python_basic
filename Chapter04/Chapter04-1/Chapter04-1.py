# 리스트와 반복문

# 파이썬에서 리스트는 여러가지 자료를 저장할 수 있는 자료를 의미한다.
# 리스트 = [요소, 요소, 요소...], '리스트[숫자] = 요소'에서 숫자는 인덱스(index)라 한다.
# 즉 리스트는 인덱스를 기반으로 값을 저장하는 것이다.
list_a = [273, 32, 103, "문자열", True, False]
print(list_a)       # [273, 32, 103, '문자열', True, False]
print(list_a[0])    # 273
print(list_a[1:3])  # [32, 103]
list_a[0] = "변경"  # 리스트의 특정 요소 변경                
print(list_a)       # ['변경', 32, 103, '문자열', True, False]
# 리스트의 다양한 사용법
# 1. 대괄호 안에 음수를 넣어 뒤에서부터 요소 선택할 수 있다.
print(list_a[-1])   # False
# 2. 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있다.   /  print(list_a[1][1])_TypeError: 'int' object is not subscriptable
# print(list_a[-1][2])_TypeError: 'bool' object is not subscriptable / 정수형과 불 형 요소에는 사용 불가
print(list_a[3])        # 문자열
print(list_a[3][0])     # 문         / "문자열"이라는 문자열에서 0번째("문")를 가져와 출력
# 3. 리스트 안에 리스트를 사용할 수 있다.
list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_a[1])        # [4, 5, 6]
print(list_a[1][1])     # 5
# 리스트에서의 IndexError 예외
list_a = [273, 32, 103]
# print(list_a[3])_IndexError: list index out of range

# 리스트 연결하기    / 연결(+), 반복(*), len()   / 
# len() 함수는 괄호 내부에 문자열을 넣으면 문자열의 길이를 세어 주지만, 리스트 변수를 넣으면 요소의 개수를 세어 준다.
# list01.py, +=_append.py
# 리스트에 요소 추가하기 / append(), insert()    / append()는 추가하려는 요소의 위치를 지정하지 못한다.
# 리스트명.append(요소), 리스트명.insert(위치, 요소)
# list02.py
# 한 번에 여러 요소를 추가할 때에는 extend() 함수를 사용
list_a = [1, 2, 3]
print(list_a.extend([4, 5, 6]))     # none
print(list_a)
# append(), insert(), extend() 함수는 파괴적 함수이다.

# 리스트에서 요소 제거하기   / by 인덱스 or 값
# 인덱스로 제거하기  / del 키워드, pop() / del 리스트명[인덱스], 리스트명.pop(인덱스)
# list03.py
list_b = [0, 1, 2, 3, 4, 5, 6]
list_b.pop()
print(list_b)       # [0, 1, 2, 3, 4, 5]    / pop() 함수의 매개변수에 아무것도 입력하지 않을경우 -1을 입력한 것과 같은 결괏값을 출력한다
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print(list_b)                   # del 키워드는 범위를 지정해 리스트의 요소를 한꺼번에 제거할 수 있다.

    # 리스트 슬라이싱    / 리스트[시작_인덱스:끝_인덱스:단계]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])       # [0, 2, 4]
print(numbers[::-1])        # [8, 7, 6, 5, 4, 3, 2, 1, 0]
del numbers[0:-1:2]
print(numbers)              # [1, 3, 5, 7, 8]
# 값으로 제거하기    / remove()  / 리스트.remove(값)
list_c = [1, 2, 1, 2]
list_c.remove(2)
print(list_c)           # [1, 1, 2]  / remove() 함수는 리스트 내에서 가장 먼저 발견되는 특정 값 하나만을 지운다.
# 모두 제거하기  / clear()
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
print(list_d)               # []

# 리스트 정렬하기    / sort(): 리스트를 오름차순으로 정렬    / 리스트.sort()
list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort()                       
print(list_e)                       # [1, 7, 32, 52, 103, 273, 275]
list_e.sort(reverse=True)           # 내림차순 정렬 
print(list_e)                       # [275, 273, 103, 52, 32, 7, 1]

# 리스트 내부에 있는지 확인하기  / in/not in 연산자  / 값 in 리스트  
list_a = [273, 32, 103, 57, 52]
print(273 in list_a)                # True
print(273 not in list_a)            # False

# for 반복문 / for 반복자 in 반복할 수 있는 것:  / 반복할 수 있는 것에는 문자열, 리스트, 딕셔너리, 범위 등이 있다
#                 코드
for i in range(5):
    print("*")
# for_list.py    / 리스트에 있는 요소 하나하나가 element라는 변수에 들어가며, 차례차례 반복된다.
for character in "안녕하세요":
    print("-", character)
# 중첩 리스트와 중첩 반복문  / 중첩 반복문은 일반적으로 n-차원 처리를 할 때 사용한다.    / 리스트가 n번 겹쳐진 리스트를 n차원 리스트라 한다
# [1, 2, 3]: 1차원 리스트, [[1, 2, 3], [4, 5, 6]]: 2차원 리스트
# 2dlist.py, 2dlist01.py, 2dlist02.py     / 2차원 리스트의 요소를 출력할 때 for반복문을 2번 중첩해서 사용하거나 아래와 같은 방법을 사용한다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number % 3) - 1].append(number)     # 중첩 리스트의 중첩을 해제할 때 사용 가능한 또 다른 방법

print(output)

# 전개 연산자    / *리스트 -> 리스트[0], 리스트[1], ...  / 리스트 내부 또는 함수의 매개변수 위치에 사용  
# 리스트 요소를 하나하나 입력하는 것과 같은 결괏값이 나오게 만든다.
# 리스트 내부에 사용하는 경우
a = [1, 2, 3, 4]
b = [*a, *a]
print(b)            # [1, 2, 3, 4, 1, 2, 3, 4]
a.append(5)
print(a)
b = [1, 2, 3, 4]
c = [*b, 5]         # c = [b, 5] -> c: [[1, 2, 3, 4], 5] / 
                    # 이를 통해 리스트에 요소를 추가할 때 비파괴적으로 구현 가능([1, 2, 3, 4, 5] 라는 리스트를 만들 때에)
print(b)
print(c)
print([*b, 6])
# 함수 매개변수 위치에 사용하는 경우
a = [1, 2, 3, 4]
print(a, *a)

# 범위 자료형과 while 반복문

# 범위(range)와 for 반복문
# 범위   / 정수로 이루어진 범위를 만들 때 사용(실수(float) 입력 불가능)
# 첫째, 매개변수에 숫자를 한 개 넣는 방법
A = 1
range(A)        # A는 숫자   / 0부터 A-1까지의 정수로 범위를 설정
# 둘째, 매개변수에 숫자를 두 개 넣는 방법
B = 1
range(A, B)     # A와 B는 숫자   / A부터 B-1까지의 정수로 범위를 설정
# 셋째, 매개변수에 숫자를 세 개 넣는 방법
C = 1
range(A, B, C)  # A, B, C는 숫자     / A부터 B-1까지의 정수로 범위를 만드는데, 앞뒤의 숫자가 C만큼의 차이를 가집니다.
a = range(5)
print(a)        # range(0, 5)
print(list(range(5)))       # [0, 1, 2, 3, 4]    / list() 함수를 통해 범위를 리스트로 변경하면 범위 내부에 어떤 값이 들어 있는지 확인 가능
print(list(range(5, 10)))       # [5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(range(0, 10, 3)))    # [0, 3, 6, 9]
# 범위를 만들 때 매개변수 내부에 수식을 사용할 수 있다.
a = range(0, 10 + 1)        # 이를 통해 범위가 10을 포함한다는 사실을 강조할 수 있고 수정에 편의성이 있다.
print(list(a))
n = 10
# a = range(0, n / 2)_TypeError: 'float' object cannot be interpreted as an integer
a = range(0, int(n / 2))
b = range(0, n // 2)        # 정수 나누기 연산자가 더욱 많이 사용된다.
print(list(a), list(b))

# for 반복문
# 범위와 함께 사용하기  / for 숫자 변수 in 범위:
#                           코드
# for_range.py
# 리스트와 범위 조합하기
# list_range01.py
# 반대로 반복하기    / range() 함수의 매개변수 세 개 이용, reversed() 함수 이용
# reversed_for01.py, reversed_for02.py

# 중첩 반복문으로 피라미드 만들기
# for_pyramid01.py, for_pyramid02.py

# while 반복문   / while 불 표현식:      / while 반복문에서 가장 중요한 키워드는 조건이다.
#                    문장
# infinite_loop.py
# for 반복문처럼 사용하기
# while_as_for.py    / while 반복문을 사용하는 대표적 예는 무한 반복이다.
# 조건을 활용해서 반복을 사용해야 한다면 while 반복문을 사용하는 것이 좋다.
# 상태를 기반으로 반복하기
# while_with_condition.py
# 시간을 기반으로 반복하기   / 유닉스 타임: 세계 표준시, 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지를 정수로 나타낸 것   /
# import time -> time.time()
# while_with_time.py
# break 키워드/ continue 키워드      / break 키워드: 무한 반복문을 만들고, 내부의 반복을 벗어날 때 사용     /
# continue 키워드: 현재 반복을 생략하고, 다음 반복으로 넘어갈 때 사용
# break.py, break01.py
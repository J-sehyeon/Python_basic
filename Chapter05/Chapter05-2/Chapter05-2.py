# 함수의 활용

# 재귀 함수
# 팩토리얼   / n! = n * (n - 1) * (n - 2) * ... * 1
# 반복문으로 팩토리얼 구하기
# factorial_for.py
# 재귀 함수로 팩토리얼 구하기    / 재귀(recursion)란 '자기 자신을 호출하는 것'을 의미한다.
# factorial(n) = n * factorial(n - 1) (n >= 1 일 때때) 
# factorial_recursion.py
# 재귀 함수의 문제
# 피보나치 수열  / n번째 수열 = (n-1)번째 수열 + (n-2)번째 수열 (초기조건: 1 번째 수열 = 1, 2 번째 수열 = 1)
# fibonacci_recursion01.py, fibonacci_recursion02.py
# fibonacci_recursion01.py 에서의 재귀 함수는 한 번 구했던 값이라도 처음부터 다시 계산해야 하므로 계산 횟수가 기하급수적으로 늘어난다.
# UnboundLocalError에 대한 처리  / fibonacci_recursion02.py 에 'globalr counte'라고 되어있는 부분
# fibonacci_recursion03.py       / 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.   
# 이를 가능케 하기 위해 다음과 같은 구문을 사용한다.     / global 변수 이름      / 함수 내부에서 함수 외부에 있는 변수라는 것을 설명함
# 메모화     / 재귀 함수의 문제는 같은 값을 구하는 연산을 반복하기 때문에 발생. 따라서 같은 값을 한 번만 계산하도록 코드를 수정     
# fibonacci_memo.py      / 딕셔너리를 사용해서 한 번 계산한 값을 저장하는 것을 메모한다고 표현한다.

# 재귀 함수의 깊이   / 재귀함수를 실행했을 때 계속해서 실행되는 것을 방지하고자 재귀함수의 깊이가 설정되어있다.
# recursion_limit.py

# 조기 리턴(early returns)   / if else 구문에서 else 부분을 삭제하여 들여쓰기 단계를 줄임    / 흐름 중간에 return 키워드를 사용하는 것

# 리스트 평탄화하는 재귀 함수 만들기
# list_flatten01.py, list_flatten02.py
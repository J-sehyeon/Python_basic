# 문자열, 리스트, 딕셔너리와 관련된 기본 함수

# 리스트에 적용할 수 있는 기본 함수  / min(), max(), sum()   / 기본함수(리스트)
numbers = [103, 52, 273, 32, 77]
print(min(numbers), max(numbers), sum(numbers))
print(max(103, 52, 273))    # 리스트를 사용하지 않고도 최솟값, 최댓값을 구할 수 있음
# reversed() 함수로 리스트 뒤집기
# reversed.py, reversed_generator.py    / 5장 내용
# enumerate() 함수와 반복문 조합하기
example_list = ["요소A", "요소B", "요소C"]
# 방법 1
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1
# 방법 2
for i in range(len(example_list)):
    print(f'{i}번째 요소는 {example_list[i]}입니다.')
# 이처럼 리스트의 요소를 반복할 때 현재 인덱스가 몇 번째인지 확인할 때 사용하는 함수이다.
# enumerate.py
# 딕셔너리의 items() 함수와 반복문 조합하기  / enumerate():리스트, items():딕셔너리  / 키와 값을 조합
# items.py
# 리스트 내포(list comprehensions)   / 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것(+ if 조건문)]   
# 반복문을 사용하여 리스트를 재조합할 때 사용        
# for_list01.py, list_in.py, array_comprehensions.py
리스트이름 = ["표현식"
    for 반복자 in "반복할수있는것"
    if "조건문"]                    # 리스트 내포 형식의 줄바꿈


# 구문 내부에 여러 줄 문자열을 사용했을 때 문제점
# if_string.py, if_string01.py   
# 여러 줄 문자열은 if 조건문, for 반복문, while 반복문 등의 구문과 사용되지 않는 편이다. 
# 하지만 그렇다고 문자열을 한 줄로 길게 적으면 코드가 복잡하다.
# if_string02.py
# 해결 방법
# 괄호로 문자열 연결하기
# string01.py, string02.py
# 문자열의 join() 함수   / 문자열.join(문자열로 구성된 리스트)
print("::".join(["1", "2", "3", "4", "5"]))
# string03.py

# 이터레이터
# 이터러블(iterable): 반복문의 구문에서 '반복할 수 있는 것', 즉 리스트, 딕셔너리, 문자열, 튜플 등을 칭한다.
# 이터레이터란 이터러블 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 칭한다.
# iterator01.py
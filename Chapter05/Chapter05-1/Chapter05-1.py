# 함수 만들기


# 함수를 사용하는 것을 '함수를 호출한다'고 표현한다. 괄호 내부에 넣는 자료는 매개변수라 부른다. 마지막으로 함수를 호출해서 최정적으로 나오는
# 결과를 리턴값이라 한다.
print(len("안녕하세요"))    # 5      / 5는 len("안녕하세요") 의 리턴값이다.

# 함수의 기본    / 함수는 '코드의 집합'이라 한다.
                            
# 함수를 생성하는 기본 형태      / def 함수 이름():
#                                문장
# fun_basic.py

# 함수에 매개변수 만들기
# print() 함수를 작성할 때 "print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)"와 같이 괄호 안에 많은 것들이 있는데
# 이러한 것들 모두 매개변수이다.
# 매개변수는 다음과 같이 함수를 생성할 때 괄호 내부에 식별자를 입력해서 만든다.  / def 함수 이름(매개변수, 매개 변수, ...)
#                                                                                 문장
# param_basic.py         / parameter: 매개변수
# 매개변수와 관련된 TypeError
# param_basic_error.py
# 가변 매개변수      / def 함수 이름(매개변수, 매개변수, ..., *가변 매개변수):   / 매개변수의 개수가 변할 수 있음
#                        문장
# 제약: "가변 매개변수 뒤에는 일반 매개변수가 올 수 없다." (매개변수간의 구분을 위한 제약), "가변 매개변수는 하나만 사용할 수 있다."
# variable_param.py
# 기본 매개변수
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)에서 가장 앞에 있는 value가 '가변 매개변수'이다.
# 그 뒤에는 일반 매개변수가 올 수 없다. 뒤에 존재하는 매개변수는 기본 매개변수이다. '매개변수=값' 형태로 저장
# 제약: 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# default_param.py       / default: 기본
# 키워드 매개변수    / 매개변수 이름을 지정해서 입력하는 매개변수를 뜻함
# 기본 매개변수가 가변 매개변수보다 앞에 올 때
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")_TypeError: 'str' object cannot be interpreted as an integer
# 맨 앞에 있는 "안녕하세요" 가 n에 들어가고 n은 range() 함수의 매개변수로 들어가므로 오류가 발생한다.   
# 가변 매개변수가 기본 매개변수보다 앞에 올 때
def print_n_times(values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3)   # ["안녕하세요", "즐거운", "파이썬 프로그래밍", 3]을 두 번 출력
# Chapter04-3에서 작성한 infinite_loop.py 에서 'end=""'라 작성한 적이 있는데 이것이 키워드 매개변수이다.
# param_keyword01.py
# 기본 매게변수 중에서 필요한 값만 입력하기
# param_examples.py
# 리턴
# 리턴값 / 함수의 결과
# 자료없이 리턴하기  / return 키워드: 함수가 끝나는 위치를 의미
# return_only.py
# 자료와 함께 리턴하기   / return 자료   
# return_with_data.py
# 아무것도 리턴하지 않기     / None 출력
# return_none.py

# 기본적인 함수의 활용   / def 함수(매개변수):
#                            변수 = 초깃값      / 연산을 해도 변화를 주지 않는 것을 사용    / 이는 로컬 변수로 이 블록 내에서만 사용 가능
#                            여러 가지 처리
#                            여러 가지 처리
#                            return 변수
# sum_all_basic.py
# sum_all_with_default.py





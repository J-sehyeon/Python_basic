# 숫자와 문자열의 다양한 기능   
# 문자열 뒤에 마침표(.)를 입력해 보면 문자열이 가지고 있는 자체적인 기능을 확인할 수 있다.

# 문자열의 format() 함수
# format(): 자료형을 문자열로 변환   / "{}".format(매개변수) / "" 내부의 중괄호({})의 개수와 format() 내부의 매개변수의 개수는 같아야 한다.
"{}".format(10)
"{} {}".format(10, 20)
"{} 안녕 {}".format(1, 1)   # format 함수는 {} 기호를 format의 괄호 안에 있는 매개변수로 대체하는 함수이다.
# format_basic.py, format01.py 
# IndexError 예외
"{} {}".format(1, 2, 3, 4, 5)   # '1 2'
# "{} {} {}".format(1, 2)_# IndexError: Replacement index 2 out of range for positional args tuple / args=arguments, 
                        # tuple: 셀 수 있는 요소들의 순서 있는 열거
# format() 함수의 다양한 기능
# 정수 출력의 다양한 형태    / {:d}: int 자료형 출력을 강제로 지정할 때에 사용
# format02.py, format03.py, format04.py
# 부동 소수점 출력의 다양한 형태 / {:f}: float 자료형 출력을 강제로 지정할 때에 사용
# format05.py, format06.py
# 의미 없는 소수점 제거하기  / {:g}  / 의미없는 0 만을 제거, 다른 숫자는 제거 x
# format07.py

# 대소문자 바꾸기    / upper(), lower()  / 이 두 함수는 a의 문자열을 변화시키지 않는 비파괴적 함수이다.
a = "Hello Pythone Programming...!"
print(a.upper())    # HELLO PYTHONE PROGRAMMING...!
print(a.lower())    # hello pythone programming...!
a.upper()
print(a)            # Hello Pythone Programming...!     / upper() 함수는 해당 문자열을 대문자로 변경한 결과만 보여줄 뿐이다.

# 문자열 양옆의 공백 제거하기(trim)  / strip(), lstrip(), rstrip()
input_a = """
     안녕하세요
문자열 함수를 알아봅니다
"""
print("\n------------------------\n",input_a, "\n------------------------")
print(input_a.strip(), "\n------------------------")
print(input_a.lstrip(), "\n------------------------")
print(input_a.rstrip(), "\n------------------------") 

# 문자열의 구성 파악하기 / isOO()    / Ex) isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인, isidentifier(): 문자열이 식별자로 
# 사용할 수 있는지 확인, isdigit(): 문자열이 숫자로 인식될 수 있는지 확인    / 출력값은 True 또는 False 이다. (boolean)
print("TrainA10".isalnum())     # True   
print("10".isdigit())           # True

# 문자열 찾기    / find(), rfind()   / (왼쪽부터, 오른쪽부터) 특정 문자가 처음 등장하는 위치를 찾는다.
output_a = "안녕안녕하세요".find("안녕")
print(output_a)     # 0
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)     # 2
print("안녕안녕하세요".find("반가워"))      # 해당 문자가 없다면 -1이 출력되는 듯하다.
# 문자열과 in 연산자 /  출력값은 True 또는 False 이다. (boolean)
print("안녕" in "안녕하세요")       # True
print("반가워" in "안녕하세요")     # False

# 문자열 자르기  / split("자르는 기준")    / 실행 결과는 리스트로 나온다.
a = "10 20 30 40 50".split(" ")
print(a)                # ['10', '20', '30', '40', '50']                  
b = "10,20"
print(b.split(","))     # ['10', '20']

# f-문자열: format() 함수를 더 간단하게 사용하는 방법    / f'문자열{표현식}문자열'
print("3 + 4 = {}".format(3 + 4))
print(f'3 + 4 = {3 + 4}')
"{}".format(10)
f'{10}'
f"""1 + 2 = {1 + 2}
2 + 3 = {2 + 3}
3 + 4 = {3 + 4}"""
# 데이터를 리스트에 담아서 사용할 때에는 format() 함수를 사용하는 것이 더 좋다
data = ['별', 2, 'M', '서울특별시 강서구', 'Y']
f"""이름: {data[0]}
나이: {data[1]}
성별: {data[2]}
지역: {data[3]}
중성화 여부: {data[4]}"""           # '이름: 별\n나이: 2\n성별: M\n지역: 서울특별시 강서구\n중성화 여부: Y'
"""이름: {}
나이: {}
성별: {}
지역: {}
중성화 여부: {}""".format(*data)    # '이름: 별\n나이: 2\n성별: M\n지역: 서울특별시 강서구\n중성화 여부: Y'  / *: 전개 연산자(리스트)

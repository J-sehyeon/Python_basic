# 구문 오류와 예외

# 오류의 종류    /1. 구문 오류(syntax error): 프로그램 실행 전에 발생하는 오류   /
# 2. 예외(exception) 또는 런타임 오류(runtime error): 프로그램 실행 중에 발생하는 오류
# 구문 오류  / 괄호의 개수, 들여쓰기 문제 등으로 프로그램이 실행되지도 전에 발생하는 오류이다.   / 프로그램 실행 X
print("# 프로그램이 시작되었습니다!")
# print("# 예외를 강제로 발생시켜 볼게요!)_SyntaxError: unterminated string literal (detected at line 6)
print("# 예외를 강제로 발생시켜 볼게요!")    # 닫는 따옴표로 문자열을 닫아서 해결
# 예외   / 실행 중에 발생하는 오류를 의미한다.   / 프로그램 실행 O
# list_a[1]_NameError: name 'list_a' is not defined
list_a = [1, 2, 3, 4, 5]    # list_a라는 이름을 가진 것을 만들어서 해결
list_a[1]

# 예외를 해결하는 모든 것을 예외 처리(exception handling)라고 부른다.   
# 예외 처리 방법 / 1. 조건문을 사용하는 방법     2. try 구문을 사용하는 방법 / 구문 오류는 문법 문제가 발생한 코드를 수정해야함
# 기본 예외 처리 / 조건문을 사용해서 예외를 처리하는 방법을 말한다.
# 예외가 발생할 수 있는 코드
number_input_a = int(input("정수 입력> "))  # "7센티미터" 입력_ValueError: invalid literal for int() with base 10: '7센티미터'

print("원의 반지름:", number_input_a)
print("원의 둘레:", 2 * 3.14 * number_input_a)
print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# 조건문으로 예외 처리하기
# handle_with_condition.py
# try except 구문    / 조건문만으로 모든 예외 처리 불가능   
try:
    "예외가 발생할 가능성이 있는 코드"
except:
    "예외가 발생했을 때 실행할 코드"
# handle_with_try.py, try_pass.py
# try except else 구문   / "예외가 발생하지 않았을 때 실행할 코드" 지정
# try_except_else.py

# finally 구문   / 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문이다. / 무조건 실행할 때 사용하는 키워드이다.
# try_except_else_finally.py
# try, except, finally 구문의 조합   / 1. try 구문은 단독으로 사용할 수 없으며, 반드시 except 구문 또는 finally 구문과 함께 사용해야 한다.
# 2. else 구문은 반드시 except 구문 뒤에 사용해야 한다.  / 규칙을 지키지 않으면 SyntaxError: Invalid syntax 가 발생한다.
# 파일을 열고 있으면 해당 파일을 이동하거나 덮어 씌우거나 하는 것이 불가능하다. 파일을 열었으면 무조건 닫아야 한다.
# 파일을 제대로 닫았는지는 file 객체의 closed 속성으로 알 수 있다.
# file_closed01.py, file_closed02.py
# finally 키워드를 사용해 파일을 닫는다.
# file_closed03.py
# finally 구문의 필요성
# file_closed04.py
# finally 키워드는 어떤 조건에 무조건 사용해야 하는 게 아니라, finally 키워드를 사용하면 코드가 깔끔해질 것 같다고 생각되는 경우에 사용한다.
# try 구문 내부에서 return 키워드를 사용하는 경우    / finally 구문은 반드시 실행된다.   / 
# 이를 이용해 finally에서 파일을 닫어서 코드를 깔끔하게 한다.
# try_return01.py, try_return02.py
# finally 키워드를 사용한 경우와 사용하지 않은 경우
# try_return03.py, try_return04.py
# 반복문과 함께 사용하는 경우    / break 키워드
# finally_loop.py
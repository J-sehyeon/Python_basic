# 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리합니다.
try:
    # 숫자를 입력받습니다.
    number_input = int(input("정수 입력> "))
    # 리스트의 요소를 출력합니다.
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
#   예외.발생해주세요()         # 이 부분에서 잡지 않은 예외가 발생한다.
except ValueError as exception:
    # ValueError가 발생하는 경우
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)

# 예외가 발생했습니다. NameError
# name '예외' is not defined
#  File "C:\Users\zip23\OneDrive\바탕 화면\Pythone\Chapter06\Chpater06-2\except03.py", line 10, in <module>
#    예외.발생해주세요()         # 이 부분에서 잡지 않은 예외가 발생한다.
#    ^^
# NameError: name '예외' is not defined

# try except 구문을 사용했는데도 프로그램이 죽었다.
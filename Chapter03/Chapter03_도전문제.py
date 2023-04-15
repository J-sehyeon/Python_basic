# 1. 간단한 대화 프로그램
import datetime
now = datetime.datetime.now()

user = input("입력: ")

if user == "안녕" or user == "안녕하세요.":
    print("안녕하세요.")
elif user == "지금 몇 시야?" or user == "지금 몇 시예요?":
    print("지금은 {}시입니다.".format(now.hour))
else:
    print(user)

# 2. 나누어 떨어지는 숫자
X = int(input("정수를 입력해주세요: "))

if X % 2 == 0:
    print("{}은 2로 나누어 떨어지는 숫자입니다.".format(X))
else:
    print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(X))
if X % 3 == 0:
    print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(X))
else:
    print("{}은 3으로 나누어 떨어지는 숫자가 아닙니다.".format(X))
if X % 4 == 0:
    print("{}은 4로 나누어 떨어지는 숫자입니다.".format(X))
else:
    print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(X))
if X % 5 == 0:
    print("{}은 5로 나누어 떨어지는 숫자입니다.".format(X))
else:
    print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(X))

# 2~10의 배수 확인하기 (사람의 방식 구현)
X = input("정수를 입력해주세요: ")

if X[-1] in "02468":
    print("{}은 2의 배수".format(X))

if X == " ":
    raise NotImplementedError

if len(X) <= 1:
    if int(X) % 4 == 0:
        print("{}은 4의 배수".format(X))
elif int(X[-2] + X[-1]) % 4 == 0:
    print("{}은 4의 배수".format(X))

if X[-1] == 0 or X[-1] == 5 or X in "05":
    print("{}은 5의 배수".format(X))



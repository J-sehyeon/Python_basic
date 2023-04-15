# 변수를 선언합니다.
numbers = [5, 15, 6, 20, 7, 25]

# 반복을 돌립니다.
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue        # 만약 number가 10 보다 작다면, 위로 올라가 리스트에서 다음 요소를 불러온다.
    # 출력합니다.
    print(number)
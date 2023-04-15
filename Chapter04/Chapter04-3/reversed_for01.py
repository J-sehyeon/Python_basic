# 역반복문
for i in range(4, 0 - 1, -1):   # 0까지 반복함을 강조하기 위해 0 - 1 사용
    # 출력합니다.
    print("현재 반복 변수: {}".format(i))

    
print(list(reversed(range(4, 0 - 1, -1))))

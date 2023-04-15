temp = reversed([1, 2, 3, 4, 5, 6])

for i in temp:
    print("첫 번째 반복문: {}".format(i))

for i in temp:
    print("두 번째 반복문: {}".format(i))       # 두 번째 반복문 출력 X 

print()

numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers):
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers):                     # 두 번째 반복문 출력 O
    print("두 번째 반복문: {}".format(i))

# reversed() 함수와 반복문을 조합할 때는 함수의 결과를 여러 번 활용하지 않고 다음과 같이 for 구문 내부에 reversed() 함수를 곧바로 넣어서 사용
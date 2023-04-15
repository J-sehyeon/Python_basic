# 3.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# 3.answer   
for number in numbers:
    if number % 2 == 0:
        print(f'{number} 는 짝수입니다.')
    else:
        print(f'{number} 는 홀수입니다.')
for number in numbers:
    print(f'{number} 는 {len(str(number))} 자릿수입니다.')
print()

# 4.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[
        # 4.answer
        (number % 3) - 1
    ].append(number)
print(output)
print()


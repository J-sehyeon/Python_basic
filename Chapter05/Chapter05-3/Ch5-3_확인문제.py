# 1. 
numbers = [1, 2, 3, 4, 5, 6]

# 1.answer
print("::".join(map(str, numbers)))
# print("::".join(numbers))_TypeError: sequence item 0: expected str instance, int found

# 2.
numbers = list(range(1, 10 + 1))

# 2.answer
print("# 홀수만 추출하기")
print(list(filter(lambda x: (x % 2) != 0, numbers)))
print()

print("# 3이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))
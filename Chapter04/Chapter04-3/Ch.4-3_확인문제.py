# 2. 
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}  

# 2.answer
for x in range(4):
    character[key_list[x]] = value_list[x]

print(character)

# 3.
limit = 10000
i = 1

# 3.answer
sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

# 4.
max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    # 4.answer
    a = i
    b = j
    max_value = a * b
    if i * j > (i + 1) * (j - 1):
        break

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# 4.another answer
list_exercise = []

for i in range(1, 100):
    j = 100 - i
    list_exercise.append(i * j)
list_exercise.sort()
print(list_exercise[-1])


  
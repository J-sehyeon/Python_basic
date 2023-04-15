# 2.
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

# 2.answer
print("# 우리 동네 애완 동물들")
for pet in pets:
    print(pet["name"], f'{pet["age"]}살')
print()

# 3.
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

# 3.answer
for number in numbers:
    if counter.get(number) == None:
        counter[number] = 1
    else:
        counter[number] += 1
print(counter)
print()

# 4.
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# 4.answer
for key in character:
    if type(character[key]) == str or type(character[key]) == int:
        print(key, ":", character[key])
    elif type(character[key]) == dict:
        for x in character[key]:
            print(x, ":", character[key][x])
    else:
        for y in character[key]:
            print(key, ":", y)
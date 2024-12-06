# 1. 숫자의 종류
list_a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

output = {}
for i in range(0, 10):
    if i in list_a:
        output[i] = list_a.count(i)
print(("{}에서\n"
"사용된 숫자의 종류는 {}개입니다.\n"
"참고: {}").format(list_a, len(output), output))

# 2. 염기의 개수
DNA = []
input_2 = input("염기 서열을 입력해주세요: ")
for x in input_2:
    DNA.append(x)

for i in "atgc":
    print("{}의 개수: {}".format(i, DNA.count(i)))

# 3. 염기 코돈 개수
DNA = []
input_3 = input("염기 서열을 입력해주세요: ")
for x in input_3:
    DNA.append(x)
T = len(DNA)
Codon = []
output = {}

for i in range(0, int(T/3)):
    Codon.append(str(DNA[3 * i]) + str(DNA[3 * i + 1]) + str(DNA[3 * i + 2])) 
for j in range(0, len(Codon)):
    output[Codon[j]] = Codon.count(Codon[j])
print(output)

# 4. 2차원 리스트 평탄화
list_a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

output = []
for i in range(len(list_a)):
    if type(list_a[i]) == list:
        for j in range(len(list_a[i])):
            output.append(list_a[i][j])
            
    else:
        output.append(list_a[i])

print(f'{list_a}를 평탄화하면\n{output}입니다.')


# 24.12.06
#1. 숫자의 종류
list_1 = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dict_1 = {}
for x in range(len(list_1)):
    if list_1[x] in dict_1:
        dict_1[list_1[x]] += 1
    else:
        dict_1[list_1[x]] = 1
print("""{}에서
사용된 숫자의 종류는 {}개입니다.
참고: {}""".format(list_1, len(dict_1), dict_1))

#2. 염기의 개수
DNA = "ctacaatgtcagtatacccattgcattagccgg"
for x in ["a", "t", "g", "c"]:
    print("{}의 개수: {}".format(x, DNA.count(x)))

#3. 염기 코돈 개수
DNA = "ctacaatgtcagtatacccattgcattagccggaa"
codon = {}

print(DNA)
for x in range(0, (len(DNA) // 3) * 3, 3):
    DNA_list = ""
    for i in range(x, x+3):
        DNA_list += DNA[i]
    if DNA_list in codon:
        codon[DNA_list] += 1
    else:
        codon[DNA_list] = 1
print(f"""염기 서열을 입력해주세요: {DNA}
{codon}""")


#4. 2차원 리스트 평탄화
list_4 = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
list_4_A = []
i = 0
while i < len(list_4):
    if type(list_4[i]) == list:
        list_4_A += list_4[i]
        print(1)
    else:
        list_4_A.append(list_4[i])
        print(2)
    i += 1
print(list_4_A)



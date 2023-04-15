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




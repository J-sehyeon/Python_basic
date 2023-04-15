# 1. 하노이 탑
memo = []
num = 0
def Tower_of_Hanoi(n, st_rod, end_rod, as_rod):
    global num
    if n == 1:
        memo.append(f'{st_rod} -> {end_rod}')
        num += 1
    else:
        Tower_of_Hanoi(n - 1, st_rod, as_rod, end_rod)
        memo.append(f'{st_rod} -> {end_rod}')
        num += 1
        Tower_of_Hanoi(n - 1, as_rod, end_rod, st_rod)

n = int(input("원판의 개수를 입력해주세요: "))

Tower_of_Hanoi(n, "A탑", "B탑", "C탑")  

print("이동 횟수는 {}회입니다.".format(num))

print("\n".join(map(str, memo)))




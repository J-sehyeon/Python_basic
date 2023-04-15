def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)

# 함수를 호출합니다.
print_n_times("기본 매개변수를 입력하지 않는다면")
print_n_times("안녕하세요", 5)
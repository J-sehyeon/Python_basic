def print_n_times(value, n):        # 매개변수 2개 지정
    for i in range(n):
        print(value)

# print_n_times("안녕하세요")    / 매개변수 1개 입력_TypeError: print_n_times() missing 1 required positional argument: 'n'

# print_n_times("안녕하세요", 10, 20)    / 매개변수 3개 입력_TypeError: print_n_times() takes 2 positional arguments but 3 were given

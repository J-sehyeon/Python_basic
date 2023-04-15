# 메모 변수를 만듭니다.
dictionary = {
    1: 1,
    2: 1
}
R_not = 0

# 함수를 선언합니다.
def fibonacci(n):
    global R_not
    if n in dictionary:
        R_not += 1
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    # 본래 'else:' 가 와야하는 자리이다. 하지만 생략할 수 있다. 이를 조기 리턴이라 한다. 
    R_not += 1
        # 메모가 되어 있지 않으면 값을 구함
    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output
    

# 함수를 호출합니다.
print("fibonacci(10):", fibonacci(10), R_not)
print("fibonacci(20):", fibonacci(20), R_not)
print("fibonacci(30):", fibonacci(30), R_not)
print("fibonacci(40):", fibonacci(40), R_not)
print("fibonacci(50):", fibonacci(50), R_not)

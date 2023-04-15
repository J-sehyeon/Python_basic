# 1. f(x) = 2x + 1, f(x) = x^2 + 2x + 1
def f(x):
    return 2 * x + 1
print(f(10))

def f(x):
    return x ** 2 + 2 * x + 1
print(f(10))

# 2. 
def mul(*values):
    # 2. answer
    x=1
    for value in values:
        x *= value
    return x

print(mul(5, 7, 9, 10))

# 3.오류가 발생하는 코드 고르기
def function(*values, valueA, valueB):
    pass
# function(1, 2, 3, 4, 5)_TypeError: function() missing 2 required keyword-only arguments: 'valueA' and 'valueB'
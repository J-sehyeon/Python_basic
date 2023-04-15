a = [1, 2, 3]   
b = [4, 5, 6]   
print(a.append(b))      # None
print("a.append(b):", a)

a = [1, 2, 3]
b = [4, 5, 6]   
# print(a += b)_SyntaxError: invalid syntax
a += b
print("a += b:", a)

a = [1, 2, 3]
b = [4, 5, 6]   
print(a.extend(b))
print("a.extend(b):", a)
# 따라서 += 연산자와 같은 기능을 수행하는 함수는 extend() 이다.
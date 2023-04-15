# 변수를 선언합니다.
numbers = [1, 2, 3, 4, 5, 6]    
r_num = reversed(numbers)

# reversed_numbers를 출력합니다.
print("reversed_numbers :", r_num, reversed(numbers))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))



print(type(numbers))                    # <class 'list'>
print(type(r_num))                      # <class 'list_reverseiterator'>     / reversed() 함수의 리턴값은 이터레이터이다. for 효율성
print(type(reversed({"1": "1"})))       # <class 'dict_reversekeyiterator'> ?

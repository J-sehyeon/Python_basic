# 함수를 선언합니다.
def power(item):
    return item * item
def under_3(item):
    return item < 3

# 변수를 선언합니다.
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수를 사용합니다.
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# map() 함수의 실행 결과
# map(power, list_input_a): <map object at 0x000002710B650100>
# map(power, list_input_a): [1, 4, 9, 16, 25]

# filter() 함수의 실행 결과
# filter(under_3, list_input_a): <filter object at 0x000002710B6503A0>
# filter(under_3, list_input_a): [1, 2]

# <map object> 와 <filter object> 를 제너레이터라 부른다.
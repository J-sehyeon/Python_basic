# 정수
output_a = "{:d}".format(52)                # {:d}: int 자료형의 정수를 출력하겠다고 선언하는 것이다.

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)   # 5칸       # {:숫자d}: '숫자'칸을 빈 칸으로 잡고 뒤에서부터 format() 함수의 숫자를 채운다.
output_c = "{:10d}".format(52)  # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)  # 양수      # 빈칸을 0으로 채우는 형태이다.
output_e = "{:05d}".format(-52) # 음수

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

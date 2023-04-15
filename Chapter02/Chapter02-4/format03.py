output_f = "{:+d}".format(52)   # 양수                   # {:+d}: 양수와 음수 기호 표현 가능
output_g = "{:+d}".format(-52)  # 음수
output_h = "{: d}".format(52)   # 양수: 기호 부분 공백    # 음수만 기호 표현(별로 의미가 없어보임)
output_i = "{: d}".format(-52)  # 음수: 기호 부분 공백    

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)



# 2.
print("{:b}".format(10))                # 1010                          
print("안녕안녕하세요".count("안"))      # 2 

# 2.answer
output = [x for x in range(1, 100 + 1)
    if "{:b}".format(x).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
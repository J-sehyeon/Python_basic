
output = ""

for i in range(1, 15):
    for j in range(0, 14 - i):      # or for j in range (14, i, -1):
        output += " "
    for k in range(0, 2 * i - 1):
        output += "*"
    output += "\n"
print(output)

# 파일을 엽니다.
with open("basic.txt", "r") as file:    # 읽기 모드로 변경함
    # 파일을 읽고 출력합니다.
    contents = file.read()
print(contents, type(contents))
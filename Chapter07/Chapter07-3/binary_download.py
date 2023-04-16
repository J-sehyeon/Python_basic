# 모듈을 읽어 들입니다.
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)   # b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHD . . .    / 맨 앞의 b 는 이것이 바이너리 파일임을 의미한다.

# write binary[바이너리 쓰기]모드로
file = open("Chapter07/Chapter07-3/output.png", "wb")     # 바이너리 형식으로 작성
file.write(output)
file.close()
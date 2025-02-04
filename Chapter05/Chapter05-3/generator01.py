# 함수를 선언합니다.
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
# 함수를 호출합니다
output = test()
# next() 함수를 호출합니다.
print("D 지점 통과")
a = next(output)        # 이 지점에서 test() 함수의 "print("A 지점 통과")"가 호출된다. 그리고 a에는 1이 저장된다.
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")    
#c = next(output)        # StopIteration  / next() 함수를 호출한 이후 yield 키워드를 만나지 못하고 함수가 끝남
#print(c)
# 한 번 더 실행하기
#next(output)
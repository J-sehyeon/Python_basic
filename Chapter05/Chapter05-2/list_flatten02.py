def flatten(data):
    output = []         # output은 계속해서 이어지는 것이 아니라 flatten() 함수를 호출할 때마다 그 안에서 존재하는 리스트이다.
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))
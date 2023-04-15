# 딕셔너리와 반복문

# 리스트가 '인덱스를 기반을 값을 저장하는 것'이라면 딕셔너리는 '키를 기반으로 값을 저장하는 것'이라 할 수 있다.      / 선언 형식: 변수 = {}
{
    "키A": 10,      # 문자열을 키로 사용 
    "키B": 20,
    "키C": 30,
    1:     40,      # 숫자를 키로 사용
    False: 50       # 불을 키로 사용
}
# 딕셔너리는 중괄호{}로 선언하며, 키: 값 형태를 쉼표(,)로 연결해서 만듭니다. / 키에는 문자열, 숫자, 불 등으로 선언할 수 있다.
dict_a = {
    "name": "어벤져스 엔드게임",
    "type": "히어로 무비"       
}   
print(dict_a)
print(dict_a["name"])       # 접근법: 딕셔너리[키]
dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"],
    "실험용": {
        "A": "a",
        "B": "b"
    }
}
print(dict_b)
print(dict_b["director"])
print(dict_b["실험용"]["A"])
# dict01.py
# 딕셔너리의 문자열 키와 관련된 실수
dict_key = {
#   name: "7D 건조 망고", _NameError: name 'name' is not defined    / name이라는 이름이 정의되지 않아 발생한 오류이다.
    type: "당절임"                                                  
}
name = "이름"
dict_key = {
    name: "7D 건조 망고",   # name이라는 이름을 변수로 만들어서 오류 자체는 해결 / 이런 방식은 거의 사용하지 않는다.                
    type: "당절임",
}                           
print(dict_key)             # {'이름': '7D 건조 망고', <class 'type'>: '당절임'} / type은 type() 함수라는 기본 식별자가 있어 오류 발생 X

# 딕셔너리에 값 추가/대체/제거하기   / 딕셔너리[새로운 키] = 새로운 값   
dict_a = {
    "A": "a"
}
dict_a["B"] = "b"
print(dict_a)       # {'A': 'a', 'B': 'b'}   / 새로운 키와 값이 추가됨
dict_a["A"] = "ㄱ"
print(dict_a)       # {'A': 'ㄱ', 'B': 'b'}  / 기존의 값을 대체
del dict_a["A"]
print(dict_a)       # {'B': 'b'}             / del 키워드를 사용하여 기존의 키 제거  -> 해당 요소 제거
# dict02.py, dict03.py
# keyError 예외  / 리스트의 길이를 넘는 인덱스에 접근하면 IndexError가 발생하듯, 딕셔너리도 존재하지 않는 키에 접근하면 KeyError가 발생한다.
dictionary = {} 
# dictionary["key"], del dictionary["key"]_KeyError: 'key'
# 딕셔너리 내부에 키가 있는지 확인하기   / in 키워드, get() 함수     / get() 함수는 존재하지 않는 키에 접근할 때 None을 출력한다.
# key_in.py, get01.py

# for 반복문: 딕셔너리와 함께 사용하기   / for 키 변수 in 딕셔너리:
                                      #     코드
# for_dict.py
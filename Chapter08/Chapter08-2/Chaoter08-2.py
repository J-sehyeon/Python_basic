# 클래스의 추가적인 구문

# 어떤 클래스의 인스턴스인지 확인하기   / isinstance(인스턴스, 클래스)
# 클래스를 선언합니다.
class Student:
    def __init__(self):
        pass

# 학생을 선언합니다.
student = Student()

# 인스턴스 확인하기
print("isinstance(student, Student):", isinstance(student, Student))
    # 상속에 따른 인스턴스 확인
    # 단순한 인스턴스 방법으로는 'type(인스턴스) == 클래스' 이 있다.    / 다만 이 방법은 '상속을 사용할 때' 다르게 동작한다.
    # isinstance_type.py 
    # isinstance() 함수는 상속 관계를 확인하는 반면, type() 함수는 상속 관계를 확인하지 않는다.
# isinstance.py

# 특수한 이름의 메소드  / __<이름>__()
# str_func.py
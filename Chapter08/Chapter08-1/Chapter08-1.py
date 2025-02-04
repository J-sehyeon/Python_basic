# 클래스의 기본

# 객체 지향 프로그래밍(Object Oriented Programming)     / 객체를 우선으로 생각해서 프로그래밍한다는 의미이다.   /
# c를 제외한 모든 프로그래밍 언어는 객체 지향 프로그래밍 언어이다.                    
# 모든 프로그래밍 언어는 클래스 기반의 객체 지향 프로그래밍 언어이다. 이는 클래스라는 것을 기반으로 객체를 만들고, 그러한 객체를 우선으로  
# 생각해서 프로그래밍해야 한다.

# 객체  / 여러 가지 속성을 가질 수 있는 대상
# 학생 성적 관리 프로그램을 만든다면 학생 이름, 학번, 과목별 성적 등이 필요할 것이다.   / 다만 그 개개인의 키, 몸무게, 가족관계 등  
# 학생 성적과 관련이 없는 요소는 필요하지 않을 것이다.
    # 추상화    / 프로그램에서 필요한 요소만을 사용해서 객체를 표현하는 것을 의미한다. 
# object_1_basic.py, object_2_dict.py, object_3_seperate.py
# 여기서 학생이 바로 객체이다. 
# 실행 결과는 세 프로그램 모두 같지만, 점점 더 객체 지향적인 프로그래밍이 되어간다.

# 클래스 선언하기   / class 클래스 이름:        / 클래스는 객체를 조금 더 효율적으로 만들기 위한 기능이다.
#                        클래스 내용
    # 클래스의 이름     / Chapter01의 <식별자> 부분에는 클래스 이름을 지을 때 각 단어의 앞 글자를 대문자로 만들고 이를 합쳐서 이름을 만드는
    # 캐멀 케이스(파스칼 케이스) 규칙을 지켜야 한다는 내용이 있다. 
# 인스턴스(instance)    / 인스턴스 이름(변수 이름) = 클래스 이름()  (ex> ins = Class() )

# 생성자(constructor)   / 클래스 이름과 같은 함수를 칭한다.     / 클래스 내부에 __init__라는 함수를 만들면 객체를 생성할 때 처리할 내용을 
# 작성할 수 있다.   / class 클래스 이름:
#                        def __init__(self, 추가적인 매개변수):
#                            pass
    # self  / 클래스 내부의 함수는 첫 번째 매개변수로 반드시 self를 입력해야 한다.  / 이때 self는 '자기 자신'을 나타내는 딕셔너리이다.
    # self.<식별자> 로 self가 가지고 있는 속성과 기능에 접근한다. (ex>self.name = name)

    # self는 클래스 인스턴스이다.   / 메모리 주솟값이 같다.
    # Class.method() 는 self에 해당하는 인자를 전달하지 않아서 오류가 발생한다.     / ins.method() 오류 X

# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 학생 리스트를 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)    
]

# Student 인스턴스의 속성에 접근하는 방법
print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)

expe = Student("실험용", 0, 0, 0, 0)
print(expe.name)
    # 소멸자(destructor)    / 생성자와 반대로 인스턴스가 소멸될 때 호출되는 함수이다.
    # destructor.py

# 메소드(method)    / 클래스가 가지고 있는 함수를 칭한다.   / 생성자를 선언하는 방법과 똑같다.  / 
# 마찬가지로 첫 번째 매개변수에 self를 넣어야 한다.
# <object_3_seperate.py> 에서 만들었던 함수를 클래스 내부에서 구현
# object_4_class.py
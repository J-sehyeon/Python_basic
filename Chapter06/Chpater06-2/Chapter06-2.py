# 예외 고급

# 예외 객체(exception object)    / try:                                              / 예외 정보가 저장되는 장소이다.
#                                    예외가 발생할 가능성이 있는 구문           
#                                 except 에외의 종류 as 예외 객체를 활용할 변수 이름:
#                                    예외가 발생했을 때 실행할 구문                       
# Exception  / '클래스'이다. / '모든 예외의 어머니'라고 불린다.
# except01.py

# 예외 구분하기  / try:                                  / except 구문을 if 조건문처럼 사용
#                    예외가 발생할 가능성이 있는 구문                       
#                except 예외의 종류A:
#                    예외가 발생했을 때 실행할 구문
#                except 예외의 종류B:
#                    예외가 발생했을 때 실행할 구문
#                except 예외의 종류C:
#                    예외가 발생했을 때 실행할 구문
# except02.py, except_multi.py, except_as.py

# 모든 예외 잡기
# except03.py, except_all.py

# raise 구문 / raise 예외 객체   / 예외를 강제로 발생시키는 기능이다.    / ex) raise NotImplementedError / 
# 원하는 형태의 메시지를 만들기 위해선 예외 클래스를 배워야 한다.
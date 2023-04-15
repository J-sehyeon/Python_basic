# 2. Github 의 TensorFlow 에서 예외를 강제로 발생시키는 raise 구문 찾아보기

raise ValueError("exception in __enter__")
raise TypeError("Expected `name` to be a string; got %r" % (name,))
raise core._status_to_exception(e) from None
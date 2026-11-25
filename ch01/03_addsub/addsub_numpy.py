import numpy as np

# 같은 위치끼리 더한다 (요소별 연산)
a = np.array([7, -4, -6, -6, 12])
b = np.array([-10, 9, -2, 2, -17])

result = a + b
print("a      =", a)
print("b      =", b)
print("a + b  =", result)

# 배열 전체의 합계도 한 줄로 구할 수 있다
print("a의 합계 =", np.sum(a))

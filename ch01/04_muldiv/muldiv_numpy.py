import numpy as np

x = np.array([-6, -8, 45, 23, -24])
y = np.array([7, -5, 9, 4, 6])

print("x * y   =", x * y)        # 요소별 곱셈
print("x / y   =", x / y)        # 요소별 나눗셈 (소수)
print("x // y  =", x // y)       # 요소별 몫
print("x % y   =", x % y)        # 요소별 나머지

# 배열 전체를 한 숫자로 요약하기
print("곱의 합계 :", np.sum(x * y))
print("곱의 평균 :", np.mean(x * y))

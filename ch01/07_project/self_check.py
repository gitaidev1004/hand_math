import numpy as np

# 1번
print("1)", -15 + 8 - (-3))

# 2번
print("2)", (-4) * (-6) / 3)

# 3번 : 단계별로 확인
s1 = 9 - 3          # 괄호
s2 = 2 * s1         # 곱셈
s3 = s2 / 4         # 나눗셈
s4 = 5 + s3         # 덧셈
print("3)", s1, s2, s3, "->", s4)

# 4번
q, r = 37 // 8, 37 % 8
print("4) 몫", q, "나머지", r, "검산", 8 * q + r)

# 5번, 6번
scores = np.array([72, 95, 68, 81, 90])
print("5) 합계", np.sum(scores), "평균", np.mean(scores))
print("6)", scores + 5)

import numpy as np

a = np.array([3, 2])
b = np.array([1, 4])

print("a      =", a)
print("b      =", b)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * 2  =", a * 2, "(스칼라 곱: 방향은 그대로, 길이만 2배)")

# 벡터의 크기 (노름)
v = np.array([3, 4])
manual = (v[0] ** 2 + v[1] ** 2) ** 0.5
print("\n|v| 직접 계산 :", manual)
print("|v| np.linalg :", np.linalg.norm(v))

# 두 점 사이의 거리
A = np.array([1, 1])
B = np.array([4, 5])
diff = B - A
print("\nB - A       :", diff)
print("거리(직접)  :", np.sqrt(np.sum(diff ** 2)))
print("거리(NumPy) :", np.linalg.norm(B - A))

# 3차원 이상에서도 똑같다
p = np.array([80, 90, 70])
q = np.array([60, 85, 95])
print("\n학생1과 학생2의 거리: {:.4f}".format(np.linalg.norm(p - q)))

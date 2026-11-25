import numpy as np
import time

# ---------- 방식 1: 로우 코드 (리스트와 반복문) ----------
start = time.time()
xs = []
ys = []
v = -5.0
while v <= 5.0:
    xs.append(v)
    ys.append(2 * v + 1)
    v = v + 0.001
t1 = time.time() - start

# ---------- 방식 2: NumPy ----------
start = time.time()
x = np.arange(-5, 5.001, 0.001)
y = 2 * x + 1
t2 = time.time() - start

print("로우 코드 점 개수:", len(xs), "소요 시간: {:.4f}초".format(t1))
print("NumPy     점 개수:", len(x), "소요 시간: {:.4f}초".format(t2))
print("첫 값 비교:", ys[0], y[0])
print("끝 값 비교:", round(ys[-1], 6), round(y[-1], 6))

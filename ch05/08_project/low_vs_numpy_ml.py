import numpy as np
import time

rng = np.random.default_rng(0)
N = 200000
x = rng.uniform(0, 10, N)
y = 3.5 * x + 20 + rng.normal(0, 2, N)

# ---------- 로우 코드 ----------
start = time.time()
n = len(x)
sx = sy = 0.0
for i in range(n):
    sx += x[i]
    sy += y[i]
mx, my = sx / n, sy / n
num = den = 0.0
for i in range(n):
    dx = x[i] - mx
    num += dx * (y[i] - my)
    den += dx * dx
a_low, b_low = num / den, my - (num / den) * mx
t_low = time.time() - start

# ---------- NumPy ----------
start = time.time()
dx = x - x.mean()
dy = y - y.mean()
a_np = np.sum(dx * dy) / np.sum(dx ** 2)
b_np = y.mean() - a_np * x.mean()
t_np = time.time() - start

print("데이터 {:,}개".format(N))
print("로우 코드: a={:.6f}, b={:.6f}".format(a_low, b_low))
print("NumPy    : a={:.6f}, b={:.6f}".format(a_np, b_np))
print("두 결과의 차이: {:.10f}".format(abs(a_low - a_np)))
print("속도 비교: 로우 {:.4f}초 / NumPy {:.4f}초".format(t_low, t_np))
print("NumPy가 약 {:.0f}배 빠름".format(t_low / t_np))

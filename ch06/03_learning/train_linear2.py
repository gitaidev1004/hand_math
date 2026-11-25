import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([52, 57, 66, 70, 78], dtype=float)

# 개선 1) 입력을 표준화하면 학습이 훨씬 빨라진다 (제5장 5.6절의 Z-score)
x_mean, x_std = x.mean(), x.std()
y_mean, y_std = y.mean(), y.std()
xs = (x - x_mean) / x_std
ys = (y - y_mean) / y_std

a, b = 0.0, 0.0
lr = 0.1

for step in range(1, 1001):
    error = (a * xs + b) - ys
    a -= lr * 2 * np.mean(error * xs)
    b -= lr * 2 * np.mean(error)
    if step in (1, 10, 100, 1000):
        print("{:>5}회  표준화 공간에서 a={:.4f}, b={:.4f}, MSE={:.6f}".format(
            step, a, b, np.mean(error ** 2)))

# 표준화를 되돌려 원래 단위의 a, b로 변환
a_real = a * y_std / x_std
b_real = y_mean + b * y_std - a_real * x_mean
print("\n원래 단위로 환산: a = {:.4f}, b = {:.4f}".format(a_real, b_real))

dx, dy = x - x.mean(), y - y.mean()
a_exact = np.sum(dx * dy) / np.sum(dx ** 2)
b_exact = y.mean() - a_exact * x.mean()
print("공식의 정답      : a = {:.4f}, b = {:.4f}".format(a_exact, b_exact))
print("오차: a {:.6f}, b {:.6f}".format(abs(a_real - a_exact), abs(b_real - b_exact)))

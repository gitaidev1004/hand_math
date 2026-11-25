import numpy as np

# 경사하강법으로 선형회귀의 a, b를 찾는다 (제5장은 공식으로 구했다)
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([52, 57, 66, 70, 78], dtype=float)

a, b = 0.0, 0.0          # 아무 값에서나 시작
lr = 0.01
n = len(x)

print("회차      a        b       MSE")
print("-" * 40)
for step in range(1, 2001):
    pred = a * x + b                      # 순전파
    error = pred - y                      # 예측 - 실제
    mse = np.mean(error ** 2)             # 손실

    # 기울기 (미분 결과를 적용: MSE를 a, b로 미분하면 아래와 같다)
    grad_a = 2 * np.mean(error * x)
    grad_b = 2 * np.mean(error)

    a -= lr * grad_a                      # 갱신
    b -= lr * grad_b

    if step in (1, 10, 100, 500, 1000, 2000):
        print("{:>5}  {:>7.4f}  {:>7.4f}  {:>8.4f}".format(step, a, b, mse))

print("-" * 40)
print("경사하강법 결과 : a = {:.4f}, b = {:.4f}".format(a, b))

# 제5장의 공식으로 구한 정답과 비교
dx, dy = x - x.mean(), y - y.mean()
a_exact = np.sum(dx * dy) / np.sum(dx ** 2)
b_exact = y.mean() - a_exact * x.mean()
print("공식(최소제곱) : a = {:.4f}, b = {:.4f}".format(a_exact, b_exact))

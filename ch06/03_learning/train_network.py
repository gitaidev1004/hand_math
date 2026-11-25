import numpy as np

# 2층 신경망으로 XOR 문제를 학습한다
# XOR: 두 입력이 다르면 1, 같으면 0  -> 직선으로는 나눌 수 없는 문제
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

rng = np.random.default_rng(42)
W1 = rng.normal(0, 1, (2, 4))      # 입력 2 -> 은닉 4
b1 = np.zeros((1, 4))
W2 = rng.normal(0, 1, (4, 1))      # 은닉 4 -> 출력 1
b2 = np.zeros((1, 1))
lr = 0.5

print("회차      손실(MSE)")
print("-" * 24)
for step in range(1, 10001):
    # ---------- 순전파 ----------
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    pred = sigmoid(z2)

    loss = np.mean((pred - y) ** 2)

    # ---------- 역전파 (연쇄법칙) ----------
    d_pred = 2 * (pred - y) / len(X)          # 손실 -> 출력
    d_z2 = d_pred * pred * (1 - pred)         # 시그모이드 미분
    d_W2 = a1.T @ d_z2
    d_b2 = np.sum(d_z2, axis=0, keepdims=True)

    d_a1 = d_z2 @ W2.T                        # 출력 -> 은닉
    d_z1 = d_a1 * a1 * (1 - a1)
    d_W1 = X.T @ d_z1
    d_b1 = np.sum(d_z1, axis=0, keepdims=True)

    # ---------- 갱신 ----------
    W2 -= lr * d_W2; b2 -= lr * d_b2
    W1 -= lr * d_W1; b1 -= lr * d_b1

    if step in (1, 100, 1000, 5000, 10000):
        print("{:>6}  {:.6f}".format(step, loss))

print("-" * 24)
print("입력      정답   예측     판정")
for i in range(4):
    p = pred[i][0]
    print("{}    {}    {:.4f}    {}".format(X[i], int(y[i][0]), p, int(p >= 0.5)))

import numpy as np

rng = np.random.default_rng(0)

# 두 개의 원형 집단 (직선으로 나눌 수 없는 데이터)
n = 100
angle = rng.uniform(0, 2 * np.pi, n)
inner = np.c_[np.cos(angle), np.sin(angle)] * rng.uniform(0, 1.0, (n, 1))
angle2 = rng.uniform(0, 2 * np.pi, n)
outer = np.c_[np.cos(angle2), np.sin(angle2)] * rng.uniform(2.0, 3.0, (n, 1))

X = np.vstack([inner, outer])
y = np.vstack([np.zeros((n, 1)), np.ones((n, 1))])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 2 -> 8 -> 1 신경망
W1 = rng.normal(0, 1, (2, 8)); b1 = np.zeros((1, 8))
W2 = rng.normal(0, 1, (8, 1)); b2 = np.zeros((1, 1))
lr = 0.1

for step in range(1, 3001):
    z1 = X @ W1 + b1
    a1 = np.tanh(z1)                    # tanh 활성화
    pred = sigmoid(a1 @ W2 + b2)

    loss = -np.mean(y * np.log(pred + 1e-9) +
                    (1 - y) * np.log(1 - pred + 1e-9))      # 교차 엔트로피

    d_z2 = (pred - y) / len(X)
    d_W2 = a1.T @ d_z2
    d_b2 = np.sum(d_z2, axis=0, keepdims=True)
    d_a1 = d_z2 @ W2.T
    d_z1 = d_a1 * (1 - a1 ** 2)         # tanh의 미분
    d_W1 = X.T @ d_z1
    d_b1 = np.sum(d_z1, axis=0, keepdims=True)

    W2 -= lr * d_W2; b2 -= lr * d_b2
    W1 -= lr * d_W1; b1 -= lr * d_b1

    if step in (1, 100, 500, 1500, 3000):
        acc = np.mean((pred >= 0.5) == y)
        print("{:>5}회  손실 {:.4f}  정확도 {:.1%}".format(step, loss, acc))

final = np.mean((pred >= 0.5) == y)
print("\n최종 정확도: {:.1%}".format(final))
print("안쪽 원 샘플 예측:", np.round(pred[:3].ravel(), 4))
print("바깥 원 샘플 예측:", np.round(pred[-3:].ravel(), 4))

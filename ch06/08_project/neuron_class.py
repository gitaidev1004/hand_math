import numpy as np

class Dense:
    """완전연결층 하나"""

    def __init__(self, n_in, n_out, seed=0):
        rng = np.random.default_rng(seed)
        # 초기 가중치는 작은 무작위 값으로 (He 초기화)
        self.W = rng.normal(0, np.sqrt(2.0 / n_in), (n_in, n_out))
        self.b = np.zeros(n_out)

    def forward(self, x):
        return x @ self.W + self.b

    def __repr__(self):
        return "Dense({} -> {}, 파라미터 {}개)".format(
            self.W.shape[0], self.W.shape[1], self.W.size + self.b.size)


def relu(x):
    return np.maximum(0, x)


# 3층 신경망 구성
layer1 = Dense(3, 4, seed=1)
layer2 = Dense(4, 4, seed=2)
layer3 = Dense(4, 1, seed=3)

print("신경망 구조")
for i, l in enumerate([layer1, layer2, layer3], 1):
    print("  {}층: {}".format(i, l))
total = sum(l.W.size + l.b.size for l in [layer1, layer2, layer3])
print("  전체 파라미터: {}개".format(total))

# 순전파
x = np.array([2.0, 3.0, 1.0])
h1 = relu(layer1.forward(x))
h2 = relu(layer2.forward(h1))
out = layer3.forward(h2)

print("\n[순전파 과정]")
print("  입력      :", np.round(x, 3))
print("  1층 출력  :", np.round(h1, 3))
print("  2층 출력  :", np.round(h2, 3))
print("  최종 출력 :", np.round(out, 3))

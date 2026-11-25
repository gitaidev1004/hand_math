import numpy as np

def relu(x):
    return np.maximum(0, x)

# 입력 3개 -> 뉴런 4개인 층
x = np.array([2.0, 3.0, 1.0])

# 가중치 행렬: (입력 3개) x (뉴런 4개)
W = np.array([
    [0.5, -0.3, 0.2, 0.8],      # x1이 각 뉴런으로 가는 가중치
    [-0.2, 0.7, 0.4, -0.5],     # x2
    [0.8, 0.1, -0.6, 0.3],      # x3
])
b = np.array([0.1, -0.2, 0.0, 0.5])    # 뉴런마다 편향 하나씩

z = x @ W + b          # (3,) @ (3,4) -> (4,)
out = relu(z)

print("가중치 행렬 모양:", W.shape, "(입력 3 x 뉴런 4)")
print("가중합 z   :", np.round(z, 3))
print("ReLU 출력  :", np.round(out, 3))

# 뉴런 하나하나 확인 (손 계산과 비교)
print("\n[뉴런별 상세]")
for j in range(4):
    detail = " + ".join("{:.1f}x{:.1f}".format(x[i], W[i, j]) for i in range(3))
    print("  뉴런{}: {} + {:.1f} = {:+.2f} -> {:.2f}".format(
        j, detail, b[j], z[j], out[j]))

# 여러 샘플을 한 번에 처리 (배치 처리)
X = np.array([[2.0, 3.0, 1.0],
              [1.0, 0.0, 2.0],
              [0.5, 1.5, 1.0]])
Z = X @ W + b
print("\n세 샘플 동시 처리 결과 모양:", Z.shape)
print(np.round(relu(Z), 3))

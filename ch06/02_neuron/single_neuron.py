import numpy as np

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 손 계산과 같은 설정
x = np.array([2.0, 3.0, 1.0])        # 입력
w = np.array([0.5, -0.2, 0.8])       # 가중치
b = 0.1                              # 편향

# 1~3단계: 가중합
products = x * w
z = np.sum(products) + b

print("입력 x    :", x)
print("가중치 w  :", w)
print("각각 곱   :", products)
print("곱의 합   :", np.sum(products))
print("편향 더함 : z =", z)

# 내적으로 한 번에 (5.2절의 행렬곱)
z2 = np.dot(x, w) + b
print("내적으로  : z =", z2)

# 4단계: 활성화 함수
print("\nReLU(z)    =", relu(z))
print("Sigmoid(z) = {:.4f}".format(sigmoid(z)))

# 입력이 달라지면
print("\n[다른 입력으로 실험]")
for xi in [np.array([0.0, 5.0, 0.0]), np.array([1.0, 1.0, 1.0])]:
    zi = np.dot(xi, w) + b
    print("  x =", xi, "-> z = {:+.2f}, ReLU = {:.2f}".format(zi, relu(zi)))

import numpy as np

def sigmoid(z):
    """어떤 수든 0과 1 사이로 변환한다"""
    return 1 / (1 + np.exp(-z))

# 손 계산과 비교
for z in [-4, -2, 0, 2, 4]:
    print("σ({:>2}) = {:.4f}".format(z, sigmoid(z)))

print("\nz = 2 손 계산 과정")
print("  e^(-2)      = {:.4f}".format(np.exp(-2)))
print("  1 + e^(-2)  = {:.4f}".format(1 + np.exp(-2)))
print("  1 / 위 값   = {:.4f}".format(1 / (1 + np.exp(-2))))

# 배열에 한 번에 적용
z = np.array([-3, -1, 0, 1, 3])
print("\n배열 입력 :", z)
print("시그모이드:", np.round(sigmoid(z), 4))

# 중요한 성질
print("\nσ(0)        =", sigmoid(0))
print("σ(z)+σ(-z)  =", sigmoid(2) + sigmoid(-2), "(항상 1)")
print("아주 큰 값  =", sigmoid(100))
print("아주 작은 값=", sigmoid(-100))

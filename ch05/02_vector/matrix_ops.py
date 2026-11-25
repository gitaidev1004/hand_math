import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A =\n", A)
print("B =\n", B)
print("\nA + B =\n", A + B)
print("\n요소별 곱 A * B =\n", A * B)
print("\n행렬곱 A @ B =\n", A @ B)
print("\n전치행렬 A.T =\n", A.T)

# 실전: 학생 점수에 과목 가중치 적용하기
scores = np.array([[80, 90, 70],        # 학생1 (국, 영, 수)
                   [60, 85, 95],        # 학생2
                   [75, 70, 80]])       # 학생3
weights = np.array([0.3, 0.3, 0.4])     # 수학 비중이 높은 가중치

total = scores @ weights                # (3,3) @ (3,) -> (3,)
print("\n가중 종합 점수:", total)

# 손 계산 검증 (학생1)
check = 80 * 0.3 + 90 * 0.3 + 70 * 0.4
print("학생1 손 계산 :", check)

# 모양 확인
print("\nscores.shape :", scores.shape)
print("weights.shape:", weights.shape)
print("결과 shape   :", total.shape)

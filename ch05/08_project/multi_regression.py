import numpy as np

# 특징: 공부시간, 출석률(%)   /   레이블: 점수
X = np.array([
    [2, 70], [3, 75], [4, 80], [5, 85], [6, 90],
    [7, 92], [8, 95], [9, 97], [1, 60], [10, 99],
])
y = np.array([55, 62, 68, 75, 82, 85, 90, 94, 48, 97])

# 1) 데이터 분할 (제2장 비례배분)
n_train = int(len(X) * 0.8)
X_train, X_test = X[:n_train], X[n_train:]
y_train, y_test = y[:n_train], y[n_train:]
print("학습 {}개 / 테스트 {}개".format(len(X_train), len(X_test)))

# 2) 절편을 위해 1로 채운 열을 붙인다  ->  y = a1*x1 + a2*x2 + b
ones = np.ones((len(X_train), 1))
A = np.hstack([X_train, ones])

# 3) 최소제곱 해 구하기 (공식을 행렬로 확장한 것)
coef, *_ = np.linalg.lstsq(A, y_train, rcond=None)
a1, a2, b = coef
print("\n회귀식: y = {:.3f}*시간 + {:.3f}*출석률 + {:.3f}".format(a1, a2, b))
print("  공부 1시간 증가 -> {:+.2f}점".format(a1))
print("  출석률 1% 증가  -> {:+.2f}점".format(a2))

# 4) 학습 데이터 성능
pred_train = A @ coef
mse = np.mean((y_train - pred_train) ** 2)
r2 = 1 - np.sum((y_train-pred_train)**2) / np.sum((y_train-y_train.mean())**2)
print("\n[학습] RMSE {:.3f}, R² {:.4f}".format(np.sqrt(mse), r2))

# 5) 테스트 데이터 성능 (본 적 없는 데이터)
A_test = np.hstack([X_test, np.ones((len(X_test), 1))])
pred_test = A_test @ coef
print("[테스트] 실제 {} / 예측 {}".format(y_test, np.round(pred_test, 1)))
print("[테스트] RMSE {:.3f}".format(
    np.sqrt(np.mean((y_test - pred_test) ** 2))))

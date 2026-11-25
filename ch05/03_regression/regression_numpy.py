import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([52, 57, 66, 70, 78])

# 공식을 그대로 한 줄씩
dx = x - x.mean()
dy = y - y.mean()
a = np.sum(dx * dy) / np.sum(dx ** 2)
b = y.mean() - a * x.mean()
print("직접 구현 : a = {:.4f}, b = {:.4f}".format(a, b))

# NumPy의 polyfit 함수 (1차 = 직선)
a2, b2 = np.polyfit(x, y, 1)
print("np.polyfit: a = {:.4f}, b = {:.4f}".format(a2, b2))

# 예측과 평가
pred = a * x + b
resid = y - pred
mse = np.mean(resid ** 2)
print("\n예측값:", np.round(pred, 2))
print("잔차  :", np.round(resid, 2))
print("MSE   : {:.4f}  RMSE: {:.4f}".format(mse, np.sqrt(mse)))

# 결정계수 R² : 모델이 데이터를 얼마나 설명하는가 (1에 가까울수록 좋음)
ss_res = np.sum(resid ** 2)
ss_tot = np.sum((y - y.mean()) ** 2)
r2 = 1 - ss_res / ss_tot
print("R²    : {:.4f}".format(r2))

# 새로운 값 예측
for h in [6, 8, 10]:
    print("{:>2}시간 공부 -> {:.1f}점 예상".format(h, a * h + b))

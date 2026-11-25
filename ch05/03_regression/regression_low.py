# 단순 선형회귀를 기본 문법만으로 구현한다
x = [1, 2, 3, 4, 5]
y = [52, 57, 66, 70, 78]
n = len(x)

# 1단계: 평균
x_mean = sum(x) / n
y_mean = sum(y) / n
print("1단계 평균: x̄ =", x_mean, ", ȳ =", y_mean)

# 2~3단계: 편차의 곱과 제곱의 합
numerator = 0      # 분자: Σ(x-x̄)(y-ȳ)
denominator = 0    # 분모: Σ(x-x̄)²
print("\n2~3단계")
print("  i   x    y    x-x̄    y-ȳ    곱      제곱")
for i in range(n):
    dx = x[i] - x_mean
    dy = y[i] - y_mean
    numerator += dx * dy
    denominator += dx * dx
    print("  {}  {:2}  {:3}  {:5.1f}  {:6.1f}  {:6.2f}  {:5.1f}".format(
        i + 1, x[i], y[i], dx, dy, dx * dy, dx * dx))
print("  합계                        {:6.2f}  {:5.1f}".format(numerator, denominator))

# 4단계: 기울기와 절편
a = numerator / denominator
b = y_mean - a * x_mean
print("\n4단계: a = {:.4f}, b = {:.4f}".format(a, b))
print("회귀식: y = {:.2f}x + {:.2f}".format(a, b))

# 5단계: 예측과 잔차, MSE
print("\n5단계: 예측과 잔차")
sq_sum = 0
resid_sum = 0
for i in range(n):
    pred = a * x[i] + b
    resid = y[i] - pred
    sq_sum += resid ** 2
    resid_sum += resid
    print("  x={}  실제 {:3}  예측 {:6.2f}  잔차 {:+6.2f}".format(
        x[i], y[i], pred, resid))
print("  잔차의 합: {:.10f} (0에 가까워야 함)".format(resid_sum))
print("  MSE : {:.4f}".format(sq_sum / n))
print("  RMSE: {:.4f}".format((sq_sum / n) ** 0.5))

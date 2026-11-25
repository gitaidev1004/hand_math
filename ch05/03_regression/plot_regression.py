import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([52, 57, 66, 70, 78, 80, 89, 95])

a, b = np.polyfit(x, y, 1)
pred = a * x + b
resid = y - pred

print("회귀식: y = {:.3f}x + {:.3f}".format(a, b))
print("MSE   : {:.4f}".format(np.mean(resid ** 2)))
print("R²    : {:.4f}".format(1 - np.sum(resid**2) / np.sum((y - y.mean())**2)))

plt.figure(figsize=(10, 4))

# 왼쪽: 데이터와 회귀 직선
plt.subplot(1, 2, 1)
plt.scatter(x, y, color="steelblue", s=40, zorder=3, label="data")
xs = np.linspace(0, 9, 50)
plt.plot(xs, a * xs + b, color="red", label="y={:.2f}x+{:.2f}".format(a, b))
for xi, yi, pi in zip(x, y, pred):
    plt.plot([xi, xi], [yi, pi], color="orange", linestyle=":")
plt.legend(fontsize=8); plt.grid(True, alpha=0.3)
plt.xlabel("study hours"); plt.ylabel("score"); plt.title("Regression Line")

# 오른쪽: 잔차 그래프 (패턴이 없어야 좋은 모델)
plt.subplot(1, 2, 2)
plt.scatter(x, resid, color="green", s=40)
plt.axhline(0, color="black", linewidth=0.8)
plt.grid(True, alpha=0.3)
plt.xlabel("study hours"); plt.ylabel("residual"); plt.title("Residual Plot")

plt.tight_layout()
plt.savefig("regression.png", dpi=150, bbox_inches="tight")
print("regression.png 저장 완료")

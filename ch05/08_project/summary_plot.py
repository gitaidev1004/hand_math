import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
rng = np.random.default_rng(7)

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

# 1) 회귀
x = np.arange(1, 11)
y = 6.2 * x + 45 + rng.normal(0, 3, 10)
a, b = np.polyfit(x, y, 1)
axes[0, 0].scatter(x, y, color="steelblue")
axes[0, 0].plot(x, a * x + b, color="red")
axes[0, 0].set_title("1. Regression (y={:.2f}x+{:.2f})".format(a, b))

# 2) 분류
xc = np.linspace(0, 12, 100)
axes[0, 1].plot(xc, 1 / (1 + np.exp(-(1.2 * xc - 7))), color="purple")
axes[0, 1].axhline(0.5, color="red", linestyle="--")
axes[0, 1].set_title("2. Classification (sigmoid)")

# 3) 군집화
pts = np.vstack([rng.normal([2, 2], 0.6, (20, 2)),
                 rng.normal([7, 7], 0.6, (20, 2)),
                 rng.normal([2, 7], 0.6, (20, 2))])
centers = np.array([[2, 2], [7, 7], [2, 7]], dtype=float)
d = np.linalg.norm(pts[:, None, :] - centers[None, :, :], axis=2)
lab = d.argmin(axis=1)
for k, c in enumerate(["tab:blue", "tab:orange", "tab:green"]):
    axes[1, 0].scatter(pts[lab == k][:, 0], pts[lab == k][:, 1], s=15, color=c)
axes[1, 0].scatter(centers[:, 0], centers[:, 1], marker="X", s=120, color="red")
axes[1, 0].set_title("3. Clustering (K-Means)")

# 4) 이상치 탐지
data = np.concatenate([rng.normal(50, 4, 40), [85, 12]])
z = (data - data.mean()) / data.std()
axes[1, 1].scatter(range(len(data)), data, c=np.where(np.abs(z) > 2, "red", "steelblue"))
axes[1, 1].axhline(data.mean(), color="green")
axes[1, 1].set_title("4. Anomaly Detection (Z-score)")

for ax in axes.flat:
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("ml_summary.png", dpi=150, bbox_inches="tight")
print("ml_summary.png 저장 완료")
print("회귀식 y = {:.2f}x + {:.2f} (원래 규칙 y = 6.2x + 45)".format(a, b))
print("이상치로 탐지된 값:", np.round(data[np.abs(z) > 2], 1))

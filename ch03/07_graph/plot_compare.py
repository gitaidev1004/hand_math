import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-4, 4, 100)

plt.figure(figsize=(10, 4))

# 왼쪽: 기울기만 다른 경우
plt.subplot(1, 2, 1)
for a in [0.5, 1, 2, -1]:
    plt.plot(x, a * x, label="y = {}x".format(a))
plt.axhline(0, color="black", lw=0.8); plt.axvline(0, color="black", lw=0.8)
plt.grid(True, alpha=0.3); plt.legend(fontsize=8)
plt.title("Different Slopes")

# 오른쪽: 절편만 다른 경우
plt.subplot(1, 2, 2)
for b in [-2, 0, 3]:
    plt.plot(x, x + b, label="y = x + ({})".format(b))
plt.axhline(0, color="black", lw=0.8); plt.axvline(0, color="black", lw=0.8)
plt.grid(True, alpha=0.3); plt.legend(fontsize=8)
plt.title("Different Intercepts")

plt.tight_layout()
plt.savefig("compare_graph.png", dpi=150, bbox_inches="tight")

# 값으로도 확인
print("x = 2 일 때")
for a in [0.5, 1, 2, -1]:
    print("  y = {}x  ->  {}".format(a, a * 2))

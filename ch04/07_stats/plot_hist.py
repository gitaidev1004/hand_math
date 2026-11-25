import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
rng = np.random.default_rng(1)

uniform = rng.uniform(0, 10, 5000)
normal = rng.normal(5, 1.5, 5000)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(uniform, bins=20, color="skyblue", edgecolor="black")
plt.title("Uniform Distribution")
plt.xlabel("value"); plt.ylabel("count")

plt.subplot(1, 2, 2)
plt.hist(normal, bins=30, color="lightgreen", edgecolor="black")
plt.axvline(normal.mean(), color="red", linestyle="--", label="mean")
plt.axvline(normal.mean() + normal.std(), color="orange", linestyle=":")
plt.axvline(normal.mean() - normal.std(), color="orange", linestyle=":")
plt.title("Normal Distribution")
plt.xlabel("value"); plt.legend()

plt.tight_layout()
plt.savefig("distributions.png", dpi=150, bbox_inches="tight")

print("균등분포 평균 {:.3f} 표준편차 {:.3f}".format(uniform.mean(), uniform.std()))
print("정규분포 평균 {:.3f} 표준편차 {:.3f}".format(normal.mean(), normal.std()))
print("distributions.png 저장 완료")

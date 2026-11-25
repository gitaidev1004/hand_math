import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False
rng = np.random.default_rng(5)

hours = np.arange(1, 21)                            # 공부 시간
scores = 3.2 * hours + 45 + rng.normal(0, 4, 20)    # 점수(약간의 잡음 포함)
scores = np.clip(scores, 0, 100)                    # 0~100 범위로 자르기

r = np.corrcoef(hours, scores)[0, 1]
print("상관계수: {:.4f}".format(r))
print("공부 시간 평균 {:.1f}시간, 점수 평균 {:.1f}점".format(
    hours.mean(), scores.mean()))

plt.figure(figsize=(6, 4))
plt.scatter(hours, scores, color="steelblue", s=35)
plt.title("Study Hours vs Score (r = {:.2f})".format(r))
plt.xlabel("study hours"); plt.ylabel("score")
plt.grid(True, alpha=0.3)
plt.savefig("scatter.png", dpi=150, bbox_inches="tight")
print("scatter.png 저장 완료")

# 관계의 강도를 말로 해석
if abs(r) >= 0.7:
    strength = "강한"
elif abs(r) >= 0.3:
    strength = "보통의"
else:
    strength = "거의 없는"
direction = "양의" if r > 0 else "음의"
print("해석: {} {} 상관관계".format(strength, direction))

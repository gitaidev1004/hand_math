import numpy as np
import matplotlib
matplotlib.use("Agg")          # 화면 없이 파일로 저장할 때 사용
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

# 1) 데이터 준비
x = np.linspace(-5, 5, 100)
y = 2 * x + 1

# 2) 그래프 그리기
plt.figure(figsize=(6, 4))
plt.plot(x, y, color="blue", linewidth=2, label="y = 2x + 1")

# 3) 축과 격자
plt.axhline(0, color="black", linewidth=0.8)    # x축
plt.axvline(0, color="black", linewidth=0.8)    # y축
plt.grid(True, alpha=0.3)

# 4) 특정 점 표시
plt.plot(0, 1, "ro")                            # 절편 (0, 1)
plt.annotate("y절편 (0, 1)", xy=(0, 1), xytext=(1, -3),
             arrowprops=dict(arrowstyle="->"))

# 5) 꾸미기
plt.xlabel("x"); plt.ylabel("y")
plt.title("Linear Function")
plt.legend()

# 6) 저장
plt.savefig("line_graph.png", dpi=150, bbox_inches="tight")
print("line_graph.png 저장 완료")

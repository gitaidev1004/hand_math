import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

def make_line(a, b, start=-5, end=5, points=100):
    """y = ax + b 의 x, y 데이터를 만든다"""
    x = np.linspace(start, end, points)
    return x, a * x + b

def show_table(a, b):
    """정수 x에 대한 표를 출력한다"""
    print("y = {}x + {}".format(a, b))
    print("  x :", end="")
    for x in range(-3, 4):
        print("{:>6}".format(x), end="")
    print("\n  y :", end="")
    for x in range(-3, 4):
        print("{:>6}".format(a * x + b), end="")
    print()

# 세 개의 함수를 표와 그래프로 비교
settings = [(2, 1), (-1, 4), (0.5, -2)]

plt.figure(figsize=(6, 4))
for a, b in settings:
    show_table(a, b)
    x, y = make_line(a, b)
    plt.plot(x, y, label="y = {}x + {}".format(a, b))
    print()

plt.axhline(0, color="black", lw=0.8); plt.axvline(0, color="black", lw=0.8)
plt.grid(True, alpha=0.3); plt.legend(fontsize=9)
plt.title("Function Graph Tool")
plt.savefig("graph_tool.png", dpi=150, bbox_inches="tight")
print("graph_tool.png 저장 완료")

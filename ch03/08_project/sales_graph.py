import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

months = np.array([1, 2, 3, 4, 5, 6])
sales = np.array([120, 135, 128, 150, 165, 180])

# 1) 첫 달과 마지막 달을 잇는 직선 (가장 단순한 추세선)
a = (sales[-1] - sales[0]) / (months[-1] - months[0])
b = sales[0] - a * months[0]
print("두 점을 지나는 직선: y = {:.1f}x + {:.1f}".format(a, b))

trend = a * months + b
print("실제값:", sales)
print("직선값:", np.round(trend, 1))
print("차이  :", np.round(sales - trend, 1))

# 2) 7월 예측
july = a * 7 + b
print("\n7월 예측 매출: {:.1f}만원".format(july))

# 3) 그래프
plt.figure(figsize=(6, 4))
plt.plot(months, sales, "o-", label="actual sales")
plt.plot(months, trend, "r--", label="trend line")
plt.plot(7, july, "g*", markersize=12, label="prediction")
plt.grid(True, alpha=0.3); plt.legend()
plt.xlabel("month"); plt.ylabel("sales")
plt.title("Monthly Sales and Trend")
plt.savefig("sales_graph.png", dpi=150, bbox_inches="tight")
print("sales_graph.png 저장 완료")

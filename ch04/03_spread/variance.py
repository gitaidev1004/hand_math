import numpy as np

data = [60, 70, 80, 90, 100]

# ---------- 로우 코드: 다섯 단계를 그대로 구현 ----------
n = len(data)
mean = sum(data) / n                               # 1단계
devs = [x - mean for x in data]                    # 2단계
sq = [d ** 2 for d in devs]                        # 3단계
variance = sum(sq) / n                             # 4단계
std = variance ** 0.5                              # 5단계

print("[로우 코드]")
print("  평균      :", mean)
print("  편차      :", devs)
print("  편차의 합 :", sum(devs), "(항상 0)")
print("  편차 제곱 :", sq)
print("  분산      :", variance)
print("  표준편차  : {:.4f}".format(std))

# ---------- NumPy ----------
arr = np.array(data)
print("[NumPy]")
print("  분산(n)     :", np.var(arr))
print("  표준편차(n) : {:.4f}".format(np.std(arr)))
print("  분산(n-1)   :", np.var(arr, ddof=1))
print("  표준편차(n-1): {:.4f}".format(np.std(arr, ddof=1)))

# 흩어짐이 다른 두 데이터 비교
a = np.array([78, 80, 80, 82, 80])
b = np.array([40, 60, 80, 100, 120])
print("\nA: 평균 {:.1f}, 표준편차 {:.2f}".format(a.mean(), a.std()))
print("B: 평균 {:.1f}, 표준편차 {:.2f}".format(b.mean(), b.std()))

import numpy as np

names = ["노트", "볼펜", "지우개", "파일"]
prices = [1200, 800, 500, 2500]        # 단가
counts = [3, 5, 2, 1]                  # 수량

# ---------- 로우 코드 ----------
total = 0
for i in range(len(names)):
    amount = prices[i] * counts[i]     # 품목별 금액
    total = total + amount
    print(names[i], ":", prices[i], "원 x", counts[i], "개 =", amount, "원")
print("합계(로우 코드):", total, "원")

# ---------- NumPy ----------
p = np.array(prices)
c = np.array(counts)
amounts = p * c                        # 품목별 금액을 한 번에
print("품목별 금액:", amounts)
print("합계(NumPy)   :", np.sum(amounts), "원")

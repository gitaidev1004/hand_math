import numpy as np

names = ["키보드", "마우스", "모니터", "USB허브"]
prices = np.array([89000, 32000, 245000, 18000])
rates = np.array([0.10, 0.15, 0.20, 0.05])     # 상품별 할인율

discounts = prices * rates              # 할인액
pays = prices - discounts               # 할인 후 금액

print("품목      정가      할인율   할인액    결제액")
print("-" * 48)
for i in range(len(names)):
    print("{:8s} {:>8,.0f} {:>7.0%} {:>8,.0f} {:>9,.0f}".format(
        names[i], prices[i], rates[i], discounts[i], pays[i]))

print("-" * 48)
total = np.sum(pays)
print("합계 결제액 : {:,.0f} 원".format(total))
print("총 할인액   : {:,.0f} 원".format(np.sum(discounts)))
print("평균 할인율 : {:.1%}".format(np.sum(discounts) / np.sum(prices)))

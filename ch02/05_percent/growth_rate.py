import numpy as np

# 6개월 매출 (단위: 만원)
sales = np.array([120, 135, 128, 150, 165, 180])
months = ["1월", "2월", "3월", "4월", "5월", "6월"]

# 전월 대비 변화율 = (이번달 - 지난달) / 지난달
prev = sales[:-1]        # 1~5월 (마지막 제외)
curr = sales[1:]         # 2~6월 (처음 제외)
rates = (curr - prev) / prev

print("전월 대비 변화율")
for i in range(len(rates)):
    print(" ", months[i + 1], ": {:+.1%}".format(rates[i]))

# 전체 기간 증가율
total_rate = (sales[-1] - sales[0]) / sales[0]
print("1월 대비 6월 증가율: {:+.1%}".format(total_rate))

# 평균 월 성장률(단순 평균)
print("월 평균 변화율: {:+.2%}".format(np.mean(rates)))

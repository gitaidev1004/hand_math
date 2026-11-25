import numpy as np

months = np.arange(1, 13)
sales = np.array([120, 135, 128, 150, 165, 180,
                  210, 230, 190, 170, 155, 200])

print("월별 판매량:", sales)
print("연간 합계  :", np.sum(sales))
print("월 평균    : {:.1f}".format(np.mean(sales)))
print("표준편차   : {:.2f}".format(np.std(sales)))

best = int(np.argmax(sales))
worst = int(np.argmin(sales))
print("\n최고 매출: {}월 ({})".format(months[best], sales[best]))
print("최저 매출: {}월 ({})".format(months[worst], sales[worst]))

# 전월 대비 증감
diff = np.diff(sales)              # 이웃한 값의 차이
print("\n전월 대비 증감:", diff)
print("상승한 달 수:", np.sum(diff > 0), "/ 하락한 달 수:", np.sum(diff < 0))

# 상반기와 하반기 비교
first, second = sales[:6], sales[6:]
print("\n상반기 평균: {:.1f} (표준편차 {:.2f})".format(first.mean(), first.std()))
print("하반기 평균: {:.1f} (표준편차 {:.2f})".format(second.mean(), second.std()))
print("증가율: {:+.1%}".format((second.mean() - first.mean()) / first.mean()))

# 월과 판매량의 상관
print("\n월-판매량 상관계수: {:+.4f}".format(np.corrcoef(months, sales)[0, 1]))

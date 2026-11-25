import numpy as np

sales = np.array([120, 135, 128, 150, 165, 180])     # 1~6월 (만원)

# 1) 전월 대비 변화율과 배율
rates = (sales[1:] - sales[:-1]) / sales[:-1]
factors = sales[1:] / sales[:-1]          # 배율 = 1 + 변화율

print("변화율:", np.round(rates, 4))
print("배율  :", np.round(factors, 4))

# 2) 단순 평균 (틀린 방법)
simple = np.mean(rates)
print("단순 평균 변화율 : {:.2%}".format(simple))

# 3) 기하평균 (올바른 방법)
n = len(factors)
geo_factor = np.prod(factors) ** (1 / n)      # 곱한 뒤 n제곱근
geo_rate = geo_factor - 1
print("기하평균 변화율  : {:.2%}".format(geo_rate))

# 4) 검증: 각 평균을 5번 적용하면?
print("단순 평균 적용 결과 :", round(sales[0] * (1 + simple) ** n, 1))
print("기하평균 적용 결과 :", round(sales[0] * geo_factor ** n, 1))
print("실제 6월 매출      :", sales[-1])

# 5) 로그를 이용한 같은 계산
log_mean = np.mean(np.log(factors))
print("로그 평균으로 구한 배율:", round(np.exp(log_mean), 6))

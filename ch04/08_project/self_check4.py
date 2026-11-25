import numpy as np

data = np.array([4, 8, 6, 10, 2])

print("1) 평균 {:.1f}, 중앙값 {:.1f}".format(data.mean(), np.median(data)))
print("2) 분산 {:.1f}, 표준편차 {:.4f}".format(data.var(), data.std()))
print("3) 주사위 3 이하 확률:", 3 / 6)

# 4) 정규분포에서 평균 +-2표준편차 비율 확인
rng = np.random.default_rng(1)
sample = rng.normal(70, 10, 100000)
inside = np.sum((sample >= 50) & (sample <= 90)) / 100000
print("4) 50~90 사이 비율: {:.2%}".format(inside))

print("5) -0.85 -> 강한 음의 상관")
print("6) 평균 > 중앙값 -> 큰 쪽에 이상치 또는 치우친 분포")

# 손 계산 검증: 편차 제곱의 합
devs = data - data.mean()
print("\n편차      :", devs)
print("편차의 합 :", devs.sum())
print("편차 제곱합:", np.sum(devs ** 2), "-> 분산", np.sum(devs ** 2) / len(data))

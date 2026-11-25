import numpy as np

# 서버 CPU 사용률(%) 측정값
usage = np.array([42, 45, 41, 44, 43, 46, 40, 44, 95, 43, 45, 42, 8, 44])

mean, std = usage.mean(), usage.std()
print("평균 {:.2f}, 표준편차 {:.2f}".format(mean, std))
print("정상 범위(평균 ±3σ): {:.2f} ~ {:.2f}".format(mean - 3*std, mean + 3*std))

z = (usage - mean) / std
print("\n번호  측정값   Z-score   판정")
print("-" * 36)
for i in range(len(usage)):
    verdict = "이상치!" if abs(z[i]) > 2 else "정상"
    print("{:>3}  {:>6}  {:>+8.3f}   {}".format(i, usage[i], z[i], verdict))

outliers = usage[np.abs(z) > 2]
print("-" * 36)
print("탐지된 이상치:", outliers)

# 이상치를 뺀 뒤 통계가 어떻게 변하는가
clean = usage[np.abs(z) <= 2]
print("\n제거 전: 평균 {:.2f}, 표준편차 {:.2f}".format(usage.mean(), usage.std()))
print("제거 후: 평균 {:.2f}, 표준편차 {:.2f}".format(clean.mean(), clean.std()))

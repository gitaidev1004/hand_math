import numpy as np

rng = np.random.default_rng(2024)

# 24시간 CPU 사용률 (정상은 30~50% 사이에서 변동)
usage = np.round(rng.normal(40, 5, 24), 1)
usage[9] = 97.3        # 오전 9시 장애 발생
usage[17] = 2.1        # 오후 5시 서비스 중단

mean, std = usage.mean(), usage.std()
z = (usage - mean) / std

print("시각  사용률   Z-score  상태")
print("-" * 34)
for h in range(24):
    if abs(z[h]) > 2:
        state = "** 이상 **"
    elif abs(z[h]) > 1.5:
        state = "주의"
    else:
        state = "정상"
    print("{:>2}시  {:>6.1f}  {:>+7.2f}  {}".format(h, usage[h], z[h], state))

print("-" * 34)
alerts = np.where(np.abs(z) > 2)[0]
print("경보 발생 시각:", alerts, "시")
print("전체 평균 {:.2f}% / 표준편차 {:.2f}".format(mean, std))

# 이상치를 뺀 정상 상태의 통계
normal = usage[np.abs(z) <= 2]
print("정상 구간 평균 {:.2f}% / 표준편차 {:.2f}".format(normal.mean(), normal.std()))
print("정상 운영 범위: {:.1f}% ~ {:.1f}%".format(
    normal.mean() - 3 * normal.std(), normal.mean() + 3 * normal.std()))

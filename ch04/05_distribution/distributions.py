import numpy as np

rng = np.random.default_rng(0)

# 1) 균등분포: 0~10 사이에서 똑같은 확률로
uniform = rng.uniform(0, 10, 10000)

# 2) 정규분포: 평균 5, 표준편차 1.5
normal = rng.normal(5, 1.5, 10000)

for name, d in [("균등분포", uniform), ("정규분포", normal)]:
    print("{} : 평균 {:.3f}, 표준편차 {:.3f}, 최소 {:.2f}, 최대 {:.2f}".format(
        name, d.mean(), d.std(), d.min(), d.max()))

# 3) 정규분포에서 68-95-99.7 규칙 확인
m, s = normal.mean(), normal.std()
for k in [1, 2, 3]:
    inside = np.sum((normal >= m - k * s) & (normal <= m + k * s))
    print("평균 +- {}σ 안: {:>6,}개 ({:.2f}%)".format(k, inside, inside / 100))

# 4) 구간별 개수 세기 (히스토그램의 숫자 버전)
print("\n[정규분포 구간별 개수]")
counts, edges = np.histogram(normal, bins=8)
for i in range(len(counts)):
    bar = "#" * (counts[i] // 60)
    print("{:5.1f} ~ {:5.1f} : {:>5}  {}".format(edges[i], edges[i+1], counts[i], bar))

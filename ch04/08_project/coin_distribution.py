import numpy as np

rng = np.random.default_rng(777)

# 동전을 100번 던지는 실험을 1000번 반복한다
n_toss = 100
n_exp = 1000
results = np.array([np.sum(rng.integers(0, 2, n_toss)) for _ in range(n_exp)])

print("실험 조건: 동전 {}번 던지기를 {}번 반복".format(n_toss, n_exp))
print("앞면 횟수의 평균    : {:.2f} (이론값 {})".format(results.mean(), n_toss // 2))
print("앞면 횟수의 표준편차: {:.2f}".format(results.std()))
print("최소 ~ 최대         : {} ~ {}".format(results.min(), results.max()))

# 구간별 분포
print("\n[앞면 횟수 분포]")
for lo in range(30, 71, 5):
    cnt = np.sum((results >= lo) & (results < lo + 5))
    print("  {:>2}~{:>2}회: {:>4}번  {}".format(lo, lo + 4, cnt, "#" * (cnt // 5)))

# 정확히 50번 나올 확률
exact = np.sum(results == 50)
print("\n정확히 50회 앞면: {}번 ({:.1f}%)".format(exact, exact / n_exp * 100))
print("45~55회 사이     : {}번 ({:.1f}%)".format(
    np.sum((results >= 45) & (results <= 55)),
    np.sum((results >= 45) & (results <= 55)) / n_exp * 100))

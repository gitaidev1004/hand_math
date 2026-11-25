import numpy as np

def kmeans(data, k, seed=0, max_iter=100):
    """K-Means 군집화. (라벨, 중심점, 반복횟수)를 돌려준다"""
    rng = np.random.default_rng(seed)
    centers = data[rng.choice(len(data), k, replace=False)].astype(float)
    labels = np.zeros(len(data), dtype=int)
    for step in range(1, max_iter + 1):
        d = np.linalg.norm(data[:, None, :] - centers[None, :, :], axis=2)
        labels = np.argmin(d, axis=1)
        new_c = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        if np.linalg.norm(new_c - centers) < 1e-9:
            return labels, new_c, step
        centers = new_c
    return labels, centers, max_iter


raw = np.array([
    [2, 15], [3, 18], [2, 20], [3, 16],           # 소액 저빈도
    [15, 180], [17, 200], [16, 190], [18, 210],   # 고액 고빈도
    [12, 40], [14, 45], [13, 38], [15, 42],       # 자주 오지만 소액
])

# 표준화 후 군집화 (단위 차이 제거)
scaled = (raw - raw.mean(axis=0)) / raw.std(axis=0)
labels, centers, steps = kmeans(scaled, 3, seed=1)
print("{}회 만에 수렴".format(steps))

names = {0: "A", 1: "B", 2: "C"}
for k in range(3):
    group = raw[labels == k]
    print("\n[그룹 {}] {}명".format(names[k], len(group)))
    print("  평균 방문 {:.1f}회, 평균 구매 {:.1f}만원".format(
        group[:, 0].mean(), group[:, 1].mean()))
    print("  고객:", group.tolist())

# 그룹별 특성 해석
print("\n[마케팅 제안]")
for k in range(3):
    g = raw[labels == k]
    v, m = g[:, 0].mean(), g[:, 1].mean()
    if m > 100:
        msg = "VIP 전용 혜택 제공"
    elif v > 10:
        msg = "객단가를 높이는 묶음 상품 추천"
    else:
        msg = "방문을 늘리는 쿠폰 발송"
    print("  그룹 {}: {}".format(names[k], msg))

import numpy as np

# 고객 데이터: (월 방문 횟수, 월 구매액 만원)
data = np.array([
    [1, 2], [2, 3], [2, 1], [3, 2],          # 저활동 고객
    [8, 9], [9, 10], [10, 8], [9, 9],        # 고활동 고객
    [1, 9], [2, 10], [2, 8],                 # 자주 안 오지만 크게 사는 고객
])

K = 3
rng = np.random.default_rng(42)
centers = data[rng.choice(len(data), K, replace=False)].astype(float)
print("초기 중심점:\n", centers)

for step in range(1, 11):
    # 2단계: 모든 점을 가장 가까운 중심에 배정
    dists = np.linalg.norm(data[:, None, :] - centers[None, :, :], axis=2)
    labels = np.argmin(dists, axis=1)

    # 3단계: 중심을 묶음의 평균으로 이동
    new_centers = np.array([data[labels == k].mean(axis=0) for k in range(K)])

    moved = np.linalg.norm(new_centers - centers)
    print("\n[{}회차] 중심 이동거리 {:.4f}".format(step, moved))
    for k in range(K):
        pts = data[labels == k]
        print("  묶음{}: {}개  중심 ({:.2f}, {:.2f})".format(
            k, len(pts), new_centers[k][0], new_centers[k][1]))

    if moved < 1e-6:                  # 4단계: 더 안 움직이면 종료
        centers = new_centers
        print("  -> 중심이 안정되어 종료")
        break
    centers = new_centers

print("\n최종 결과")
for k in range(K):
    print("묶음{} :".format(k), data[labels == k].tolist())

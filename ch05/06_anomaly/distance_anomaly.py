import numpy as np

# 고객 데이터: (월 방문 횟수, 월 구매액 만원)
data = np.array([
    [5, 20], [6, 22], [5, 19], [7, 25], [6, 21],
    [5, 23], [6, 20], [7, 22], [30, 18], [6, 95],
])

# 1) 표준화: 단위가 다른 특징을 같은 범위로 맞춘다
mean = data.mean(axis=0)
std = data.std(axis=0)
scaled = (data - mean) / std
print("특징별 평균:", np.round(mean, 2))
print("특징별 표준편차:", np.round(std, 2))

# 2) 중심(원점)으로부터의 거리 계산
dist = np.linalg.norm(scaled, axis=1)

print("\n번호   원본 데이터      표준화 값          중심까지 거리")
print("-" * 60)
for i in range(len(data)):
    mark = "  <- 이상치" if dist[i] > 2 else ""
    print("{:>3}  [{:>3}, {:>3}]   [{:+6.2f}, {:+6.2f}]   {:>8.3f}{}".format(
        i, data[i][0], data[i][1], scaled[i][0], scaled[i][1], dist[i], mark))

print("-" * 60)
print("거리 평균 {:.3f}, 최대 {:.3f}".format(dist.mean(), dist.max()))
print("이상치 번호:", np.where(dist > 2)[0])

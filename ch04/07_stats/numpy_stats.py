import numpy as np

data = np.array([23, 45, 12, 67, 34, 89, 21, 56, 43, 38])

print("데이터     :", data)
print("개수       :", data.size)
print("합계       :", np.sum(data))
print("평균       :", np.mean(data))
print("중앙값     :", np.median(data))
print("분산       :", np.var(data))
print("표준편차   : {:.4f}".format(np.std(data)))
print("최솟값/최댓값:", np.min(data), "/", np.max(data))
print("범위       :", np.max(data) - np.min(data))
print("누적합     :", np.cumsum(data))

# 2차원 배열에서 축(axis)을 지정한 계산
table = np.array([[80, 90, 70],       # 학생1의 국영수
                  [60, 85, 95],       # 학생2
                  [75, 70, 80]])      # 학생3
print("\n성적표:")
print(table)
print("학생별 평균(행 방향, axis=1):", np.mean(table, axis=1))
print("과목별 평균(열 방향, axis=0):", np.mean(table, axis=0))
print("전체 평균                  :", np.mean(table))

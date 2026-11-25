import numpy as np

scores = np.array([55, 62, 65, 68, 70, 71, 72, 74, 75, 75,
                   76, 78, 80, 81, 82, 83, 85, 88, 90, 95])

mean, std = scores.mean(), scores.std()
print("데이터 개수 :", scores.size)
print("평균        : {:.2f}".format(mean))
print("중앙값      : {:.2f}".format(np.median(scores)))
print("표준편차    : {:.2f}".format(std))
print("범위        : {} ~ {}".format(scores.min(), scores.max()))

# 사분위수: 데이터를 4등분하는 값
q1, q2, q3 = np.percentile(scores, [25, 50, 75])
print("\n1사분위(하위 25%) : {:.1f}".format(q1))
print("2사분위(중앙값)   : {:.1f}".format(q2))
print("3사분위(상위 25%) : {:.1f}".format(q3))

# 구간별 인원
print("\n[점수 구간별 인원]")
bins = [50, 60, 70, 80, 90, 101]
labels = ["50점대", "60점대", "70점대", "80점대", "90점대"]
for i in range(len(labels)):
    cnt = np.sum((scores >= bins[i]) & (scores < bins[i + 1]))
    print("  {} : {:>2}명  {}".format(labels[i], cnt, "*" * cnt))

# 평균 ± 1표준편차 안에 몇 명?
inside = np.sum((scores >= mean - std) & (scores <= mean + std))
print("\n평균 +-1표준편차({:.1f} ~ {:.1f}) 안: {}명 ({:.0f}%)".format(
    mean - std, mean + std, inside, inside / scores.size * 100))

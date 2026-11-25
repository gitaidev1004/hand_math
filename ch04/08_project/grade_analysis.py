import numpy as np

names = ["김철수", "이영희", "박민수", "최지은", "정우성", "한소영"]
subjects = ["국어", "영어", "수학"]
scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 65, 80],
    [88, 92, 85],
    [60, 72, 58],
    [95, 85, 90],
])

print("=" * 46)
print("{:8s}".format("이름"), end="")
for s in subjects:
    print("{:>7s}".format(s), end="")
print("{:>8s}{:>8s}".format("합계", "평균"))
print("=" * 46)

for i, name in enumerate(names):
    print("{:8s}".format(name), end="")
    for j in range(len(subjects)):
        print("{:>7d}".format(scores[i, j]), end="")
    print("{:>8d}{:>8.1f}".format(np.sum(scores[i]), np.mean(scores[i])))

print("-" * 46)
print("{:8s}".format("과목평균"), end="")
for j in range(len(subjects)):
    print("{:>7.1f}".format(np.mean(scores[:, j])), end="")
print("{:>8.1f}{:>8.1f}".format(np.sum(scores) / len(names), np.mean(scores)))

print("{:8s}".format("표준편차"), end="")
for j in range(len(subjects)):
    print("{:>7.2f}".format(np.std(scores[:, j])), end="")
print()
print("=" * 46)

# 가장 편차가 큰 과목 찾기
stds = np.std(scores, axis=0)
hardest = subjects[int(np.argmax(stds))]
print("\n실력 차이가 가장 큰 과목:", hardest,
      "(표준편차 {:.2f})".format(stds.max()))
print("평균이 가장 낮은 과목   :", subjects[int(np.argmin(np.mean(scores, axis=0)))])

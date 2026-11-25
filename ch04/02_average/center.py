import numpy as np

scores = [72, 95, 68, 81, 90, 68, 77]

# ---------- 로우 코드: 정의를 그대로 구현 ----------
total = 0
for s in scores:
    total = total + s
mean_low = total / len(scores)

ordered = sorted(scores)              # 정렬
n = len(ordered)
if n % 2 == 1:
    median_low = ordered[n // 2]                    # 홀수: 가운데
else:
    median_low = (ordered[n // 2 - 1] + ordered[n // 2]) / 2   # 짝수: 평균

counts = {}
for s in scores:
    counts[s] = counts.get(s, 0) + 1   # 값마다 등장 횟수 세기
mode_low = max(counts, key=counts.get)

print("[로우 코드]")
print("  정렬된 데이터:", ordered)
print("  평균  :", round(mean_low, 2))
print("  중앙값:", median_low)
print("  최빈값:", mode_low, "(", counts[mode_low], "번 )")

# ---------- NumPy ----------
arr = np.array(scores)
values, cnts = np.unique(arr, return_counts=True)
mode_np = values[np.argmax(cnts)]

print("[NumPy]")
print("  평균  :", round(float(np.mean(arr)), 2))
print("  중앙값:", np.median(arr))
print("  최빈값:", mode_np)

import numpy as np

scores = [90, 85, 77, 68, 95]

# ---------- 방식 1: 로우 코드 (기본 문법만 사용) ----------
total = 0
for s in scores:          # 리스트의 값을 하나씩 꺼낸다
    total = total + s     # 꺼낸 값을 누적해서 더한다
average = total / len(scores)
print("[로우 코드] 합계:", total, "평균:", average)

# ---------- 방식 2: NumPy ----------
arr = np.array(scores)
print("[NumPy   ] 합계:", np.sum(arr), "평균:", np.mean(arr))

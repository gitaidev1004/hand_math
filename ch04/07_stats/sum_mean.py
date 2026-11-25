import numpy as np

scores = [72, 95, 68, 81, 90]

# 방법 1) 반복문으로 직접 더하기
total = 0
for s in scores:
    total += s                 # total = total + s 와 같은 의미
print("방법1 합계:", total, "평균:", total / len(scores))

# 방법 2) 내장 함수 sum() 사용
print("방법2 합계:", sum(scores), "평균:", sum(scores) / len(scores))

# 방법 3) NumPy 사용
arr = np.array(scores)
print("방법3 합계:", np.sum(arr), "평균:", np.mean(arr))

# 가중평균: 중요도가 다를 때
weights = [0.1, 0.3, 0.1, 0.2, 0.3]        # 합이 1이 되도록
weighted = np.sum(arr * np.array(weights))
print("\n단순평균  :", np.mean(arr))
print("가중평균  :", weighted)

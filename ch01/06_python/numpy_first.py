import numpy as np        # numpy를 np라는 짧은 이름으로 불러온다

# 1) 배열 만들기
scores = np.array([90, 85, 77, 68, 95])
print("배열        :", scores)
print("자료형      :", type(scores))
print("원소 개수   :", scores.size)

# 2) 배열 전체에 같은 연산 적용하기
print("모두 +5점   :", scores + 5)
print("모두 2배    :", scores * 2)

# 3) 배열을 하나의 숫자로 요약하기
print("합계        :", np.sum(scores))
print("평균        :", np.mean(scores))
print("최댓값      :", np.max(scores))
print("최솟값      :", np.min(scores))

import numpy as np

# 여러 사람의 사과 개수를 한 번에 처리한다
totals = np.array([10, 20, 36])    # 세 집단의 전체 사과 개수
people = np.array([2, 4, 6])       # 각 집단의 사람 수
shares = totals / people           # 배열끼리 한 번에 나눗셈

print("각 집단의 1인당 사과:", shares)

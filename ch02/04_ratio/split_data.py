import numpy as np

def divide_by_ratio(total, ratios):
    """total을 ratios의 비로 나눈다"""
    s = sum(ratios)
    return [total * r / s for r in ratios]

# 1) 돈을 2:3으로 나누기
print("60000원을 2:3 ->", divide_by_ratio(60000, [2, 3]))

# 2) 데이터 1000개를 7:2:1로 나누기
parts = divide_by_ratio(1000, [7, 2, 1])
print("학습/검증/테스트:", parts)

# 3) NumPy로 실제 데이터 나누기
data = np.arange(1000)              # 0부터 999까지의 데이터
n_train = int(1000 * 0.7)
n_valid = int(1000 * 0.2)

train = data[:n_train]                      # 처음 700개
valid = data[n_train:n_train + n_valid]     # 다음 200개
test = data[n_train + n_valid:]             # 나머지 100개

print("개수 확인:", len(train), len(valid), len(test))
print("각 구간의 첫 값:", train[0], valid[0], test[0])

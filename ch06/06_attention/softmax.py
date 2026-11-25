import numpy as np

def softmax(x):
    """여러 점수를 합이 1인 확률로 바꾼다 (오버플로 방지 포함)"""
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

scores = np.array([2.0, 1.0, 0.1])
p = softmax(scores)

print("점수   :", scores)
print("지수   :", np.round(np.exp(scores), 3))
print("지수 합: {:.3f}".format(np.sum(np.exp(scores))))
print("확률   :", np.round(p, 3))
print("확률 합: {:.6f}".format(np.sum(p)))

# 오버플로 방지 효과 확인
big = np.array([1000.0, 999.0, 998.0])
print("\n큰 값에도 안전:", np.round(softmax(big), 4))

# 점수 차이가 클수록 한쪽에 몰린다
print("\n[점수 차이에 따른 확률 분포]")
for s in [np.array([1.0, 1.0, 1.0]),
          np.array([2.0, 1.0, 0.5]),
          np.array([5.0, 1.0, 0.5])]:
    print("  점수 {} -> 확률 {}".format(s, np.round(softmax(s), 3)))

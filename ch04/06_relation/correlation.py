import numpy as np

rng = np.random.default_rng(3)
n = 60
x = rng.uniform(1, 20, n)                             # 공부 시간

y_pos = 3 * x + rng.normal(0, 5, n) + 40              # 양의 관계
y_neg = -2 * x + rng.normal(0, 5, n) + 100            # 음의 관계
y_non = rng.uniform(40, 100, n)                       # 관계 없음

def correlation(a, b):
    """상관계수를 정의대로 직접 계산한다"""
    za = (a - a.mean()) / a.std()      # 표준편차 단위로 변환
    zb = (b - b.mean()) / b.std()
    return np.mean(za * zb)

for name, y in [("양의 관계", y_pos), ("음의 관계", y_neg), ("무관계", y_non)]:
    mine = correlation(x, y)
    numpy_r = np.corrcoef(x, y)[0, 1]
    print("{:8s} 직접계산 {:+.4f} / np.corrcoef {:+.4f}".format(
        name, mine, numpy_r))

# 상관계수가 강해도 인과는 아니다 - 제3의 변수 예시
temp = np.array([5, 10, 15, 20, 25, 30, 33, 28, 20, 12])      # 기온
ice = temp * 12 + 30                                           # 아이스크림 판매
drown = temp * 0.4 + 1                                         # 익사 사고
print("\n아이스크림-익사 상관계수: {:+.4f}".format(np.corrcoef(ice, drown)[0, 1]))
print("둘 다 기온과의 상관: {:+.4f}, {:+.4f}".format(
    np.corrcoef(temp, ice)[0, 1], np.corrcoef(temp, drown)[0, 1]))

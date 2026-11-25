import numpy as np

rng = np.random.default_rng(100)

print("0~1 사이 실수 5개 :", np.round(rng.random(5), 4))
print("1~6 사이 정수 10개:", rng.integers(1, 7, 10))
print("정규분포 5개      :", np.round(rng.normal(0, 1, 5), 4))
print("리스트에서 뽑기   :", rng.choice(["가위", "바위", "보"], 5))

# 씨앗값을 고정하면 항상 같은 결과가 나온다
a = np.random.default_rng(7).integers(1, 7, 5)
b = np.random.default_rng(7).integers(1, 7, 5)
print("\n같은 씨앗값 두 번:", a, b, "-> 같은가?", np.array_equal(a, b))

# 확률이 다른 선택 (가중 추출)
items = ["당첨", "꽝"]
probs = [0.1, 0.9]
result = rng.choice(items, 12, p=probs)
print("\n10% 당첨 복권 12회:")
print(" ", " ".join(result))
print("당첨 횟수:", np.sum(result == "당첨"), "회")

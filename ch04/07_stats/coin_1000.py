import numpy as np

rng = np.random.default_rng(2024)
n = 1000
tosses = rng.integers(0, 2, n)        # 0=뒤, 1=앞

heads = np.sum(tosses)
print("총 {}회 중 앞면 {}회, 뒷면 {}회".format(n, heads, n - heads))
print("앞면 비율: {:.4f} (이론값 0.5)".format(heads / n))

# 던질수록 비율이 0.5에 가까워지는 과정 관찰
cum = np.cumsum(tosses)                       # 누적 앞면 횟수
trials = np.arange(1, n + 1)
ratios = cum / trials                         # 각 시점까지의 비율

print("\n시행 횟수별 앞면 비율의 변화")
for k in [1, 5, 10, 50, 100, 500, 1000]:
    print("  {:>5}회까지: {:.4f}".format(k, ratios[k - 1]))

# 가장 길게 이어진 연속 앞면 찾기
longest = cur = 0
for t in tosses:
    cur = cur + 1 if t == 1 else 0
    longest = max(longest, cur)
print("\n가장 길게 이어진 연속 앞면:", longest, "회")

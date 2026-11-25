import numpy as np

rng = np.random.default_rng(42)      # 난수 생성기 (42는 결과 재현용 씨앗값)

print("동전 던지기 실험 (앞면 = 1, 뒷면 = 0)")
print("{:>8} {:>8} {:>10} {:>10}".format("시행횟수", "앞면", "실제비율", "이론과차이"))
print("-" * 40)

for n in [10, 100, 1000, 10000, 100000]:
    tosses = rng.integers(0, 2, n)          # 0 또는 1을 n개 생성
    heads = np.sum(tosses)                  # 1의 개수 = 앞면 횟수
    ratio = heads / n
    print("{:>8,} {:>8,} {:>10.4f} {:>+10.4f}".format(
        n, heads, ratio, ratio - 0.5))

# 주사위도 같은 방식으로 실험
print("\n주사위 6000번 던지기")
dice = rng.integers(1, 7, 6000)             # 1~6
values, counts = np.unique(dice, return_counts=True)
for v, c in zip(values, counts):
    print("  {}: {:>4}회  비율 {:.4f} (이론 0.1667)".format(v, c, c / 6000))

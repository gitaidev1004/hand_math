import numpy as np

math_scores = np.array([70, 75, 80, 85, 90, 95, 88, 92, 85, 80])
eng_scores = np.array([40, 55, 60, 65, 70, 75, 50, 62, 58, 65])

for name, s in [("수학", math_scores), ("영어", eng_scores)]:
    print("{} : 평균 {:.1f}, 표준편차 {:.2f}, 범위 {} ~ {}".format(
        name, s.mean(), s.std(), s.min(), s.max()))

# 내 점수: 수학 80, 영어 75
my_math, my_eng = 80, 75
print("\n[평균과 비교]")
print("  수학 {}점: 평균보다 {:+.1f}점".format(my_math, my_math - math_scores.mean()))
print("  영어 {}점: 평균보다 {:+.1f}점".format(my_eng, my_eng - eng_scores.mean()))

print("\n[표준편차 단위로 비교]")
print("  수학: {:+.2f} 표준편차".format((my_math - math_scores.mean()) / math_scores.std()))
print("  영어: {:+.2f} 표준편차".format((my_eng - eng_scores.mean()) / eng_scores.std()))

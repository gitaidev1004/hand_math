# 1) 자료형 확인
print(type(10), type(10.0), type(10 / 2))

# 2) 소수 오차 확인
x = 0.1 + 0.2
print("0.1 + 0.2 =", x)
print("0.3과 같은가?", x == 0.3)

# 3) 안전하게 비교하는 방법: 차이가 아주 작으면 같다고 본다
print("오차 허용 비교:", abs(x - 0.3) < 1e-9)

# 4) 반올림해서 보기 좋게 출력
print("반올림:", round(x, 2))
print("서식 출력: {:.4f}".format(x))

# 5) 정확한 계산이 필요하면 Fraction 사용
from fractions import Fraction
print("분수로:", Fraction(1, 10) + Fraction(2, 10))

from fractions import Fraction

a = Fraction(3, 7)
b = Fraction(4, 9)

print("a =", a, "=", float(a))
print("b =", b, "=", float(b))
print("a < b ?", a < b)

# 대각선 곱셈으로 직접 비교
print("3 x 9 =", 3 * 9, " 4 x 7 =", 4 * 7)

# 통분한 결과 확인
print("통분:", Fraction(3 * 9, 63), "vs", Fraction(4 * 7, 63))

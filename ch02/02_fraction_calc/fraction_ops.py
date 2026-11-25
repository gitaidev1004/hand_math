from fractions import Fraction
from math import gcd

# 1) 분모가 같은 덧셈
print("1)", Fraction(1, 4) + Fraction(2, 4))

# 2) 분모가 다른 덧셈 (자동 통분)
print("2)", Fraction(1, 2) + Fraction(1, 3))

# 3) 뺄셈
print("3)", Fraction(3, 4) - Fraction(1, 6))

# 4) 곱셈
print("4)", Fraction(2, 3) * Fraction(4, 5))

# 5) 나눗셈 (역수를 곱한 것과 같은지 확인)
print("5)", Fraction(2, 3) / Fraction(4, 5),
      "/ 역수 곱셈:", Fraction(2, 3) * Fraction(5, 4))

# 6) 약분: 최대공약수로 나눈다
n, d = 12, 18
g = gcd(n, d)
print("6) 최대공약수", g, "->", n // g, "/", d // g)

# 소수로 바꾸어 검산
print("검산:", float(Fraction(1, 2) + Fraction(1, 3)))

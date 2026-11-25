import math

# 거듭제곱
print("2 ** 8      =", 2 ** 8)
print("math.pow    =", math.pow(2, 8))     # 결과가 실수
print("제곱근      =", math.sqrt(64))      # 64 = 8^2 이므로 8

# 로그 (밑을 지정할 수 있다)
print("log2(8)     =", math.log2(8))
print("log10(1000) =", math.log10(1000))
print("log(e)      =", math.log(math.e))   # 자연로그

# 역연산 확인: 로그를 취한 뒤 다시 거듭제곱하면 원래 값
x = 1000
y = math.log10(x)
print("log10(1000) =", y, " -> 10 **", y, "=", 10 ** y)

# e의 값
print("e =", math.e)
print("e^1 =", math.exp(1))

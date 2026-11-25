import numpy as np

x = np.array([1, 2, 3, 4, 5])

print("x        =", x)
print("exp(x)   =", np.exp(x))         # e의 x제곱
print("log(x)   =", np.log(x))         # 자연로그
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))

# 역연산 확인
print("log(exp(x)) =", np.log(np.exp(x)))

# 큰 값 범위를 로그로 압축하기
big = np.array([1, 100, 10000, 1000000])
print("원래 값    :", big)
print("log10 변환 :", np.log10(big))

# 소수점 정리해서 보기
print("exp 반올림 :", np.round(np.exp(x), 3))

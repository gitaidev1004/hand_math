import math

print("=== 지수 / 로그 계산기 ===")
base = float(input("밑을 입력하세요 (예: 2): "))
value = float(input("값을 입력하세요 (예: 8): "))

# 로그: 밑을 몇 번 곱해야 값이 되는가
result = math.log(value, base)
print("log_{:g}({:g}) = {:.4f}".format(base, value, result))

# 역연산 검증: 밑^결과 = 원래 값
back = base ** result
print("검증: {:g} ** {:.4f} = {:.4f}".format(base, result, back))

# 배수가 아닌 경우도 계산된다
print("-" * 30)
for v in [1, 2, 4, 8, 16, 100]:
    print("log2({:3d}) = {:.4f}".format(v, math.log2(v)))

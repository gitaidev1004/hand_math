# 간단한 사칙연산 계산기
print("=== 간단한 계산기 ===")

a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))

print("-" * 25)
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

if b == 0:
    print(a, "/", b, "= 0으로는 나눌 수 없습니다")
else:
    print(a, "/", b, "=", a / b)
    print(a, "//", b, "=", a // b, "... 나머지", a % b)

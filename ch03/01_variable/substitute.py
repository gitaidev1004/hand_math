# 수학의 식 2x + 1 을 Python으로 표현한다
def expression(x):
    return 2 * x + 1

# 여러 값을 대입해 본다
for x in [2, 0, -3, 10]:
    print("x =", x, "일 때  2x + 1 =", expression(x))

print("-" * 30)

# 제곱이 포함된 식: 음수를 대입할 때 주의
def square_expr(x):
    return x ** 2 + 2 * x

for x in [2, 0, -3]:
    print("x =", x, "일 때  x^2 + 2x =", square_expr(x))

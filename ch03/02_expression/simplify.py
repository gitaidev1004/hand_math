# 식을 정리한 결과가 맞는지 여러 x값으로 확인한다
def original(x):
    return 2 * (x + 3) + 4 * x - 1      # 정리 전

def simplified(x):
    return 6 * x + 5                    # 정리 후

print("x      정리 전    정리 후   같은가")
for x in [-2, 0, 1, 5, 10]:
    a, b = original(x), simplified(x)
    print("{:>3}  {:>8}  {:>8}   {}".format(x, a, b, a == b))

print("-" * 38)

# 괄호 앞 마이너스 확인: 5 - (2x + 3)
def minus_paren(x):
    return 5 - (2 * x + 3)

def wrong(x):
    return 5 - 2 * x + 3                # 부호를 바꾸지 않은 잘못된 식

def correct(x):
    return -2 * x + 2                   # 올바르게 정리한 식

for x in [1, 4]:
    print("x =", x, "원식:", minus_paren(x),
          "/ 올바른 정리:", correct(x), "/ 잘못된 식:", wrong(x))

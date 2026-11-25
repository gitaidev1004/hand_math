import numpy as np

# 1) arange: 일정 간격으로 만들기 (끝값 포함 안 함)
a = np.arange(0, 10, 2)
print("arange(0, 10, 2)   =", a)

# 2) linspace: 개수를 지정해서 만들기 (끝값 포함)
b = np.linspace(0, 10, 5)
print("linspace(0, 10, 5) =", b)

# 3) 그래프용 x와 y 만들기
x = np.linspace(-5, 5, 11)
y = 2 * x + 1
print("x =", x)
print("y =", y)

# 4) x와 y를 짝지어 출력
print("\n  x      y")
for i in range(len(x)):
    print("{:5.1f}  {:5.1f}".format(x[i], y[i]))

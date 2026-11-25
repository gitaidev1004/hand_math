# 표로 주어진 데이터에서 값을 읽고 변화를 해석한다
x_values = [0, 1, 2, 3, 4, 5]
y_values = [3, 5, 7, 9, 11, 13]

print(" x |  y  | 이전 대비 변화")
print("---+-----+---------------")
for i in range(len(x_values)):
    if i == 0:
        change = "-"
    else:
        change = "+" + str(y_values[i] - y_values[i - 1])
    print("{:2} | {:3} | {:>8}".format(x_values[i], y_values[i], change))

# x가 1 늘어날 때 y가 얼마나 변하는가 = 기울기
slope = (y_values[-1] - y_values[0]) / (x_values[-1] - x_values[0])
print("\nx가 1 증가할 때 y의 변화량(기울기):", slope)
print("x = 0일 때의 y값(절편):", y_values[0])
print("따라서 식은  y =", slope, "x +", y_values[0])

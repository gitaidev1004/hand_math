price = 20000

# 방법 1) 할인액을 구해서 빼기
rate = 0.3
discount = price * rate
pay1 = price - discount
print("할인액:", discount, "원 / 지불:", pay1, "원")

# 방법 2) 남는 비율을 바로 곱하기
pay2 = price * (1 - rate)
print("방법 2 지불:", pay2, "원")

# 중복 할인: 30% 후 추가 20%
step1 = price * (1 - 0.3)
step2 = step1 * (1 - 0.2)
print("1차 할인 후:", step1, "원")
print("2차 할인 후:", step2, "원")

total_rate = 1 - (step2 / price)
print("실제 총 할인율: {:.1%}".format(total_rate))

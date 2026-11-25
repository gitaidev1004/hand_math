# 아래 코드에는 계산 순서와 관련된 실수가 하나 있다
price = 20000
discount_rate = 0.2
count = 2

# (잘못된 계산) 의도: 할인된 가격 x 수량
wrong = price - discount_rate * count
print("잘못된 결과:", wrong)

# (올바른 계산) 할인가를 먼저 구하고 수량을 곱한다
unit = price * (1 - discount_rate)     # 할인된 단가
right = unit * count
print("올바른 결과:", right)

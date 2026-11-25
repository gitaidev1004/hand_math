# 배송비 3000원 + 개당 1200원  ->  y = 1200x + 3000
UNIT = 1200
SHIPPING = 3000

def total_price(count):
    """구매 수량을 받아 총 결제 금액을 돌려준다"""
    if count == 0:
        return 0                       # 안 사면 배송비도 없다
    return UNIT * count + SHIPPING

def max_count(budget):
    """예산으로 살 수 있는 최대 수량 (방정식을 거꾸로 푼다)"""
    if budget < UNIT + SHIPPING:
        return 0
    return (budget - SHIPPING) // UNIT

print("수량    총액      개당 실부담")
print("-" * 32)
for n in [0, 1, 3, 5, 10, 20]:
    total = total_price(n)
    per = total / n if n > 0 else 0
    print("{:>4}  {:>7,}원  {:>9,.0f}원".format(n, total, per))

print("-" * 32)
for budget in [10000, 30000, 100000]:
    n = max_count(budget)
    print("예산 {:,}원 -> 최대 {}개 (결제 {:,}원, 잔액 {:,}원)".format(
        budget, n, total_price(n), budget - total_price(n)))

# 상품 구매 금액 계산
price = 15000        # 상품 1개 가격
count = 3            # 구매 수량

total = price * count          # 1단계: 합계
discount = total * 0.1         # 2단계: 10% 할인액
payment = total - discount     # 3단계: 실제 지불 금액

print("상품 가격:", price, "원")
print("구매 수량:", count, "개")
print("합계 금액:", total, "원")
print("할인 금액:", discount, "원")
print("지불 금액:", payment, "원")

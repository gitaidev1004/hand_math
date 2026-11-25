VAT = 0.1       # 부가가치세율 10%

supply = 50000
total = supply * (1 + VAT)
print("공급가액", supply, "-> 판매가", total)

# 되돌리기: 나눗셈을 사용해야 한다
back = total / (1 + VAT)
print("판매가", total, "-> 공급가액", back)

# 흔한 실수: 0.9를 곱하면 틀린다
wrong = total * 0.9
print("잘못된 계산:", wrong, "(차이", round(back - wrong), "원)")

# 세액만 따로 구하기
tax = total - back
print("세액:", tax, "원")

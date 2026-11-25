# 한 달 예산을 하루 단위로 나눈다
monthly = 300000      # 한 달 예산(원)
days = 30             # 한 달 일수
fixed = 60000         # 교통비 등 고정 지출

usable = monthly - fixed          # 쓸 수 있는 돈
per_day = usable // days          # 하루 용돈(원 단위로 버림)
left = usable % days              # 나누고 남은 돈

print("한 달 예산   :", monthly, "원")
print("고정 지출    :", fixed, "원")
print("사용 가능액  :", usable, "원")
print("하루 용돈    :", per_day, "원")
print("남는 돈      :", left, "원")

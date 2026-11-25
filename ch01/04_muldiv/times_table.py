# 3단부터 5단까지 곱셈표를 출력한다
for dan in range(3, 6):          # dan = 3, 4, 5
    for i in range(1, 10):       # i = 1 ~ 9
        print(dan, "x", i, "=", dan * i)
    print("-" * 12)              # 단이 끝나면 구분선 출력

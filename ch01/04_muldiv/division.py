a = 17
b = 5

print("a / b  =", a / b)      # 소수까지 계산
print("a // b =", a // b)     # 몫만 (소수점 버림)
print("a % b  =", a % b)      # 나머지만

# 검산: 나누는 수 x 몫 + 나머지 = 원래 수
check = b * (a // b) + (a % b)
print("검산 결과:", check)

# 짝수/홀수 판별에도 나머지를 사용한다
for n in [10, 7, 24]:
    if n % 2 == 0:
        print(n, "은(는) 짝수")
    else:
        print(n, "은(는) 홀수")

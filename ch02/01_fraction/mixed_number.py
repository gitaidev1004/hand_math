# 가분수 <-> 대분수 변환
numerator = 7      # 분자
denominator = 4    # 분모

whole = numerator // denominator       # 정수 부분 = 몫
rest = numerator % denominator         # 남은 분자 = 나머지

print(numerator, "/", denominator, "=", whole, "과", rest, "/", denominator)
print("소수로는:", numerator / denominator)

# 반대로 대분수를 가분수로
w, n, d = 1, 3, 4
print(w, "과", n, "/", d, "=", (w * d + n), "/", d)

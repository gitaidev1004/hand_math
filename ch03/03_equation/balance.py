# 방정식 x + 3 = 7 을 등식의 성질로 푼다
left_const = 3        # 좌변의 상수
right = 7             # 우변

print("원래 식 : x +", left_const, "=", right)

# 양변에서 같은 수를 뺀다
answer = right - left_const
print("양변에서", left_const, "을(를) 뺀다")
print("결과    : x =", answer)

# 검산
check = answer + left_const
print("검산    :", answer, "+", left_const, "=", check,
      "-> 우변과 같은가?", check == right)

print("-" * 30)

# 여러 방정식을 한 번에 풀어 본다  (x + a = b 형태)
problems = [(3, 7), (-5, 2), (10, 4), (0, 9)]
for a, b in problems:
    x = b - a
    print("x + ({:>3}) = {:>2}  ->  x = {:>3}  (검산 {})".format(
        a, b, x, x + a == b))

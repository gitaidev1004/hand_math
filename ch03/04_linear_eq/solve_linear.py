def solve(a, b, c, d):
    """ax + b = cx + d 형태의 일차방정식을 푼다"""
    if a == c:
        return None                 # x항이 사라지면 해가 없거나 무수히 많음
    return (d - b) / (a - c)

# 여러 방정식을 풀고 검산까지 수행한다
problems = [
    (1, 3, 0, 7,   "x + 3 = 7"),
    (1, -5, 0, 2,  "x - 5 = 2"),
    (2, 0, 0, 10,  "2x = 10"),
    (2, 3, 0, 11,  "2x + 3 = 11"),
    (5, -4, 2, 8,  "5x - 4 = 2x + 8"),
    (3, 6, 0, 18,  "3x + 6 = 18  (3(x+2)=18)"),
]

for a, b, c, d, label in problems:
    x = solve(a, b, c, d)
    left = a * x + b
    right = c * x + d
    print("{:28s} x = {:>5.2f}   검산 {:>7.2f} = {:>7.2f}  {}".format(
        label, x, left, right, abs(left - right) < 1e-9))

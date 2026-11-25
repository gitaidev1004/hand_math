# 비례식 a : b = c : x 에서 x를 구한다
def solve_proportion(a, b, c):
    """a : b = c : x 일 때 x = b * c / a"""
    return b * c / a

# 공책 3권 3600원 -> 7권은?
price7 = solve_proportion(3, 3600, 7)
print("공책 7권 가격:", price7, "원")

# 검산: 외항의 곱 = 내항의 곱
print("검산  3 x", price7, "=", 3 * price7)
print("      3600 x 7 =", 3600 * 7)

# 지도 축척: 지도에서 2cm가 실제 5km일 때, 지도 7cm는?
real = solve_proportion(2, 5, 7)
print("지도 7cm의 실제 거리:", real, "km")

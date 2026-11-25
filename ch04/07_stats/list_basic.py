scores = [72, 95, 68, 81, 90]

print("전체       :", scores)
print("첫 번째    :", scores[0])
print("세 번째    :", scores[2])
print("마지막     :", scores[-1])
print("뒤에서 둘째:", scores[-2])
print("개수       :", len(scores))

# 일부만 잘라내기 (슬라이싱)
print("앞 3개     :", scores[:3])
print("뒤 2개     :", scores[-2:])
print("2~4번째    :", scores[1:4])

# 값 추가와 변경
scores.append(85)          # 끝에 추가
scores[0] = 75             # 첫 값 변경
print("변경 후    :", scores)

# 정렬 (원본을 바꾸지 않는 방법)
print("정렬       :", sorted(scores))
print("원본 유지  :", scores)

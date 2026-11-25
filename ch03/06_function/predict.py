# 공부 시간과 점수의 관계: y = 5x + 40
def predict_score(hours):
    """공부 시간을 받아 예상 점수를 돌려준다"""
    return 5 * hours + 40

# 이미 알고 있는 데이터
known = [(2, 50), (4, 60), (6, 70)]
print("[기존 데이터 확인]")
for h, real in known:
    pred = predict_score(h)
    print("  {}시간 -> 실제 {}점 / 예측 {}점 / 오차 {}".format(
        h, real, pred, real - pred))

# 데이터에 없는 값 예측하기
print("\n[새로운 예측]")
for h in [8, 10, 0]:
    print("  {}시간 공부하면 약 {}점".format(h, predict_score(h)))

# 거꾸로 묻기: 90점을 받으려면 몇 시간?
target = 90
hours_needed = (target - 40) / 5
print("\n{}점을 받으려면 {}시간 필요".format(target, hours_needed))
print("검증:", predict_score(hours_needed), "점")

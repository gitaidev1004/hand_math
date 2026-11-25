import numpy as np

def distance(speed, hours):
    """거리 = 속도 x 시간"""
    return speed * hours

def time_needed(speed, dist):
    """시간 = 거리 / 속도  (거리 공식을 거꾸로 푼 것)"""
    return dist / speed

speed = 60      # km/h
times = np.array([0, 1, 2, 3, 4, 5])
dists = distance(speed, times)

print("시속 {}km로 달릴 때".format(speed))
print("시간(h) :", times)
print("거리(km):", dists)

# 거꾸로: 300km를 가려면?
target = 300
print("\n{}km를 가려면 {}시간 필요".format(target, time_needed(speed, target)))

# 속도가 다르면?
print("\n[속도별 3시간 이동 거리]")
for s in [40, 60, 80, 100]:
    print("  시속 {:>3}km -> {:>3}km  (기울기 {})".format(s, distance(s, 3), s))

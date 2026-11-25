import numpy as np

names = ["김철수", "이영희", "박민수", "최지은", "정우성"]
scores = np.array([72, 95, 68, 81, 90])
full = 100

percent = scores / full                 # 0~1 사이 비율
print("이름     점수   백분율  등급")
print("-" * 30)
for i in range(len(names)):
    p = percent[i]
    if p >= 0.9:
        grade = "A"
    elif p >= 0.8:
        grade = "B"
    elif p >= 0.7:
        grade = "C"
    else:
        grade = "D"
    print("{:6s} {:>5d} {:>7.0%}   {}".format(names[i], scores[i], p, grade))

print("-" * 30)
print("학급 평균: {:.1f}점 ({:.1%})".format(np.mean(scores), np.mean(percent)))
print("최고점과의 차이:", np.max(scores) - scores)

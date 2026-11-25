import numpy as np

def analyze(name, data):
    """데이터 하나에 대한 통계 보고서를 출력한다"""
    arr = np.array(data, dtype=float)
    mean, std = arr.mean(), arr.std()
    q1, q2, q3 = np.percentile(arr, [25, 50, 75])

    print("\n" + "=" * 44)
    print(" [{}] 데이터 분석 보고서".format(name))
    print("=" * 44)
    print(" 1. 기본 정보")
    print("    개수     : {}".format(arr.size))
    print("    최솟값   : {:.2f}".format(arr.min()))
    print("    최댓값   : {:.2f}".format(arr.max()))
    print("    범위     : {:.2f}".format(arr.max() - arr.min()))

    print(" 2. 대표값")
    print("    평균     : {:.2f}".format(mean))
    print("    중앙값   : {:.2f}".format(q2))
    print("    사분위수 : Q1 {:.2f} / Q3 {:.2f}".format(q1, q3))

    print(" 3. 흩어짐")
    print("    분산     : {:.2f}".format(arr.var()))
    print("    표준편차 : {:.2f}".format(std))
    print("    변동계수 : {:.1%}  (표준편차/평균)".format(std / mean))

    print(" 4. 이상치 점검 (평균 +- 2표준편차 기준)")
    low, high = mean - 2 * std, mean + 2 * std
    outliers = arr[(arr < low) | (arr > high)]
    print("    정상 범위: {:.2f} ~ {:.2f}".format(low, high))
    if outliers.size == 0:
        print("    이상치   : 없음")
    else:
        print("    이상치   : {} ({}개)".format(outliers, outliers.size))

    print(" 5. 해석")
    if mean > q2 * 1.1:
        print("    평균이 중앙값보다 크다 -> 큰 값 쪽으로 치우침")
    elif mean < q2 * 0.9:
        print("    평균이 중앙값보다 작다 -> 작은 값 쪽으로 치우침")
    else:
        print("    평균과 중앙값이 비슷하다 -> 비교적 대칭적인 분포")


analyze("시험 점수", [55, 62, 65, 68, 70, 71, 72, 74, 75, 75,
                   76, 78, 80, 81, 82, 83, 85, 88, 90, 95])
analyze("월 매출", [120, 135, 128, 150, 165, 180, 210, 230, 190, 170, 155, 500])

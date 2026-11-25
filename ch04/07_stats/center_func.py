import numpy as np

def describe(data):
    """데이터의 대표값들을 한 번에 계산해 돌려준다"""
    arr = np.array(data)
    values, counts = np.unique(arr, return_counts=True)
    return {
        "개수": len(arr),
        "평균": round(float(arr.mean()), 2),
        "중앙값": float(np.median(arr)),
        "최빈값": int(values[np.argmax(counts)]),
        "최솟값": int(arr.min()),
        "최댓값": int(arr.max()),
    }

datasets = {
    "정상 데이터": [70, 72, 75, 75, 78, 80, 82],
    "이상치 포함": [70, 72, 75, 75, 78, 80, 500],
}

for name, data in datasets.items():
    print("[" + name + "]", data)
    result = describe(data)
    for key, value in result.items():
        print("   {:5s}: {}".format(key, value))
    print()

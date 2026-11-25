import numpy as np

def evaluate(actual, pred):
    """혼동행렬과 평가 지표를 계산한다"""
    TP = int(np.sum((pred == 1) & (actual == 1)))
    TN = int(np.sum((pred == 0) & (actual == 0)))
    FP = int(np.sum((pred == 1) & (actual == 0)))
    FN = int(np.sum((pred == 0) & (actual == 1)))

    total = TP + TN + FP + FN
    acc = (TP + TN) / total
    prec = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    rec = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0

    print("          예측:양성  예측:음성")
    print("  실제:양성  {:>6}    {:>6}".format(TP, FN))
    print("  실제:음성  {:>6}    {:>6}".format(FP, TN))
    print("  정확도 {:.4f} / 정밀도 {:.4f} / 재현율 {:.4f} / F1 {:.4f}".format(
        acc, prec, rec, f1))
    return acc, prec, rec, f1


# 예제 1: 손 계산과 같은 상황 (TP=8, FP=2, FN=4, TN=86)
actual = np.array([1] * 12 + [0] * 88)
pred = np.array([1] * 8 + [0] * 4 + [1] * 2 + [0] * 86)
print("[예제 1] 균형 잡힌 모델")
evaluate(actual, pred)

# 예제 2: 모두 음성이라고 답하는 게으른 모델
print("\n[예제 2] 전부 음성이라 답하는 모델")
lazy = np.zeros(100, dtype=int)
evaluate(actual, lazy)

# 예제 3: 모두 양성이라고 답하는 모델
print("\n[예제 3] 전부 양성이라 답하는 모델")
greedy = np.ones(100, dtype=int)
evaluate(actual, greedy)

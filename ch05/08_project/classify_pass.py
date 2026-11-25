import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

X = np.array([
    [2, 70], [3, 75], [4, 80], [5, 85], [6, 90],
    [7, 92], [8, 95], [9, 97], [1, 60], [10, 99],
])
y_score = np.array([55, 62, 68, 75, 82, 85, 90, 94, 48, 97])
y_class = (y_score >= 70).astype(int)        # 70점 이상이면 합격(1)

print("실제 합격 여부:", y_class)

# 학습으로 찾았다고 가정한 가중치 (제6장에서 직접 학습한다)
w = np.array([0.55, 0.12])
b = -11.0

z = X @ w + b
prob = sigmoid(z)
pred = (prob >= 0.5).astype(int)

print("\n시간 출석  z값    확률   예측 실제")
print("-" * 38)
for i in range(len(X)):
    print("{:>3} {:>4}  {:>+6.2f}  {:.4f}   {}    {}".format(
        X[i][0], X[i][1], z[i], prob[i], pred[i], y_class[i]))

# 평가 지표 계산
TP = int(np.sum((pred == 1) & (y_class == 1)))
TN = int(np.sum((pred == 0) & (y_class == 0)))
FP = int(np.sum((pred == 1) & (y_class == 0)))
FN = int(np.sum((pred == 0) & (y_class == 1)))
acc = (TP + TN) / len(y_class)
prec = TP / (TP + FP) if TP + FP else 0
rec = TP / (TP + FN) if TP + FN else 0
f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0

print("-" * 38)
print("TP {} TN {} FP {} FN {}".format(TP, TN, FP, FN))
print("정확도 {:.3f} 정밀도 {:.3f} 재현율 {:.3f} F1 {:.3f}".format(
    acc, prec, rec, f1))

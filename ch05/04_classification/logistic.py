import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 학습으로 찾았다고 가정한 가중치
a, b = 1.2, -6.0

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
actual = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])      # 실제 합격 여부

z = a * hours + b
prob = sigmoid(z)
pred = (prob >= 0.5).astype(int)        # True/False를 1/0으로

print("시간   z값    확률    예측  실제  일치")
print("-" * 42)
for i in range(len(hours)):
    mark = "O" if pred[i] == actual[i] else "X"
    print("{:>3}  {:>6.2f}  {:.4f}   {}     {}    {}".format(
        hours[i], z[i], prob[i], pred[i], actual[i], mark))

acc = np.mean(pred == actual)
print("-" * 42)
print("정확도: {:.1%} ({}/{})".format(acc, np.sum(pred == actual), len(hours)))

# 결정 경계: z = 0 이 되는 지점
boundary = -b / a
print("\n결정 경계: {:.2f}시간 (이보다 많이 공부하면 합격 예측)".format(boundary))

# 임계값을 바꾸면 결과가 달라진다
print("\n[임계값별 예측 결과]")
for t in [0.3, 0.5, 0.7]:
    p = (prob >= t).astype(int)
    print("  임계값 {:.1f}: 합격 예측 {}명, 정확도 {:.1%}".format(
        t, np.sum(p), np.mean(p == actual)))

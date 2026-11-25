import numpy as np

# 손실 함수 L(w) = (w - 4)^2 + 2 의 최저점을 찾아보자
def loss(w):
    return (w - 4) ** 2 + 2

def numeric_gradient(f, w, h=1e-5):
    """수치 미분으로 기울기를 구한다"""
    return (f(w + h) - f(w - h)) / (2 * h)

w = 0.0              # 시작 위치
lr = 0.2             # 학습률

print("회차    w        손실      기울기    갱신 내용")
print("-" * 54)
for step in range(1, 16):
    g = numeric_gradient(loss, w)
    new_w = w - lr * g
    print("{:>3}  {:>7.4f}  {:>8.4f}  {:>8.4f}   {:.4f} -> {:.4f}".format(
        step, w, loss(w), g, w, new_w))
    w = new_w
    if abs(g) < 1e-4:
        print("기울기가 거의 0 -> 최저점 도달")
        break

print("-" * 54)
print("찾은 w: {:.6f} (정답 4.0)".format(w))
print("최종 손실: {:.6f} (최솟값 2.0)".format(loss(w)))

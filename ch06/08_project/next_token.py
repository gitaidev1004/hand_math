import numpy as np

rng = np.random.default_rng(2024)

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

# "나는 밥을" 다음에 올 토큰의 점수(로짓) - 모델이 계산했다고 가정
tokens = ["먹었다", "샀다", "지었다", "버렸다", "하늘", "컴퓨터"]
logits = np.array([5.2, 3.8, 3.1, 2.0, -1.0, -2.5])

print("[Temperature에 따른 확률 분포]")
print("{:8s}".format("토큰"), end="")
for T in [0.5, 1.0, 1.5, 2.0]:
    print("{:>9s}".format("T=" + str(T)), end="")
print()
for i, t in enumerate(tokens):
    print("{:8s}".format(t), end="")
    for T in [0.5, 1.0, 1.5, 2.0]:
        print("{:>9.4f}".format(softmax(logits / T)[i]), end="")
    print()

# Top-k 적용
def top_k(probs, k):
    idx = np.argsort(-probs)[:k]
    masked = np.zeros_like(probs)
    masked[idx] = probs[idx]
    return masked / masked.sum()

# Top-p 적용
def top_p(probs, p):
    order = np.argsort(-probs)
    cum = np.cumsum(probs[order])
    cut = np.searchsorted(cum, p) + 1
    keep = order[:cut]
    masked = np.zeros_like(probs)
    masked[keep] = probs[keep]
    return masked / masked.sum(), cut

base = softmax(logits)
print("\n기본 확률     :", np.round(base, 4))
print("Top-k(k=3)    :", np.round(top_k(base, 3), 4))
p_probs, cut = top_p(base, 0.9)
print("Top-p(p=0.9)  :", np.round(p_probs, 4), "-> 후보 {}개".format(cut))

# 실제로 토큰을 뽑아 본다
print("\n[T=1.0으로 10번 생성]")
picks = rng.choice(tokens, 10, p=base)
print(" ", " ".join(picks))
print("\n[T=0.3으로 10번 생성]")
picks2 = rng.choice(tokens, 10, p=softmax(logits / 0.3))
print(" ", " ".join(picks2))

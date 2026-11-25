import numpy as np

def softmax(x, axis=-1):
    e = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e / np.sum(e, axis=axis, keepdims=True)

# 손 계산과 같은 설정
q = np.array([1.0, 0.0])                       # '빨갛다'의 Query
K = np.array([[0.2, 0.8],                      # '그'
              [1.0, 0.1],                      # '사과는'
              [0.4, 0.5]])                     # '빨갛다'
V = np.array([[0.1, 0.9],
              [0.8, 0.2],
              [0.5, 0.5]])
d = q.shape[0]

scores = K @ q                                 # ① 내적
scaled = scores / np.sqrt(d)                   # ② 스케일링
weights = softmax(scaled)                      # ③ 소프트맥스
context = weights @ V                          # ④ 가중평균

words = ["그", "사과는", "빨갛다"]
print("① 내적 점수   :", np.round(scores, 3))
print("② √d로 나눔   :", np.round(scaled, 3))
print("③ Attention 가중치")
for w, p in zip(words, weights):
    print("     {:6s}: {:.3f}  {}".format(w, p, "#" * int(p * 40)))
print("④ 문맥 벡터   :", np.round(context, 3))

# ---------- 전체 문장에 대한 Self-Attention ----------
print("\n[Self-Attention: 모든 단어가 Query가 된다]")
Q = np.array([[0.3, 0.6], [1.0, 0.0], [1.0, 0.0]])    # 단어 3개의 Query
A = softmax((Q @ K.T) / np.sqrt(d), axis=1)           # (3,3) 관련도 행렬
out = A @ V

print("관련도 행렬 (행=보는 단어, 열=참고되는 단어)")
print("          " + "".join("{:>9s}".format(w) for w in words))
for i, w in enumerate(words):
    print("{:8s}".format(w), end="")
    for j in range(3):
        print("{:>9.3f}".format(A[i, j]), end="")
    print()
print("\n각 단어의 문맥 벡터:")
for i, w in enumerate(words):
    print("  {:6s}: {}".format(w, np.round(out[i], 3)))

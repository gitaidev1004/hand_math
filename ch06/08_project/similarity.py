import numpy as np

rng = np.random.default_rng(7)

# 8차원 임베딩을 가진 작은 사전
vocab = ["왕", "여왕", "남자", "여자", "사과", "포도", "자동차", "기차"]
base = {
    "왕":     [0.9, 0.8, 0.1, 0.0, 0.0, 0.0, 0.1, 0.0],
    "여왕":   [0.9, 0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 0.0],
    "남자":   [0.2, 0.9, 0.2, 0.0, 0.0, 0.0, 0.1, 0.0],
    "여자":   [0.2, 0.1, 0.2, 0.0, 0.0, 0.0, 0.1, 0.0],
    "사과":   [0.0, 0.0, 0.0, 0.9, 0.8, 0.1, 0.0, 0.0],
    "포도":   [0.0, 0.0, 0.0, 0.9, 0.7, 0.2, 0.0, 0.0],
    "자동차": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.8],
    "기차":   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.7],
}
E = np.array([base[w] for w in vocab])

def cosine_matrix(M):
    """모든 쌍의 코사인 유사도를 한 번에 계산한다"""
    norms = np.linalg.norm(M, axis=1, keepdims=True)
    unit = M / norms
    return unit @ unit.T

S = cosine_matrix(E)

print("[유사도 행렬]")
print("        " + "".join("{:>8s}".format(w) for w in vocab))
for i, w in enumerate(vocab):
    print("{:7s}".format(w), end="")
    for j in range(len(vocab)):
        print("{:>8.2f}".format(S[i, j]), end="")
    print()

print("\n[각 단어와 가장 비슷한 단어]")
for i, w in enumerate(vocab):
    s = S[i].copy()
    s[i] = -2                       # 자기 자신 제외
    j = int(np.argmax(s))
    print("  {:6s} -> {:6s} ({:.3f})".format(w, vocab[j], s[j]))

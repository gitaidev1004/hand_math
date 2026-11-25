import numpy as np

# 아주 작은 임베딩 표 (실제로는 학습으로 만들어진다)
# 각 단어를 4차원 벡터로 표현: [생물, 먹을것, 크기, 움직임]
vocab = {
    "사과":   np.array([0.9, 0.95, 0.2, 0.0]),
    "바나나": np.array([0.9, 0.93, 0.25, 0.0]),
    "고양이": np.array([0.95, 0.05, 0.3, 0.9]),
    "강아지": np.array([0.95, 0.05, 0.35, 0.92]),
    "자동차": np.array([0.0, 0.0, 0.8, 0.85]),
    "돌":     np.array([0.0, 0.0, 0.3, 0.0]),
}

def cosine(a, b):
    """코사인 유사도: 두 벡터의 방향이 얼마나 같은가"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 손 계산 검증
a, b = np.array([3, 4]), np.array([4, 3])
print("검증: cos((3,4),(4,3)) = {:.4f} (손 계산 0.96)".format(cosine(a, b)))

words = list(vocab.keys())
print("\n[단어 간 코사인 유사도]")
print("        " + "".join("{:>8s}".format(w) for w in words))
for w1 in words:
    print("{:6s}".format(w1), end="")
    for w2 in words:
        print("{:>8.3f}".format(cosine(vocab[w1], vocab[w2])), end="")
    print()

print("\n[가장 비슷한 단어 찾기]")
for target in ["사과", "고양이", "자동차"]:
    sims = [(w, cosine(vocab[target], vocab[w])) for w in words if w != target]
    sims.sort(key=lambda t: -t[1])
    print("  {} 와 가장 비슷한 단어: {} ({:.4f})".format(
        target, sims[0][0], sims[0][1]))

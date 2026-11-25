import numpy as np

# '왕 - 남자 + 여자 = 여왕' 을 확인하는 예제
emb = {
    "왕":   np.array([0.9, 0.8, 0.1]),      # [권력, 남성성, 젊음]
    "여왕": np.array([0.9, 0.1, 0.1]),
    "남자": np.array([0.2, 0.9, 0.3]),
    "여자": np.array([0.2, 0.1, 0.3]),
    "소년": np.array([0.1, 0.9, 0.9]),
    "소녀": np.array([0.1, 0.1, 0.9]),
}

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 벡터 연산으로 의미를 계산한다
result = emb["왕"] - emb["남자"] + emb["여자"]
print("왕 - 남자 + 여자 =", np.round(result, 3))
print("여왕 벡터        =", emb["여왕"])

print("\n[계산 결과와 각 단어의 유사도]")
for w, v in emb.items():
    print("  {:4s}: {:.4f}".format(w, cosine(result, v)))

best = max(emb.items(), key=lambda kv: cosine(result, kv[1]))
print("\n가장 가까운 단어:", best[0])

# 다른 관계도 확인
r2 = emb["소년"] - emb["남자"] + emb["여자"]
best2 = max(emb.items(), key=lambda kv: cosine(r2, kv[1]))
print("소년 - 남자 + 여자 ->", best2[0])

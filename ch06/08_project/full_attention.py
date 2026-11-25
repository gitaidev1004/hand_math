import numpy as np

rng = np.random.default_rng(42)

def softmax(x, axis=-1):
    e = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e / np.sum(e, axis=axis, keepdims=True)

words = ["나는", "빨간", "사과를", "먹었다"]
d_model, d_k = 6, 4

# 입력 임베딩 (실제로는 학습된 값)
X = rng.normal(0, 1, (len(words), d_model))

# Q, K, V를 만드는 가중치 행렬 (학습 대상)
Wq = rng.normal(0, 0.5, (d_model, d_k))
Wk = rng.normal(0, 0.5, (d_model, d_k))
Wv = rng.normal(0, 0.5, (d_model, d_k))

Q, K, V = X @ Wq, X @ Wk, X @ Wv
print("입력 X 모양:", X.shape, " Q/K/V 모양:", Q.shape)

scores = Q @ K.T / np.sqrt(d_k)
A = softmax(scores, axis=1)
out = A @ V

print("\n[Attention 가중치 행렬]")
print("            " + "".join("{:>9s}".format(w) for w in words))
for i, w in enumerate(words):
    print("{:10s}".format(w), end="")
    for j in range(len(words)):
        print("{:>9.3f}".format(A[i, j]), end="")
    print("   합 {:.2f}".format(A[i].sum()))

print("\n[각 단어가 가장 많이 참고하는 단어]")
for i, w in enumerate(words):
    j = int(np.argmax(A[i]))
    print("  {:6s} -> {:6s} ({:.3f})".format(w, words[j], A[i, j]))

print("\n출력(문맥 반영 벡터) 모양:", out.shape)
print(np.round(out, 3))

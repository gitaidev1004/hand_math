import numpy as np

print("리스트로부터  :", np.array([1, 2, 3, 4, 5]))
print("0으로 채우기  :", np.zeros(5))
print("1로 채우기    :", np.ones(5))
print("같은 값 채우기:", np.full(5, 7))
print("연속된 정수   :", np.arange(5))
print("간격 지정     :", np.arange(0, 10, 2))
print("개수 지정     :", np.linspace(0, 1, 5))

# 2차원 배열 (제5장의 행렬)
table = np.array([[1, 2, 3],
                  [4, 5, 6]])
print("\n2차원 배열:")
print(table)
print("모양(행, 열):", table.shape)
print("전체 개수   :", table.size)
print("자료형      :", table.dtype)

# 배열의 일부 꺼내기
print("\n1행 전체:", table[0])
print("2행 3열 :", table[1, 2])
print("1열 전체:", table[:, 0])

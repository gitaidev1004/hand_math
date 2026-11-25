import numpy as np

# 학생 한 명의 점수를 벡터로
student = np.array([80, 90, 70])
print("학생 벡터   :", student)
print("차원(개수)  :", student.shape)
print("국어 점수   :", student[0])

# 여러 학생 = 여러 벡터 = 행렬
students = np.array([[80, 90, 70],
                     [60, 85, 95],
                     [75, 70, 80]])
print("\n행렬 모양   :", students.shape, "(3명, 3과목)")
print("두 번째 학생:", students[1])
print("수학 점수만 :", students[:, 2])

# 벡터의 각 자리에 이름 붙이기
subjects = ["국어", "영어", "수학"]
for name, score in zip(subjects, student):
    print("  {} : {}".format(name, score))

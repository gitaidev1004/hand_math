# 0으로 나누면 오류가 발생한다
total = 10
count = 0

# print(total / count)   # 이 줄의 주석을 풀면 ZeroDivisionError 발생

# 안전하게 처리하는 방법
if count == 0:
    print("나눌 수 없습니다. (분모가 0)")
else:
    print("평균:", total / count)

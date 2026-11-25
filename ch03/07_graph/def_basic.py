# 함수 정의의 기본 구조
def add(a, b):              # def 이름(매개변수):
    result = a + b          # 들여쓰기 4칸
    return result           # 결과 돌려주기

# 수학의 f(x) = 2x + 1 과 같은 함수
def f(x):
    return 2 * x + 1

# 함수 사용하기(호출)
print("add(3, 5)  =", add(3, 5))
print("f(3)       =", f(3))
print("f(0)       =", f(0))
print("f(-2)      =", f(-2))

# 함수는 다른 함수 안에서도 쓸 수 있다
print("f(add(1, 2)) =", f(add(1, 2)))

# 기본값을 가진 매개변수
def linear(x, a=1, b=0):
    """y = ax + b 를 계산한다. a와 b를 생략하면 y = x"""
    return a * x + b

print("linear(5)         =", linear(5))
print("linear(5, 2)      =", linear(5, 2))
print("linear(5, 2, 3)   =", linear(5, 2, 3))

from math import gcd

def simplify(a, b):
    """두 정수의 비를 가장 간단하게 만든다"""
    g = gcd(a, b)
    return a // g, b // g

print("40 : 60 ->", simplify(40, 60))
print("18 : 24 ->", simplify(18, 24))
print("35 : 49 ->", simplify(35, 49))

# 소수가 섞인 비: 10을 곱해 정수로 만든 뒤 간단히 한다
a, b = 0.5, 1.5
print("0.5 : 1.5 ->", simplify(int(a * 10), int(b * 10)))

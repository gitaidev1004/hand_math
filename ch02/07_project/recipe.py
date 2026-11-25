# 4인분 기준 재료를 인원수에 맞게 조정한다
base_people = 4
recipe = {"밀가루(g)": 400, "설탕(g)": 120, "우유(ml)": 300, "달걀(개)": 2}

target = 7      # 만들고 싶은 인분

ratio = target / base_people        # 배율
print(base_people, "인분 ->", target, "인분 (배율 {:.2f})".format(ratio))
print("-" * 30)

for name, amount in recipe.items():
    need = amount * ratio
    print("{:10s} {:>8.1f}".format(name, need))

# 비례식으로 검산: 4 : 400 = 7 : x
x = 400 * 7 / 4
print("-" * 30)
print("비례식 검산(밀가루):", x, "g")

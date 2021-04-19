from random import randint

with open("lesson5.txt", "w", encoding='utf-8')as f:
    user = [randint(1, 100) for _ in range(100)]
    f.write(" ".join(map(str, user)))
print(f" сумма чисел = {sum(user)}")
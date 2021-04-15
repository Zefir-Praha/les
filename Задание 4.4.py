from random import randint

user = [randint(-10, 10) for _ in range(20)]
uniq = [el for el in user if user.count(el) ==1]
print(uniq)
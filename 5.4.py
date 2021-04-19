
my_dic = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
with open("lesson4.txt", "w", encoding= 'utf-8') as file:
    with open ("lesson4.txt", encoding= 'utf-8') as user:
        file.writelines([line.replace(line.split()[0], my_dic.get(line.split()[0])) for line in user])

with open("Lesson1.txt", "r", encoding='utf-8') as file1:
    user = file1.readlines()
    for index, value in enumerate(user):
        num = len(value.split())
        print(f'Строка №{index} включает в себя {num} слов')
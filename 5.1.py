with open("lesson1.txt", 'w', encoding= 'utf-8') as file1:
    while True:
        user = input("Введите новую информацию или пустую строку для выхода :")
        if not user:
            break
        print(user, file=file1)
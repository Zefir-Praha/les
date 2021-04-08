user_word = input("введите слова используя пробелы: ").split()
for i, word in enumerate(user_word, 1):
    print(f"{i}.{word[:10]}")
number = [43, 12, 98, 55, 3, 4, 73, 2]
another = [number[num] for num in range(1, len(number)) if number[num] > number[num - 1]]
print(another)
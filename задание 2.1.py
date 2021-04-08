my_list = [range(22), False, [222, 52], {11: "november", 4: "april"}, (16.2, 11.1), (1, 30), "Python - the best", bytearray(b"twelve"), frozenset(), TypeError]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
print(type(my_list))
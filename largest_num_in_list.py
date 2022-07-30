numbers = [3, 5, 6, 2, 6, 7, 9, 20, 27, 2, 4, 1, 3, 7, 3, 3]
max_num = numbers[0]
for x in numbers:
    if max_num < x:
        max_num = x
print(max_num)

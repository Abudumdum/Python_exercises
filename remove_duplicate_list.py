
numbere = [3, 4, 5, 6, 3, 5, 5, 4, 6, 7, 8, 9, 0]
new_numbere = []
for number in numbere:
    if number not in new_numbere:
        new_numbere.append(number)
print(new_numbere)

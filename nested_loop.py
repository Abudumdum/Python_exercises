numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print(x * "x")
# this above method is an easier method while the one below makes use of
# nested loops


numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

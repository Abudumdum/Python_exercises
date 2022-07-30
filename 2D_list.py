# This is an example of a 2d list and how you can access iut
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# to access 2, since 2 is the second item in the first list
print(matrix[0][1])

print("List of items in the matrix")
# To print all the item in the list by item we make use of nested loops
for row in matrix:
    for items in row:
        print(items)

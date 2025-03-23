mode = input()
matrix = []
n = 12

for r in range(n):
    row = []

    for items in range(n):

        item = float(input())
        row.append(item)

    matrix.append(row)

# print(matrix)
output = 0

if mode == "S":

    for i in range(n):

        item_select = matrix[i][i+1:]
        output += sum(item_select)

    print(f"{output:.1f}")

length = 0

if mode == "M":

    for i in range(n):

        item_select = matrix[i][i+1:]
        length += len(item_select)
        output += sum(item_select)

    output = output / length

    print(f"{output:.1f}")

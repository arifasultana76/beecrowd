c = int(input())
mode = input()

matrix = []

for r in range(12):

    row = []

    for items in range(12):

        item = float(input())
        row.append(item)

    matrix.append(row)

# print(matrix)
output = 0

if mode == "S":
    for i in range(12):

        init_out = matrix[i][c]
        output += init_out
    print(f"{output:.1f}")

if mode == "M":
    for i in range(12):

        init_out = matrix[i][c]
        output += init_out

    output = output / 12
    print(f"{output:.1f}")

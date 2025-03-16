l = int(input())
mode = input()

matrix = []

for r in range(12):

    row = []

    for item in range(12):

        item_row = float(input())
        row.append(item_row)

    # print(row)
    matrix.append(row)

# print(matrix)
if mode == "S":

    output = sum(matrix[l])
    print(f"{output:.1f}")


if mode == "M":

    output = sum(matrix[l]) / 12
    print(f"{output:.1f}")

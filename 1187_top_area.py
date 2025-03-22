mode = input()
n = 12
matrix = []

for r in range(n):

    row = []

    for items in range(n):

        item = float(input())
        row.append(item)
    matrix.append(row)
# print(matrix)

output = 0
no_of_items = 0
for i in range(5):
    item_select = matrix[i][i+1:n-1-i]
    no_of_items += len(item_select)
    output += sum(item_select)

if mode == "S":

    print(f"{output:.1f}")

if mode == "M":

    output = output / no_of_items
    print(f"{output:.1f}")

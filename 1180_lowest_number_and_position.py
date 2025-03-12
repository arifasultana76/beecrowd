n = int(input())

x = []

list_x = list(map(int, input().split()))

for i in range(n):

    item_x = list_x[i]
    x.append(item_x)

min_val = min(x)
print(f"Menor valor: {min_val}")
index_min_val = x.index(min_val)
print(f"Posicao: {index_min_val}")

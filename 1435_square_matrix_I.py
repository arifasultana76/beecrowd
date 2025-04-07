while True:
    n = int(input())
    if n == 0:
        break

    matrix = [[0]*n for _ in range(n)]

    for layer in range((n + 1) // 2):
        for i in range(layer, n - layer):
            for j in range(layer, n - layer):
                matrix[i][j] = layer + 1

    for row in matrix:
        print(" ".join(f"{num:>3}" for num in row))
    print()

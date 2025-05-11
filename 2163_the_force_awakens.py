n, m = map(int, input().split())
terrain = [list(map(int, input().split())) for r in range(n)]

for i in range(1, n - 1):
    for j in range(1, m - 1):

        if terrain[i][j] == 42 and all(
            terrain[i + dx][j + dy] == 7
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        ):
            print(i + 1, j + 1)
            exit()

print(0, 0)

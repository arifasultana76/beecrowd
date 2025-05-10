n = int(input())

grid = [list(map(int, input().split())) for r in range(n + 1)]

for i in range(n):
    result = ""
    for j in range(n):

        cameras = (
            grid[i][j] +
            grid[i][j+1] +
            grid[i+1][j] +
            grid[i+1][j+1]
        )
        if cameras >= 2:
            result += 'S'
        else:
            result += 'U'
    print(result)

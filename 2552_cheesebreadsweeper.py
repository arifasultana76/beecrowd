import sys

for line in sys.stdin:
    if not line.strip():
        continue
    N, M = map(int, line.split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        row = ''
        for j in range(M):
            if board[i][j]:
                row += '9'
            else:
                row += str(sum(board[x][y] for x, y in ((i-1, j), (i+1, j),
                           (i, j-1), (i, j+1)) if 0 <= x < N and 0 <= y < M))
        print(row)

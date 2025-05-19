import sys
from collections import deque

while True:
    try:
        n, m = map(int, input().split())
        grid, start, end = [], None, None
        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
            for j in range(m):
                if row[j] == 1:
                    start = (i, j)
                elif row[j] == 2:
                    end = (i, j)
        q = deque([(start[0], start[1], 0)])
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        while q:
            x, y, d = q.popleft()
            if (x, y) == end:
                print(d)
                break
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))
    except EOFError:
        break

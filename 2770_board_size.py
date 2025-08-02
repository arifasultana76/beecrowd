import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    X, Y, M = map(int, line.split())
    for _ in range(M):
        Xi, Yi = map(int, sys.stdin.readline().split())
        if (Xi <= X and Yi <= Y) or (Yi <= X and Xi <= Y):
            print("Sim")
        else:
            print("Nao")

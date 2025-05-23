import sys

while True:
    try:
        n, q = map(int, input().split())
        grades = sorted([int(input()) for _ in range(n)], reverse=True)
        queries = [int(input()) for _ in range(q)]
        for p in queries:
            print(grades[p - 1])
    except EOFError:
        break

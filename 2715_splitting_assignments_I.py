import sys


def get_min_difference(n, tasks):
    total = sum(tasks)
    rangel = 0
    min_diff = float('inf')
    for i in range(n - 1):
        rangel += tasks[i]
        gugu = total - rangel
        diff = abs(rangel - gugu)
        min_diff = min(min_diff, diff)
    return min_diff


lines = sys.stdin.read().splitlines()
i = 0

while i < len(lines):
    if not lines[i].strip():
        i += 1
        continue

    n = int(lines[i])
    i += 1

    while i < len(lines) and not lines[i].strip():
        i += 1

    tasks = list(map(int, lines[i].split()))
    i += 1

    if n == 0:
        print(0)
    else:
        print(get_min_difference(n, tasks))

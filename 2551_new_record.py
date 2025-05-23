import sys

lines = sys.stdin.read().splitlines()
i = 0

while i < len(lines):
    n = int(lines[i])
    i += 1
    max_speed = -1
    for day in range(1, n + 1):
        t, d = map(int, lines[i].split())
        i += 1
        speed = d / t
        if speed > max_speed:
            print(day)
            max_speed = speed

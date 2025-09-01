import sys

for line in sys.stdin:
    t = int(line.strip())
    times = []
    for r in range(t):
        times.append(float(sys.stdin.readline().strip()))
    print(min(times))

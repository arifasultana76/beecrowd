import sys

for line in sys.stdin:
    try:
        N, D = map(int, line.split())
        found = False
        for _ in range(D):
            parts = sys.stdin.readline().split()
            date, availability = parts[0], list(map(int, parts[1:]))
            if sum(availability) == N and not found:
                print(date)
                found = True
        if not found:
            print("Pizza antes de FdI")
    except:
        break

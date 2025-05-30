import sys

jewels = set()

for line in sys.stdin:
    jewels.add(line.strip())

print(len(jewels))

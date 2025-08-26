import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    left, right = s.split('.', 1)
    print(f"{int(right)}.{int(left)}")

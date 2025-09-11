import sys

for line in sys.stdin:
    if line.strip() == "":
        continue
    h, m = map(int, line.split())
    hours = h // 30
    minutes = m // 6
    print(f"{hours:02d}:{minutes:02d}")

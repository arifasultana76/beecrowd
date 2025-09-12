import sys

MAX_COL = 16384

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue

    value = 0
    for c in s:
        value = value * 26 + (ord(c) - ord('A') + 1)

    if value > MAX_COL:
        print("Essa coluna nao existe Tobias!")
    else:
        print(value)

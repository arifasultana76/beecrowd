import math

c = int(input())
for r in range(c):
    n, m = map(int, input().split())
    if n == 0:
        print(1 if m == 0 else 1)   # edge case 0^0 or 0^M
    else:
        digits = int(m * math.log10(n)) + 1
        print(digits)

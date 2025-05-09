import sys
for line in sys.stdin:
    Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, line.split())
    dist = ((Xi - Xf) ** 2 + (Yi - Yf) ** 2) ** 0.5 + Vi * 1.5
    print("Y" if dist <= R1 + R2 else "N")

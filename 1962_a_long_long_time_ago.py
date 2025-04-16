n = int(input())
for r in range(n):
    t = int(input())
    year = 2015 - t
    if year > 0:
        print(f"{year} D.C.")
    else:
        print(f"{abs(year) + 1} A.C.")

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        row = []
        for j in range(n):
            value = abs(i - j) + 1
            row.append(f"{value:>3}")
        print(" ".join(row))
    print()

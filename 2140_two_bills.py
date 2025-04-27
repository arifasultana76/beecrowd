bills = [2, 5, 10, 20, 50, 100]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    change = m - n
    found = False

    for i in range(len(bills)):
        for j in range(i + 1, len(bills)):
            if bills[i] + bills[j] == change:
                found = True
                break
        if found:
            break

    print("possible" if found else "impossible")

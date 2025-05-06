while True:
    x, m = map(int, input().split())
    if x == 0 and m == 0:
        break
    if x == 1:
        print(m)
    else:
        print(m * x)

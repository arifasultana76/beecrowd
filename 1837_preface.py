a, b = map(int, input().split())

if b == 0:
    print("Divisor cannot be zero.")
else:
    q = a // b
    r = a % b

    if r < 0:
        r += abs(b)
        q = (a - r) // b

    print(q, r)
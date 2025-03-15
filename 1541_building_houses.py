while True:

    x = input().split(" ")

    if "0" in x:
        break

    a, b, c = map(int, x)

    h_a = a*b
    y = c/100
    l_a = h_a / y
    l = int(l_a**0.5)

    print(l)

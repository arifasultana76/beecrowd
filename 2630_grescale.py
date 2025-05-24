t = int(input())
for n in range(1, t + 1):
    mode = input()
    r, g, b = map(int, input().split())
    if mode == 'min':
        P = min(r, g, b)
    elif mode == 'max':
        P = max(r, g, b)
    elif mode == 'mean':
        P = (r + g + b) // 3
    elif mode == 'eye':
        P = (30 * r + 59 * g + 11 * b) // 100
    print(f"Caso #{n}: {P}")

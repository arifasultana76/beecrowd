try:
    while True:
        N, Amin, Amax = map(int, input().split())
        count = 0
        for _ in range(N):
            h = int(input())
            if Amin <= h <= Amax:
                count += 1
        print(count)
except EOFError:
    pass

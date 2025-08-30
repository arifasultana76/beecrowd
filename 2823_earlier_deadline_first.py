n = int(input())
tasks = [tuple(map(int, input().split())) for r in range(n)]

u = sum(C / P for C, P in tasks)

if u <= 1:
    print("OK")
else:
    print("FAIL")

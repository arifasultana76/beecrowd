n, m = map(int, input().split())

for _ in range(m):
    action = input().strip()
    if action == "fechou":
        n += 1
    else:
        n -= 1

print(n)

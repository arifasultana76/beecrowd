c = int(input())
for r in range(c):
    h, m, o = map(int, input().split())
    status = "A porta abriu!" if o == 1 else "A porta fechou!"
    print(f"{h:02d}:{m:02d} - {status}")

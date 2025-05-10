n = int(input())
rpm = list(map(int, input().split()))

for i in range(1, n):
    if rpm[i] < rpm[i - 1]:
        print(i + 1)
        break
else:
    print(0)

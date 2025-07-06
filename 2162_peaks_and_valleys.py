n = int(input())
h = list(map(int, input().split()))

valid = 1
for i in range(1, n):

    if h[i] == h[i - 1]:
        valid = 0
        break

    if i > 1 and ((h[i] > h[i - 1]) == (h[i - 1] > h[i - 2])):
        valid = 0
        break

print(valid)

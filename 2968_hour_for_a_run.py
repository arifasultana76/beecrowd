import math

v, n = map(int, input().split())
total = v * n
result = []

for p in range(10, 100, 10):
    result.append(math.ceil(total * p / 100))

print(*result)

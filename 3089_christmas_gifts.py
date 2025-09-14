import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    gifts = list(map(int, sys.stdin.readline().split()))

    min_sum = float('inf')
    max_sum = 0

    for i in range(n):
        pair_sum = gifts[i] + gifts[2*n - 1 - i]
        min_sum = min(min_sum, pair_sum)
        max_sum = max(max_sum, pair_sum)

    print(max_sum, min_sum)

import math

# Read number of points
N = int(input())

# Helper for combinations (n choose k)


def C(n, k):
    if n < k:
        return 0
    return math.comb(n, k)  # Python 3.8+


# Calculate regions
regions = 1 + C(N, 2) + C(N, 4)

# Output result
print(regions)

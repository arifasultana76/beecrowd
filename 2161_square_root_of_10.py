n = int(input())
fraction = 0.0

for r in range(n):
    fraction = 1 / (6 + fraction)

result = 3 + fraction
print(f"{result:.10f}")

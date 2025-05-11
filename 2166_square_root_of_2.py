n = int(input())
fraction = 0.0

for r in range(n):
    fraction = 1 / (2 + fraction)

result = 1 + fraction
print(f"{result:.10f}")

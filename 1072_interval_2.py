n = int(input())

a = 0
b = 0

for i in range(n):
    x = int(input())

    if 10 <= x <= 20:
        a += 1
    else:
        b += 1

print(f"{a} in")
print(f"{b} out")

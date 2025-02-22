x = int(input())

while True:
    z = int(input())

    if z > x:
        break

count = 0
result = 0
for i in range(x,z):
    result += i
    count += 1
    if result>z:
        break

print(count)


age = []

while True:

    n = int(input())

    if n < 0:
        break

    else:
        age.append(n)

avg = sum(age) / len(age)

print(f"{avg:.2f}")
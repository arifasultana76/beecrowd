even = []
odd = []

for i in range(15):

    n = int(input())

    if n % 2 == 0:
        even.append(n)

    else:
        odd.append(n)

    if len(even) == 5:

        count = 0
        for a in even:
            print(f"par[{count}] = {a}")
            count += 1
        even = []

    if len(odd) == 5:

        count = 0
        for b in odd:
            print(f"impar[{count}] = {b}")
            count += 1
        odd = []

if len(odd) > 0:
    count = 0
    for b in odd:
        print(f"impar[{count}] = {b}")
        count += 1

if len(even) > 0:
    count = 0
    for a in even:
        print(f"par[{count}] = {a}")
        count += 1

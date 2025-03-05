n = int(input())

for i in range(n):

    x = int(input())
    count = 0

    for j in range(1,x+1):

        if x % j == 0:
            count += 1

    if count > 2:
        print(f"{x} nao eh primo")

    else:
        print(f"{x} eh primo")

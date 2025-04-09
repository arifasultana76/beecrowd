qt = int(input())  # Total test case

for r in range(qt):
    line = input().split()
    name1 = line[0]
    choice1 = line[1]
    name2 = line[2]
    choice2 = line[3]

    n, m = map(int, input().split())
    total = n + m

    if total % 2 == 0:
        # Even number → PAR je select koreche she jite
        if choice1 == "PAR":
            print(name1)
        else:
            print(name2)
    else:
        # Odd number → IMPAR je select koreche she jite
        if choice1 == "IMPAR":
            print(name1)
        else:
            print(name2)

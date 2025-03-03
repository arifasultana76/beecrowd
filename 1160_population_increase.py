n = int(input())

for i in range(n):

    pa,pb,g1,g2 = input().split()

    Pa = int(pa)
    Pb = int(pb)
    G1 = float(g1)
    G2 = float(g2)

    count = 0

    while (Pa<=Pb):

        CPa = int(Pa*(G1/100))
        CPb = int(Pb*(G2/100))
        count += 1

        Pa += CPa
        Pb += CPb

        if count > 100:
            break

    if count > 100:
        print(f"Mais de 1 seculo.")
        
    else:
        print(f"{count} anos.")



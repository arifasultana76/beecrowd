t = int(input())

for r in range(t):
    b = int(input())

    Ad, Dd, Ld = map(int, input().split())

    Ag, Dg, Lg = map(int, input().split())

    Vd = (Ad + Dd) / 2
    if Ld % 2 == 0:
        Vd += b

    Vg = (Ag + Dg) / 2
    if Lg % 2 == 0:
        Vg += b

    if Vd > Vg:
        print("Dabriel")
    elif Vg > Vd:
        print("Guarte")
    else:
        print("Empate")

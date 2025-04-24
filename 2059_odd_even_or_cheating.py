p, j1, j2, r, a = map(int, input().split())

if r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif r == 0 and a == 1:
    print("Jogador 1 ganha!")
else:

    total = j1 + j2
    if total % 2 == 0:
        if p == 1:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        if p == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")

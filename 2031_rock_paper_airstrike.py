n = int(input())

for _ in range(n):
    p1 = input().strip()
    p2 = input().strip()

    if p1 == p2:
        if p1 == "ataque":
            print("Aniquilacao mutua")
        elif p1 == "pedra":
            print("Sem ganhador")
        else:
            print("Ambos venceram")
    elif (p1 == "ataque" and p2 in ["pedra", "papel"]) or (p1 == "pedra" and p2 == "papel"):
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")

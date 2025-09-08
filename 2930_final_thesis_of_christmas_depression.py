E, D = map(int, input().split())

if E > D:
    print("Eu odeio a professora!")
elif (D - E) >= 3:
    print("Muito bem! Apresenta antes do Natal!")
else:
    print("Parece o trabalho do meu filho!")
    if (D + 2) <= 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")

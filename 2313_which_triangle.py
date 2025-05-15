a, b, c = sorted(map(int, input().split()))

if a + b > c:
    if a == b == c:
        print("Valido-Equilatero")
    elif a == b or b == c:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    print("Retangulo: S" if a * a + b * b == c * c else "Retangulo: N")
else:
    print("Invalido")

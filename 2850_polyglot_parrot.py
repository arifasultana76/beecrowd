while True:
    try:
        s = input().strip()
        if s == "esquerda":
            print("ingles")
        elif s == "direita":
            print("frances")
        elif s == "nenhuma":
            print("portugues")
        elif s == "as duas":
            print("caiu")
    except EOFError:
        break

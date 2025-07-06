try:
    while True:
        N = int(input())
        M, L = map(int, input().split())
        marcos = [list(map(int, input().split())) for _ in range(M)]
        leonardo = [list(map(int, input().split())) for _ in range(L)]
        CM, CL = map(int, input().split())
        A = int(input())

        m_attr = marcos[CM - 1][A - 1]
        l_attr = leonardo[CL - 1][A - 1]

        if m_attr > l_attr:
            print("Marcos")
        elif l_attr > m_attr:
            print("Leonardo")
        else:
            print("Empate")
except EOFError:
    pass

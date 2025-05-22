import sys

for input_line in sys.stdin:
    N = int(input_line)
    M, L = map(int, sys.stdin.readline().split())
    marcos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    leonardo = [list(map(int, sys.stdin.readline().split())) for _ in range(L)]
    CM, CL = map(int, sys.stdin.readline().split())
    A = int(sys.stdin.readline())

    m_attr = marcos[CM - 1][A - 1]
    l_attr = leonardo[CL - 1][A - 1]

    print("Marcos" if m_attr > l_attr else "Leonardo" if l_attr >
          m_attr else "Empate")

n = int(input())
S_total = B_total = A_total = S1_total = B1_total = A1_total = 0

for r in range(n):
    input()
    S, B, A = map(int, input().split())
    S1, B1, A1 = map(int, input().split())
    S_total += S
    B_total += B
    A_total += A
    S1_total += S1
    B1_total += B1
    A1_total += A1

print(f"Pontos de Saque: {S1_total / S_total * 100:.2f} %.")
print(f"Pontos de Bloqueio: {B1_total / B_total * 100:.2f} %.")
print(f"Pontos de Ataque: {A1_total / A_total * 100:.2f} %.")

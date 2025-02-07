matches = 0
inter = 0
gremio = 0
draw = 0

while True:
    i,g = map(int,input().split())

    if i > g:
        inter += 1
    elif i < g:
        gremio +=1
    elif i == g:
        draw += 1

    matches += 1

    print("Novo grenal (1-sim 2-nao)")
    check = int(input())

    if check == 2:
        break

print(f"{matches} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{draw}")

if inter == gremio:
    print("Não houve vencedor")

else:
    if inter > gremio:
        print("Inter venceu mais")

    else:
        print("Gremio venceu mais")
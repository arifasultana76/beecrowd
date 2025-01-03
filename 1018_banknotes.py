n = int(input())

banknotes =[100,50,20,10,5,2,1]

print(f"{n}")

for note in banknotes:

    count = n // note

    print(f"{count} nota(s) de R$ {note},00")

    n %= note

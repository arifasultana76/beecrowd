import sys

b = {'pedra': 'tesoura', 'tesoura': 'papel', 'papel': 'pedra'}
m = [
    "Os atributos dos monstros vao ser inteligencia, sabedoria...",
    "Iron Maiden's gonna get you, no matter how far!",
    "Urano perdeu algo muito precioso...",
    "Putz vei, o Leo ta demorando muito pra jogar..."
]

for l in sys.stdin:
    d, l_, p = l.split()
    if b[d] == l_ == p:
        print(m[0])
    elif b[l_] == d == p:
        print(m[1])
    elif b[p] == d == l_:
        print(m[2])
    else:
        print(m[3])

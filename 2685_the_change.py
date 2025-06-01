import sys

for line in sys.stdin:
    m = int(line)
    if 0 <= m < 90 or m == 360:
        print("Bom Dia!!")
    elif 90 <= m < 180:
        print("Boa Tarde!!")
    elif 180 <= m < 270:
        print("Boa Noite!!")
    else:
        print("De Madrugada!!")

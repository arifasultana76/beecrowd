sides = list(map(float,input().split()))

sides.sort(reverse=True)

a = sides[0]
b = sides[1]
c = sides[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")

elif a*a == b*b + c*c:
    print("TRIANGULO RETANGULO")

elif a*a > b*b + c*c:
    print("TRIANGULO OBTUSANGULO")

elif a*a < b*b + c*c:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")

elif a == b or b == c or c == a:
    print("TRIANGULO ISOSCELES")


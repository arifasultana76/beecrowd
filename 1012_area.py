
a, b, c = map(float, input().split())

pi = 3.14159

area_of_the_rectangled_triangle = 0.5 * a * c
area_of_circle = pi * c**2
area_of_trapezium = 0.5 * (a+b) * c
area_of_square = b**2
area_of_rectangle = a*b 

print(f"TRIANGULO: {area_of_the_rectangled_triangle:.3f}")
print(f"CIRCULO: {area_of_circle:.3f}")
print(f"TRAPEZIO: {area_of_trapezium:.3f}")
print(f"QUADRADO: {area_of_square:.3f}")
print(f"RETANGULO: {area_of_rectangle:.3f}")

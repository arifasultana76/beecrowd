alcohol = 0
gasoline = 0
diesel = 0

while True:
    n = int(input())

    if n == 1:
        alcohol += 1
    if n == 2:
        gasoline += 1
    if n == 3:
        diesel += 1
    if n == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcohol}")
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")

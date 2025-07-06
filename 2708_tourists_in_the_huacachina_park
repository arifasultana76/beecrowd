total_jeeps = 0
total_tourists = 0

while True:
    line = input()
    if line == "ABEND":
        break

    action, number = line.split()
    number = int(number)

    if action == "SALIDA":
        total_jeeps += 1
        total_tourists += number
    elif action == "VUELTA":
        total_jeeps -= 1
        total_tourists -= number

print(total_tourists)
print(total_jeeps)

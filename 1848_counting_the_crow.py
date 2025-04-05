count = 0
total = 0

while count < 3:
    line = input()
    if line == "caw caw":
        print(total)
        total = 0
        count += 1
    else:
        value = 0
        if line[0] == '*':
            value += 4
        if line[1] == '*':
            value += 2
        if line[2] == '*':
            value += 1
        total += value

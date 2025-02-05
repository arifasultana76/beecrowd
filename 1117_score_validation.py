valid = []

while True:

    for i in range(1):

        x = float(input())

        if 0<=x<=10:
            valid.append(x)

        else:
            print("nota invalida")

    if len (valid) == 2:

            avg = sum(valid) / 2
            print(f"media = {avg:.2f}")
            break

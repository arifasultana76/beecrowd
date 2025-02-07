while True:
    valid = []  

    while len(valid) < 2:
        x = float(input())

        if 0 <= x <= 10:
            valid.append(x)
        else:
            print("nota invalida")

    avg = sum(valid) / 2 
    print(f"media = {avg:.2f}")

    while True:  
        print("novo calculo (1-sim 2-nao)")
        check = int(input())

        if check == 1 or check == 2:
            break 

    if check == 2:
        break 



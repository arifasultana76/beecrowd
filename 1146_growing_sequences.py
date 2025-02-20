while True:
    
    x = int(input())

    if x == 0:
        break

    output = ""
    for i in range(1,x+1):
        output += str(i) + " "
    
    print(output[:-1])
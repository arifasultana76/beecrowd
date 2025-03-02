while True:

    x = int(input())

    if x == 0:
        break
    else:

        even_num = []
        count = 0

        while (count<5):

            if x % 2 == 0:
                even_num.append(x)
                count += 1
            x += 1

        output = sum (even_num)
        print(output)

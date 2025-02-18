n1, n2 = map(int,input().split())

count = 1
col = int(n2/n1) + 1
#column for loop
for i in range(1,col):
    r = ""
    #row for loop

    for j in range(n1):
        r += str (count) + " "
        count += 1
    print(r[:-1])


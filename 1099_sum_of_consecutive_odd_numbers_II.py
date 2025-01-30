n = int(input())

for i in range(n):
    x, y = map(int, input().split())


    a= min(x,y)
    b= max(x,y)

    t_list = []

    for j in range(a+1,b):
        if (j % 2) !=0:

            t_list.append(j)

    total = sum(t_list)
    print(total)

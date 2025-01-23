while True:
    m,n = map(int,input().split())


    if (m<=0) or (n<=0):
        break
    else:
        result =[]

        a = min(m,n)
        b = max(m,n)

        for i in range(a,b+1):
            result.append(i)

        output = " ".join(map(str,result))
        print(f"{output} Sum={sum(result)}")

   
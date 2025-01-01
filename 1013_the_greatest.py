a,b,s = map(int,input().split())

maiorAB = (a+b+abs(a-b)) // 2           # double slash dile floating digit ashbe na. intiger digit a ans hobe.
maiorFinal = (maiorAB + s + abs(maiorAB - s)) // 2   #greatest ber korte bolle ae 2 ta formula use hobe. 
                                                  
print(f"{maiorFinal} eh o maior")         # here's abs substractor(jog biyog korar por jodi digit er age minus value ashe tokhn sei minus r ashbe na.)
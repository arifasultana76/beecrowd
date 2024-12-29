a,b,s = map(int,input().split())

MaiorAB = (a+b+abs(a-b)) // 2
MaiorFinal = (MaiorAB + s + abs(MaiorAB - s)) // 2   

print(f"{MaiorFinal} eh o maior")
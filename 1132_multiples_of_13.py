result= []

x = int(input())
y = int(input())

a = min(x,y)
b = max(x,y)

for i in range(a,b+1):

    if i % 13 != 0:
        result.append(i)

output = sum(result)   
print(output)
 
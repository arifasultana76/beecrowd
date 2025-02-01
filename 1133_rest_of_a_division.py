x = int(input())
y = int(input())

a = min(x,y)
b = max(x,y)

for i in range(a+1,b):
    if (i % 5 == 2) or (i % 5 == 3):
        print(i)
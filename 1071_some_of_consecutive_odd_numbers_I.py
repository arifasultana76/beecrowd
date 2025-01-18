x = int(input())
y = int(input())

start = min(x,y)
end = max(x,y)

sum = 0
for i in range(start+1,end):
    if i % 2 !=0:
        sum +=i

print(sum)
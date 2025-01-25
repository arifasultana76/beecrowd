n = int(input())

for i in range (n):
    a,b,c = map(float,input().split())

    avg = ((a*2) + (b*3) + (c*5)) / 10
    print(f"{avg:.1f}")

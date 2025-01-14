def myrange(start,end,step):
    i = start
    while i < end:
            yield i
            i += step
    yield end

for i in myrange(2,100,2):
    print(i)
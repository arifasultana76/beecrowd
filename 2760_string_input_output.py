# Read 3 strings (phrases up to 100 characters)
a = input()
b = input()
c = input()

# First combination: A + B + C
print(a + b + c)

# Second combination: B + C + A
print(b + c + a)

# Third combination: C + A + B
print(c + a + b)

# Fourth: print only the first 10 characters of each (or full if shorter)
print(a[:10] + b[:10] + c[:10])

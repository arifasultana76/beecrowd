n = int(input())

for r in range(n):
    x = int(input())
    binary = bin(x)[2:]  # Convert to binary string without '0b'
    max_ones = max(map(len, binary.split('0')))
    print(max_ones)

n = int(input())

sequence = [0,1]
result = 0

for i in range(n-2):

    result = sequence[-1] + sequence[-2]
    sequence.append(result)

print(' '.join(map(str,sequence)))
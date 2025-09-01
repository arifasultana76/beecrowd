import sys

data = sys.stdin.read().split()
n = int(data[0])
wins = sum(1 for x in data[1:1+n] if x != '1')
print(wins)

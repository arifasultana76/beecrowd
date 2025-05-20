import sys

while True:
    try:
        letters = input()
        n = int(input())
        bulbs = list(map(int, input().split()))
        message = ''.join(letters[b - 1] for b in bulbs)
        print(message)
    except EOFError:
        break

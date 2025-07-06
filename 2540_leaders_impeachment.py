import sys

while True:
    try:
        n = int(input())
        votes = list(map(int, input().split()))
        if sum(votes) * 3 >= 2 * n:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break

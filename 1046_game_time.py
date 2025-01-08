start_t, end_t = map(int,input().split())

if start_t > end_t:
    duration = 24 - (start_t - end_t)
    print(f"O JOGO DUROU {duration} HORA(S)")

elif end_t > start_t:
    duration = end_t - start_t
    print(f"O JOGO DUROU {duration} HORA(S)")

elif start_t == end_t:
    print(f"O JOGO DUROU 24 HORA(S)")
i_hr, i_min, f_hr, f_min = map(int,input().split())

duration = ((f_hr*60)+f_min)-((i_hr*60)+i_min)

if duration <= 0:
    duration += 24*60

hr = duration // 60
min = duration % 60

print(f"O JOGO DUROU {hr} HORA(S) E {min} MINUTO(S)")
n1, n2, n3, n4 = map(float,input().split())

avg1 = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / (2+3+4+1)

print(f"Media: {avg1:.1f}")

if avg1 > 7:
    print("Aluno aprovado.")
elif avg1 < 5:
    print("Aluno reprovado.")
elif 5 <= avg1 <= 6.9:
    print("Aluno em exame.") 
    new_score = float(input())
    print(f"Nota do exame: {new_score:.1f}")

    avg2 = (new_score + avg1) / 2

    if avg2 >= 5:
        print("Aluno aprovado.")
    elif avg2 <= 4.9:
        print(f"Aluno reprovado.")
    
    print(f"Media final: {avg2:.1f}")
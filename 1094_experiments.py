rabbit = []
rat = []
frog = []

num_of_test_case = int(input())

for i in range(num_of_test_case):

    amount,type = input().split()
    amount = int(amount)

    if 1<= amount <= 15:

        if type == "C":
            rabbit.append(amount)

        if type == "R":
            rat.append(amount)

        if type == "S":
            frog.append(amount)

t_rabbit = sum(rabbit)
t_rat = sum(rat)
t_frog = sum(frog)
t_animals = t_rabbit + t_rat + t_frog

if t_animals > 0:
    p_rabbit = (t_rabbit / t_animals)*100
    p_rat = (t_rat / t_animals)*100
    p_frog = (t_frog / t_animals)*100
else:
    p_rabbit = p_rat = p_frog = 0.0

print(f"Total: {t_animals} cobaias")
print(f"Total de coelhos: {t_rabbit}")
print(f"Total de ratos: {t_rat}")
print(f"Total de sapos: {t_frog}")
print(f"Percentual de coelhos: {p_rabbit:.2f} %")
print(f"Percentual de ratos: {p_rat:.2f} %")
print(f"Percentual de sapos: {p_frog:.2f} %")
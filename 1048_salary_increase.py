old_salary = float(input())

lb = [0, 400, 800, 1200, 2000] 
ub = [400, 800, 1200,2000]
rate = [15, 12, 10, 7, 4]

for i in range(len(lb)):
    
    if old_salary > lb[4]:
        increment = rate[4]*0.01*old_salary
        j = 4

    elif lb[i] < old_salary <= ub[i]:
        increment = rate[i]*0.01*old_salary
        j = i

new_salary = increment + old_salary

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {increment:.2f}")
print(f"Em percentual: {rate[j]} %")


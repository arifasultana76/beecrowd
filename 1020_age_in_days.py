a = int(input())

years = a // 365
remaining_days = a % 365
months = remaining_days // 30
days = remaining_days % 30

print(f"{years} ano(s)")
print(f"{months} mes(es)")     
print(f"{days} dia(s)")
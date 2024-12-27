sellers_name = input()
monthly_fixed_salary = float(input())
sales_total = float(input())

commission_sales = sales_total * 0.15


total_salary = (monthly_fixed_salary + commission_sales)

print(f"TOTAL = R$ {total_salary:.2f}")





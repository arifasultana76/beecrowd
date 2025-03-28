salary = float(input())

if 0 < salary <= 2000:

    print("Isento")

elif 2000 < salary <= 3000:
    tax_on_salary = salary - 2000
    tax_to_pay = tax_on_salary*8*0.01
    print(f"R$ {tax_to_pay:.2f}")

elif 3000 < salary <= 4500:
    tax_on_salary1 = salary - 2000
    tax_on_salary2 = tax_on_salary1 - 1000

    tax_to_pay1 = 1000*8*0.01
    tax_to_pay2 = tax_on_salary2*18*0.01
    total_tax = tax_to_pay1 + tax_to_pay2

    print(f"R$ {total_tax:.2f}")

else:
    tax_on_salary1 = salary - 2000
    tax_on_salary2 = tax_on_salary1 - 1000 - 1500

    tax_to_pay1 = 1000*8*0.01
    tax_to_pay2 = 1500*18*0.01
    tax_to_pay3 = tax_on_salary2*28*0.01
    total_tax = tax_to_pay1 + tax_to_pay2 + tax_to_pay3

    print(f"R$ {total_tax:.2f}")

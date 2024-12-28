product_1,unit_number_of_product_1 ,price_for_one_unit_1 = input().split()   
product_1,unit_number_of_product_1 ,price_for_one_unit_1 = int(product_1), int(unit_number_of_product_1),float(price_for_one_unit_1)

product_2,unit_number_of_product_2 ,price_for_one_unit_2 = input().split()
product_2,unit_number_of_product_2 ,price_for_one_unit_2 = int(product_2), int(unit_number_of_product_2),float(price_for_one_unit_2)

total_amount = (unit_number_of_product_1 * price_for_one_unit_1) + (unit_number_of_product_2 * price_for_one_unit_2)

print(f"VALOR A PAGAR: R$ {total_amount:.2f}")
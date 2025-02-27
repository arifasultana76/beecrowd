s_list = []

divisor = 1
power = 0

while (divisor<40):
    dividend = 2**power

    s = divisor / dividend
    s_list.append(s)

    divisor += 2
    power += 1

result = sum(s_list)
print(f"{result:.2f}")
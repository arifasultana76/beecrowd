s_list = []

for i in range(1,101):

    s = 1/i

    s_list.append(s)

result = sum(s_list)
print(f"{result:.2f}")
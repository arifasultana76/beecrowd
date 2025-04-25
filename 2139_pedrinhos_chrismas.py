days_in_month = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

while True:
    try:
        line = input()
        if not line.strip():
            continue
        month, day = map(int, line.split())
        today = days_in_month[month - 1] + day
        christmas = 360
        diff = christmas - today

        if diff == 0:
            print("E natal!")
        elif diff == 1:
            print("E vespera de natal!")
        elif diff < 0:
            print("Ja passou!")
        else:
            print(f"Faltam {diff} dias para o natal!")
    except EOFError:
        break

n = int(input().strip())
buy_home, buy_office = 0, 0
home, office = 0, 0

for _ in range(n):
    morning, evening = input().split()

    if morning == "chuva":
        if home > 0:
            home -= 1
            office += 1
        else:
            buy_home += 1
            office += 1

    if evening == "chuva":
        if office > 0:
            office -= 1
            home += 1
        else:
            buy_office += 1
            home += 1

print(buy_home, buy_office)

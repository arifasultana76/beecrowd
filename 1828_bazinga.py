t = int(input())

win_map = {
    'tesoura': ['papel', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'pedra': ['lagarto', 'tesoura'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}

for i in range(1, t + 1):
    sheldon, raj = input().split()

    if sheldon == raj:
        result = "De novo!"
    elif raj in win_map[sheldon]:
        result = "Bazinga!"
    else:
        result = "Raj trapaceou!"

    print(f"Caso #{i}: {result}")

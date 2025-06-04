import sys


def get_greeting(hour):
    if 6 <= hour < 12:
        return "Bom Dia!!"
    elif 12 <= hour < 18:
        return "Boa Tarde!!"
    elif 18 <= hour < 24:
        return "Boa Noite!!"
    else:
        return "De Madrugada!!"


for line in sys.stdin:
    try:
        m = float(line.strip())
    except:
        continue

    adjusted_degree = (m + 90) % 360

    total_seconds = int(adjusted_degree * 240 + 0.00001)

    hour = (total_seconds // 3600) % 24
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60

    print(get_greeting(hour))
    print(f"{hour:02d}:{minute:02d}:{second:02d}")

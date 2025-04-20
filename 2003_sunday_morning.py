while True:
    try:
        time = input()
        hour, minute = map(int, time.split(":"))

        wake_minutes = hour * 60 + minute
        delay = max(0, wake_minutes - 420)

        print(f"Atraso maximo: {delay}")
    except EOFError:
        break

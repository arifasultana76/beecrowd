while True:
    try:
        date_input = input().strip()  # Read input like "02/08/10"
        dd, mm, yy = date_input.split('/')

        print(f"{mm}/{dd}/{yy}")  # MM/DD/YY
        print(f"{yy}/{mm}/{dd}")  # YY/MM/DD
        print(f"{dd}-{mm}-{yy}")  # DD-MM-YY

    except EOFError:
        break

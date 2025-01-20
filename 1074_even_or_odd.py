n = int(input())

string1 = ""
string2 = ""

for i in range(n):
    val = int(input())

    if val == 0:
        print("NULL")

    else:
        if val % 2 == 0:
            string1 = "EVEN"
        else:
            string1 = "ODD"
        if val > 0:
            string2 = "POSITIVE"
        if val < 0:
            string2 = "NEGATIVE"

        print(f"{string1} {string2}")
   
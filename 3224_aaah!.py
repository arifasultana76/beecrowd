def jon_marius():
    jon = input().strip()
    doctor = input().strip()

    if len(jon) >= len(doctor):
        print("go")
    else:
        print("no")


if __name__ == "__main__":
    jon_marius()

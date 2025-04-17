n = int(input())  # Number of students

highest_note = -1
best_registration = -1

for r in range(n):
    reg, note = input().split()
    reg = int(reg)
    note = float(note)

    if note > highest_note:
        highest_note = note
        best_registration = reg

# Check if highest note is at least 8
if highest_note >= 8.0:
    print(best_registration)
else:
    print("Minimum note not reached")

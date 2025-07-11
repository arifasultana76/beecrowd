import re


def get_restriction_day(plate):
    # Regex pattern for valid plate: three uppercase letters, hyphen, four digits
    pattern = r'^[A-Z]{3}-\d{4}$'

    if not re.match(pattern, plate):
        return "FAILURE"

    last_digit = plate[-1]

    if last_digit in '12':
        return "MONDAY"
    elif last_digit in '34':
        return "TUESDAY"
    elif last_digit in '56':
        return "WEDNESDAY"
    elif last_digit in '78':
        return "THURSDAY"
    elif last_digit in '90':
        return "FRIDAY"
    else:
        return "FAILURE"  # Just in case


# Reading input
n = int(input())
for _ in range(n):
    plate = input().strip()
    print(get_restriction_day(plate))

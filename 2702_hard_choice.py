# Read available meals
Ca, Ba, Pa = map(int, input().split())

# Read requested meals
Cr, Br, Pr = map(int, input().split())

# Calculate shortages
missed_chicken = max(0, Cr - Ca)
missed_beef = max(0, Br - Ba)
missed_pasta = max(0, Pr - Pa)

# Total unfulfilled meal requests
total_missed = missed_chicken + missed_beef + missed_pasta

print(total_missed)

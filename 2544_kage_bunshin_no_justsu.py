import sys
for line in sys.stdin:
    print((int(line).bit_length() - 1))

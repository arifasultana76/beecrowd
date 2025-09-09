import sys
import struct

data = sys.stdin.read().strip().split()
if len(data) < 4:
    sys.exit(0)

A = float(data[0])
B = float(data[1])
C = float(data[2])
D = float(data[3])

# emulate C float (single precision) for A and B
A32 = struct.unpack('f', struct.pack('f', A))[0]
B32 = struct.unpack('f', struct.pack('f', B))[0]

# six decimals (default %f)
print(f"A = {A32:f}, B = {B32:f}")
print(f"C = {C:f}, D = {D:f}")

# 1 decimal place
print(f"A = {A32:.1f}, B = {B32:.1f}")
print(f"C = {C:.1f}, D = {D:.1f}")

# 2 decimal places
print(f"A = {A32:.2f}, B = {B32:.2f}")
print(f"C = {C:.2f}, D = {D:.2f}")

# 3 decimal places
print(f"A = {A32:.3f}, B = {B32:.3f}")
print(f"C = {C:.3f}, D = {D:.3f}")

# 3 decimal places scientific notation with 'E'
print(f"A = {A32:.3E}, B = {B32:.3E}")
print(f"C = {C:.3E}, D = {D:.3E}")

# integer part (rounded as in printf("%.0f"))
print(f"A = {A32:.0f}, B = {B32:.0f}")
print(f"C = {C:.0f}, D = {D:.0f}")

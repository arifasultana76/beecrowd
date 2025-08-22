import sys
import math


def sensor_accuracy(values):
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    return math.sqrt(variance)


data = sys.stdin.read().strip().splitlines()
i = 0
while i < len(data):

    H, M = map(int, data[i].split())
    i += 1

    values = list(map(float, data[i].split()))
    i += 1
    result = sensor_accuracy(values)
    print(f"{result:.5f}")

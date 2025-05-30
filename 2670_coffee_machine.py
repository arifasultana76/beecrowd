a1 = int(input())
a2 = int(input())
a3 = int(input())

time1 = 0 * a1 + 1 * a2 * 2 + 2 * a3 * 2

time2 = 1 * a1 * 2 + 0 * a2 + 1 * a3 * 2

time3 = 2 * a1 * 2 + 1 * a2 * 2 + 0 * a3


print(min(time1, time2, time3))

# n = int(input())
# sheep = list(map(int, input().split()))

# visited = [0] * n  # Attack count tracker
# i = 0

# while 0 <= i < n:
#     if sheep[i] > 0:
#         sheep[i] -= 1  # Steal 1 sheep
#     if visited[i] == 0:
#         visited[i] = 1  # Mark as attacked

#     # Check the number BEFORE stealing: (sheep[i] + 1)
#     if (sheep[i] + 1) % 2 == 1:  # if odd
#         i += 1
#     else:  # if even
#         i -= 1

# # Output
# total_attacked = sum(visited)
# remaining_sheep = sum(sheep)
# print(f"{total_attacked} {remaining_sheep}")


n = int(input())
sheep = list(map(int, input().split()))

visited = [0] * n
i = 0

while 0 <= i < n and sheep[i] > 0:
    visited[i] = 1
    if sheep[i] % 2 == 0:
        sheep[i] -= 1
        i -= 1
    else:
        sheep[i] -= 1
        i += 1

attacked_farms = sum(visited)
remaining_sheep = sum(sheep)

print(f"{attacked_farms} {remaining_sheep}")

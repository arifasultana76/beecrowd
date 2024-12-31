spent_time_of_trip = int(input())
avg_speed_of_trip = int(input())

distance = spent_time_of_trip * avg_speed_of_trip
fuel_need = distance / 12

print(f"{fuel_need:.3f}")
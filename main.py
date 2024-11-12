# Exercise 16: Calculate Travel Time
distance = float(input("Enter the distance to travel in km: "))
speed = float(input("Enter the average speed of the car in km/h: "))

travel_time_hours = distance / speed

travel_time_minutes = (travel_time_hours - int(travel_time_hours)) * 60
travel_time_minutes = round(travel_time_minutes)

print(f"The estimated travel time is: {int(travel_time_hours)} hours and {travel_time_minutes} minutes.")

if speed > 120:
    print("Warning! The speed is over 120 km/h.")



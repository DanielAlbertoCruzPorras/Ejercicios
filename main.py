# Exercise 21: Parking Fee System with Progressive Rates
hours = int(input("Enter the number of hours parked: "))

if hours == 1:
    cost = 5
elif 2 <= hours <= 4:
    cost = 5 + (hours - 1) * 4  # First hour is $5, then $4 per hour for 2-4 hours
else:
    cost = 5 + (3 * 4) + (hours - 4) * 3  # First hour is $5, next 3 hours are $4, then $3 per hour for more than 4 hours

print(f"The total parking cost is: ${cost}")

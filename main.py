# Exercise 18: University Credit Evaluation System
num_courses = int(input("Enter the number of courses taken: "))
total_credits = 0

for i in range(num_courses):
    score = float(input(f"Enter the score for course {i + 1}: "))
    if score >= 60:
        total_credits += 3  # Each passed course gives 3 credits

print(f"The total number of credits earned is: {total_credits}")


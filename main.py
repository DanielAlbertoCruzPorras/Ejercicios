# Exercise 17: Grading System with Bonuses
grade = float(input("Enter the student's grade (0-100): "))
extra_tasks = input("Did the student do extra tasks? (yes/no): ").strip().lower()

if extra_tasks == "yes":
    grade += grade * 0.05  # Add 5% bonus
    if grade > 100:
        grade = 100  # Ensure the grade doesn't exceed 100

print(f"The final grade is: {grade:.2f}")



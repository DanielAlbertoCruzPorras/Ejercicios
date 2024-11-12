# Exercise 20: Convert Numerical Grade to Letter Grade
grade = float(input("Enter the numerical grade (0-100): "))

match grade:
    case grade if 90 <= grade <= 100:
        letter = "A"
    case grade if 80 <= grade < 90:
        letter = "B"
    case grade if 70 <= grade < 80:
        letter = "C"
    case grade if 60 <= grade < 70:
        letter = "D"
    case _:
        letter = "F"

print(f"The letter grade is: {letter}")

# Exercise 12: BMI (Body Mass Index) Calculator
weight = float(input("Enter your weight in kg: ")) #Peso
height = float(input("Enter your height in meters: ")) #Altura

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal weight"
elif 25 <= bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obesity"

print(f"Your BMI is {bmi:.2f}. Weight status: {status}")





# Exercise 15: Calculate Net Salary
gross_salary = float(input("Enter your gross salary: "))
country = input("Enter your country of residence: ").strip().upper()

if country == "COUNTRY A":
    tax_rate = 0.20
elif country == "COUNTRY B":
    tax_rate = 0.15
elif country == "COUNTRY C":
    tax_rate = 0.10
else:
    tax_rate = 0.25  # Apply 25% tax if the country is not listed

net_salary = gross_salary * (1 - tax_rate)

print(f"Your net salary is: {net_salary:.2f}")



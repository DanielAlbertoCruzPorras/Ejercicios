# Exercise 22: Triangle Classification by Angles
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))

if angle1 < 90 and angle2 < 90 and angle3 < 90:
    triangle_type = "Acute triangle"
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    triangle_type = "Right triangle"
else:
    triangle_type = "Obtuse triangle"

print(f"The triangle is: {triangle_type}")

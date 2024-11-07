# Exercise 11: Temperature conversion
temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ").upper()

match scale:
    case "C":
        # Convert Celsius to Fahrenheit
        converted_temp = (temperature * 9/5) + 32
        print(f"{temperature}°C is equal to {converted_temp}°F.")
    case "F":
        # Convert Fahrenheit to Celsius
        converted_temp = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {converted_temp}°C.")
    case _:
        print("Invalid scale entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")





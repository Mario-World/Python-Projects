#temperature 

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip()
temp = float(input("Enter your temperature: "))

if unit == "F": 
    temp =  round((9 * temp) / 5 + 32, 1)
    print(f"Your temperature in Fahrenheit is: {temp}°F")
elif unit == "C": 
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")    
else: 
    print(f"{unit} is an invalid unit of measurement")
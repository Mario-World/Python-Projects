
# 
# python weight conversion 

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").strip()

if unit =="K": 
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your Weight is: {round(weight, 1)} {unit}") 
elif  unit == "L": 
    weight = weight / 2.205 
    unit ="Kgs"
    print(f"Your Weight is: {round(weight, 1)} {unit}") 
else: 
    print(f"{unit} was not valid")
    

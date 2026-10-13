#python weight converter

weight = float(input("Enter weight in pounds: "))
unit=input("Enter the unit to convert to (kg or lbs): ")

if unit == "kg":
    converted_weight = weight * 0.453592
    print(f"Weight in kg: {converted_weight}")
elif unit == "lbs":
    converted_weight = weight
    print(f"Weight in lbs: {converted_weight}")
else:
    print("Invalid unit. Please enter 'kg' or 'lbs'.")
print("Thank you for using the weight converter!")

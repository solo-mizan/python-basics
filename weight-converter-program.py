# weight converter program

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pound? (K or L): " )

if unit.lower() == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit.lower() == "l":
    unit = "Kgs"
    weight = weight / 2.205
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")
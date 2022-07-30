weight = float(input("WEIGHT: "))
unit = input("(L)bs or (K)g: ")
new_kg_weight = weight * 0.453492
new_lbs_weight = weight * 2.20462
if unit.upper() == "L":
    print(str(new_kg_weight) + "Kg")
elif unit.upper() == "K":
    print(str(new_lbs_weight) + "lbs")
else:
    print("Please enter a valid unit 'K' or 'l'!")

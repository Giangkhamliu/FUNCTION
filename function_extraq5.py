# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
def mass(weight,height):
    bmi=weight/(height*height)
    print(bmi)
    if bmi>30:
        return "Obese"
    elif bmi<=18.5:
        return "Underweight"
    elif bmi<=25.0:
        return ("Normal")
    elif bmi<=30.0:
        return "Overweight"
    else:
        pass
weight=float(input("Enter the weight:-"))
height=float(input("Enter the height:-"))
print(mass(weight,height))

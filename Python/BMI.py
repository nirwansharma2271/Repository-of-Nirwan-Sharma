weight=int(input("Enter your weight:"))
height=float(input("Enter your height:"))
unit=input("enter the unit's initial for your height:")
if unit=="cm":
    value=height/100
elif unit=="m":
    value=height/1
elif unit=="ft":
    value=height/3.281
else:
    print("couldn't recognise")
BMI=weight/(value)**2
print("BMI:",BMI)
if BMI<18.5:
    print("underweight")
elif BMI<24.9:
    print("Normal weight")
elif BMI<29.9:
    print("Over weight")
else:
    print("obese")

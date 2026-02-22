kg = int(input("Please enter your weight in kg"))
h = float(input("please enter your height in meters"))

h2 = h*h
bmi = kg/h2

print("you bmi is", bmi)

if bmi<18.5:
    print("you are under weight")
if 18.5<bmi<24.9:
    print("you have a healthy weight")
if bmi>25:
    print("you are over weight")

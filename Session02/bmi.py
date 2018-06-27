height_in_cm = float(input (" height (cm): "))
height = height_in_cm/100
weight = float(input (" weight (kg): "))

bmi = weight/(height*height) 



if bmi < 16:
    print ("Severely underweight")
elif bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print ("Normal")
elif bmi < 30:
    print ("Overweight")
else:
    print ("Obese")
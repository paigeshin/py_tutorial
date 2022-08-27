height = input("enter you height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2 
bmi_as_int = int(bmi)

print("Your BMI is " + str(bmi_as_int))
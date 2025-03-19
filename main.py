# BMI-Calculator

# BMI Formula= (weight * 730) / (height * height)


weight = float(input("Enter your weight in pounds: "))

height = float(input("Enter your height in inches: "))

bmi = (weight * 730) / (height * height)
print(f'Your BMI is {round(bmi, 1)}')

if bmi > 0:
    if bmi < 18.5:
        print("Your BMI is Underweight")

    elif bmi < 24.9:
        print("Your BMI is Normal")

    elif bmi < 29.9:
        print("Your BMI is Overweight")

    elif bmi < 39.9:
        print('Your BMI is Obese')

    else:
        print("Your BMI is Morbidly Obese")

else:
    print("Enter a Valid Input")

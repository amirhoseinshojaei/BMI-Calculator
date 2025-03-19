# 📊 BMI Calculator

A simple **Body Mass Index (BMI) Calculator** built in Python.  
This tool helps you determine whether you are **underweight, normal, overweight, or obese** based on your height and weight.

## 🏋️‍♂️ BMI Formula

\[
BMI = \frac{{\text{weight} \times 730}}{{\text{height}^2}}
\]

Where:
- **Weight** is in **pounds (lbs)**
- **Height** is in **inches (in)**

## 🚀 How to Use

1. Run the script in Python.
2. Enter your **weight in pounds**.
3. Enter your **height in inches**.
4. The program calculates and displays your **BMI value** along with its category.

## 🖥️ Code Overview

```python
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
        print("Your BMI is Obese")
    else:
        print("Your BMI is Morbidly Obese")
else:
    print("Enter a Valid Input")

# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 36.875
# 36.875 is not a whole number, it has decimal places. Therefore there is a remainder of 0.875, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

number = int(input("Wich number do you want to check? "))
number_module = number % 2
if(number_module == 0):
    print('This is an odd number.')
else:
    print('This is an even number.')

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese. 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))
if bmi <= 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi > 18.5 and bmi <= 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi > 25 and bmi <= 30:
    print(f'Your BMI is {bmi}, you are slightly overweight')
elif bmi > 30 and bmi <= 35:
    print(f'Your BMI is {bmi},you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
year = int(input("Which year do you want to check? "))
module_year = year % 4
module_year_hundred = year % 100
module_year_four_hundred = year % 400 
if module_year == 0:
    if module_year_hundred == 0:
        if module_year_four_hundred:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
    
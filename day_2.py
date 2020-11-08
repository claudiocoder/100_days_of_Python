# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

number = input("Type a two digit number ")
print(int(number[0]) + int(number[1]))

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height**2)
print(bmi)

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:

age = int(input("What is your current age? "))
age_rest = 90 - age

days = age_rest * 365
weeks = age_rest * 52
months = age_rest * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')


# Project - Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the totall bill? "))
tip = int(input("How much tip would you like to give? 10, 12 0 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f'Each person should pay {final_amount}')
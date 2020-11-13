# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# Don't worry about the lines 3-4, it's there to allow us to test your code.
# You need to generate a random number, either 0 or 1.
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Don't worry about the lines 3/4 it's there to allow us to test your code.
# Line 8 splits the string namesAsCSV into individual names and puts them inside a List called names.
# import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
random_number = random.randint(0, len(names)-1)
print(random_number)
print(names[random_number])
# You are going to write a program which will mark a spot with an X.
# The map is made of 3 rows of blank squares.
#       1      2      3
# 1 ['⬜️', '⬜️', '⬜️']
# 2 ['⬜️', '⬜️', '⬜️']
# 3 ['⬜️', '⬜️', '⬜️']
# Your program should allow you to enter the position of the treasure using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
array_position = list(position)
map[int(array_position[0]) -1 ][int(array_position[1]) - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
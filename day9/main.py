import os
from art import logo

print(logo)
more_users = True
bird_information = {}

def get_information_user():
    name = input("What's is your name ")
    bird = int(input("What's is your price "))
    bird_information[name] = bird

while more_users:
    get_information_user()
    answer = input("Is there another price ").lower()
    print(answer)
    if answer == 'yes':
        os.system('cls||clear')
    else:
        more_users = False

winner = max(bird_information, key=bird_information.get)
print(f"The winner is {winner}")
import random
import os
from hang_words import word_list
from hang_man import stages, logo


clear = lambda: os.system('cls')

end_of_game = False
number_random = random.randint(0, len(word_list)-1)
chosen_word = word_list[number_random]
display = []
size_len = len(chosen_word)
print(logo)
# print(f'the solution is {chosen_word}')

lives = 6

for index in range(size_len):
    display.append('_')


while not end_of_game:

    guess = input("Give me a letter ").lower()

    clear()

    for index in range(size_len):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])


# Functions
# Try https://reeborg.ca/reeborg.html
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
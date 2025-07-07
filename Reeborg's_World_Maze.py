def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear() and wall_on_right() and not at_goal():
        move()
    while not wall_on_right() and not at_goal():
        turn_right()
        move()
        
    while not front_is_clear() and not at_goal():
        turn_left()

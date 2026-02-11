def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def build_win_right():
    global itis
    turn_right()
    build_wall()
    turn_left()
    itis="wall"
    
def check_wallorwin():
    global itis
    move()
    if wall_on_right():
        itis="win"
    else:
        itis="wall"
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()


move()
move()
move()
turn_right()
move()





while not at_goal():
    if wall_on_right() & front_is_clear():
        move()
    elif wall_on_right() & wall_in_front():
        turn_left()
    elif not wall_on_right() & front_is_clear():
        check_wallorwin()
        if itis =="win":
            build_win_right()
        else:
            turn_right()
            move()
        


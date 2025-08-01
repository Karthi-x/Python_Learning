def turn_right():
    turn_left()
    turn_left()
    turn_left()

def harvest_one():
    while object_here():
        take()
    put()    # plants 1 after taking everything else
    move()
def harvest_one_row():
    harvest_one()
    harvest_one()
    harvest_one()
    harvest_one()
    harvest_one()
    harvest_one()
    turning()

def turning():        
    if is_facing_north():
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            move()
    else:
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            move()

move()
move()
turn_left()
move()
move()

harvest_one_row()
harvest_one_row()
harvest_one_row()
harvest_one_row()
harvest_one_row()
harvest_one_row()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()


while not at_goal():
    while object_here():
            take()
    if front_is_clear():
        move()
    else:
        turn_left()
        turn_left()
        if front_is_clear():
            move()
            
turn_right()        
while carries_object():
    toss()
        
        
        
        
        
        
        
        
        
        
        
        
        


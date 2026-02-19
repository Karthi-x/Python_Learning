def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pick():
    while object_here():
        take()
        
def picknmove():
    if front_is_clear():
        pick()
        move()
        
        
while not at_goal():
    while object_here():
        picknmove()
    
    while carries_object():
        put()
        
    move()
    
    
    
    
    
    
    
    
    

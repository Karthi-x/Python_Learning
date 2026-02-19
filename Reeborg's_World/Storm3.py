def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pick():
    while object_here():
        take()
        
def pickngo():
    while not wall_in_front():
        if front_is_clear():
            move()
            pick()
        else:
            deviate()
        
def countngo():
    global rows
    while not wall_in_front():
        move()
        pick()
        rows+=1
        
def deviate():
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
        
def completepick():
    pickngo()
    if is_facing_north():
        turn_left()
        move()
        pick()
        turn_left()
    else:
        turn_right()
        move()
        pick()
        turn_right()
 
rows=0
        
countngo()
turn_left()
for i in range(rows):
    completepick()
    i+=1
    
pickngo()
while carries_object():
    toss()
    
    
turn_left()
move()
pick()
turn_right()    
pickngo()
turn_right()    
pickngo()

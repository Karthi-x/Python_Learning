def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pick():
    while object_here():
        take()
        
def pickngo():
    while front_is_clear():
        move()
        pick()
        
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
 
rows=6
        
pickngo()
turn_left()
for i in range(rows-1):
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

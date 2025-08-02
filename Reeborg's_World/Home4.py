def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move3():
    move()
    move()
    move()

def oneleft():    
    move3()    
    turn_left() 
    move3()

def next_pos():
    turn_right()
    move()
    turn_right()
    
oneleft()
next_pos()
oneleft()
next_pos()
oneleft()
next_pos()
oneleft()

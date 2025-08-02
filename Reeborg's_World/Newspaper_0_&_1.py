def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
def climb_up_one_floor():
    turn_left()
    move()
    turn_right()
    move()
    move()
    
    
def climb_down_one_floor():
    move()
    move()
    turn_left()
    move()
    turn_right()
    

take() 
climb_up_one_floor()
climb_up_one_floor()
climb_up_one_floor()
put("star")
while object_here("token"):
    take("token")

turn_around()
climb_down_one_floor()
climb_down_one_floor()
climb_down_one_floor()

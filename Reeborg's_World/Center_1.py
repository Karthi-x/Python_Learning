steps=0
while front_is_clear():
    move()
    steps=steps+1
turn_left()
turn_left()
pos=steps/2
while not pos==0:
    move()
    pos=pos-1
put()

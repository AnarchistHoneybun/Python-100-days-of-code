#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#following code runs on above reeborg project
#if world resets, choose "maze" in dropdown

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#sys_reset is to overcome cases where robot has no right wall for the first four turns, which traps it in an infinite loop

def sys_reset():
    while front_is_clear():
        move()
    turn_left()

if right_is_clear():
    sys_reset()

while not(at_goal()):
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
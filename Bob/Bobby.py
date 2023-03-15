commands = ["FORWARD,BACK,RIGHT,LEFT,OFF"]

def bobbie_chip():
    bobbie_Bob = input ("What would you like to name your bot? ")
    print(f"{bobbie_Bob}: Hello There:)")
    return bobbie_Bob


def command_input(position):
    bobbie_Bob = bobbie_chip()
    position = position
    m,n = 0,0
    steps = 0
    co_rd = [m,n]
    while True:
        position = track_position(position)
        user_input = input(f"{bobbie_Bob}: What should i do next? ").upper().strip()
        command = user_input.split()
        if "OFF" in command:
            print(f"{bobbie_Bob}: Shutting down.. ")
            break
        if "FORWARD" in command:
            steps = int(command[1])
            co_rd = move_forward_command(bobbie_Bob, position, co_rd, steps)
            print(f" > {bobbie_Bob} now at position ({co_rd[0]}, {co_rd[1]}).")

        elif "BACK" in command:
            steps = int (command[1])
            co_rd = move_back(bobbie_Bob, position, co_rd, steps)
            print(f" > {bobbie_Bob} now at position ({co_rd[0]},{co_rd[1]}).")

        elif "RIGHT" in command:
            position = turn_right(bobbie_Bob,position,co_rd)

        elif "LEFT" in command:
            position = turn_left(bobbie_Bob,position,co_rd)

def commands():
    print("""I can understand these commands:

OFF  - Shut down robot
FORWARD - moves forward by certain number of steps
BACK - moves back certain number of times
RIGHT - turns right
LEFT - turns left""")

    return 'I can understand these commands:\
        OFF - Shut down robot\
        FORWARD - moves forward by certain number of steps\
        BACK - moves back certain number of times\
        RIGHT - turns right\
        LEFT - turns left'

def track_position(position):
    if position == -4 or position == 4:
        position = 0
    return position 


def move_forward_command(bobbie_Bob, position, co_rd, steps):
    old_cord = co_rd.copy()
    position = track_position(position)
    if position == 1 or position == -3:
        co_rd[0] += steps
        co_rd[0] += steps
    elif position == -1 or position == 3:
        co_rd[0] -= steps
    elif position == 2 or position == -2:
        co_rd[1] -= steps
    elif position == 0:
        co_rd[1] += steps
    if not check_cords(bobbie_Bob,co_rd):
        return old_cord
    else:
        print(f" > {bobbie_Bob} moved forward by {steps} steps.")
    return co_rd

def check_cords(bobbie_Bob,co_rd):
    if co_rd[0] < -100 or co_rd[0] > 100:
        print(f'{bobbie_Bob}: Sorry, I cannot go outside my safe zone.')
        return False
    elif co_rd[1] < -200 or co_rd[1] > 200:
        print(f'{bobbie_Bob}: Sorry, I cannot go outside my safe zone.')
        return False
    return True

def move_back(bobbie_Bob,position, co_rd,steps):
    old_cord = co_rd.copy()
    position = track_position(position)
    if position == -1 or position == 3:
        co_rd[0] += steps
    
    elif position == 2 or position == -2:
        co_rd[1] += steps

    elif position == 1 or position == -3:
        co_rd[0] -= steps

    elif position == 0:
        co_rd[1] -= steps

    if not check_cords(bobbie_Bob,co_rd):
        return old_cord
    else:
        print(f" > {bobbie_Bob} moved back by {steps} steps.")
    return co_rd 

def turn_right(bobbie_Bob,position,co_rd):
    position += 1
    print(f" > {bobbie_Bob} turned right.")
    print(f" > {bobbie_Bob} now at position ({co_rd[0]},{co_rd[1]}).")
    return position

def turn_left(bobbie_Bob,position,co_rd):
    position -= 1
    print(f" > {bobbie_Bob} turned left.")
    print(f" > {bobbie_Bob} now at position ({co_rd[0]},{co_rd[1]}).")
    return position

def robot_start():
    """This is the entry function, do not change"""
    position = 0
    position = track_position(position)
    command_input(position)

if __name__ == "__main__":
    robot_start()


def robot_name():
    """Takes in user input for name of the robot and displays it with a greeting and returns the name."""
    
    name = input("What do you want to name your robot? ")
    print(f"{name}: Hello kiddo!")
    return name


def commands(robo_name):
    """Takes in user commands and return them based of control flow."""

    command = input(f"{robo_name}: What must I do next? ")
    lenght = command.split()
    if command.lower() == "off":
        print(f'{robo_name}: Shutting down..')
    elif "forward" in command.lower() and len(lenght) == 2:
        return command  
    elif "back" in command.lower() and len(lenght) == 2:
        return command
    elif "sprint" in command.lower() and len(lenght) == 2:
        return command
    elif "right" == command.lower():
        return command
    elif "left" == command.lower():
        return command
    
    else:
        lis_commands = ['OFF  - Shut down robot','HELP - provide information about commands','Forward','Back','Right',"Left","Sprint"]
        if command.lower() == 'help':
            print("I can understand these commands:")
            for i in lis_commands :
                print(i)
        else :
            print(f"{robo_name}: Sorry, I did not understand '{command}'.")

    return command.lower()


def forward_command(name,steps):
    """
    Displays forward information when the user passes in forward 
    and returns the number of every command that contains a number.
    """
    num = ""
    sign = ""
    for i in steps:
        if i.isdigit()==True:
            num+=i
        if i == "b":
            sign +=i

    lenght = steps.split()

    if  "forward" in steps.lower() and len(lenght)==2  and (int(num)>-200 and int(num)<200) :
        print(f" > {name} moved forward by {num} steps.")
        
    else:
        if len(num) == 3 :
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    return num,sign


def co_ordinates(name,com,x,y):
    """
    Displays cooridinates accordingly.
    """

    if "forward" in com or "back" in com or "sprint" in com or "right" == com or "left" == com  or "right_1" == com or "left_1" == com:
        print(f" > {name} now at position ({x},{y}).")


def back_commands(name,com,num):
    """
    Displays and information when the back command is passed in.
    """
    lenght = com.split()
    if  "back" in com.lower() and len(lenght) == 2 :
        print(f" > {name} moved back by {num} steps.")


def sprint_commands(name,commands,num):
    """
    Responsible for displaying output when  the user passes in the sprint command.
    """

    if  ("right" != commands.lower() and num != '') or ("left" != commands.lower() and num != ''):
        one_less = 0 +int(num)-1
        if "sprint" in commands.lower():
            print(f" > {name} moved forward by {num} steps.")
            if one_less == 0:
                pass
            else:
                new_num =sprint_commands(name,commands,one_less)
                return new_num
    

    pass
    

def x_range(number):
    """
    Responsible for returning a number .
    """

    return number


def tracker(name,com,num,x,y,right_com,left_com ):
    """
    Responsible for keeping track of positions from the functions the increment and decrement accordingly.
    """
    
    if  "right" == com.lower():
        right_com += ["right"]

    if  "left" == com.lower():
        left_com += ["left"]
        if len(right_com) >= 1:
            right_com.pop()

    if len(right_com) == 0 and len(left_com) == 0 :
        if "forward" in com.lower():
            x_1,y_2,command=increment_forward(com,num,x,y)
            return x_1,y_2,command,right_com,left_com

    if len(right_com) >= 1 and len(right_com)<=4 :
        if "right" in com.lower() or "forward" in com.lower():
            x_1,y_2,command,right_com,left_com=increment_right(name,com,x,y,right_com,left_com)
            return x_1,y_2,command,right_com,left_com

    if "left" == com.lower():
        x_1,y_2,command,left_com,right_com=increment_left(name,com,x,y,left_com,right_com)
        return x_1,y_2,command,right_com,left_com

    else:
        x_1,y_2,command=increment_sprint(com,num,x,y)
        return x_1,y_2,command,right_com,left_com
    

def increment_forward(command,number,x,y):
    """
    Responsible for incrementing forward .
    """
    if "forward" in command.lower():
        if int(number) < -200 or int(number) < 200 :
            y+= int(number)
            return x,y,command.lower()
        else:
            return x,y,command.lower()


def increment_right(name,command,x,y,lis,lis_2):
    """
    Responsible for tracking the positions accordingly when  right is pass in.
    """

    lenght = command.split()

    if "right" == command.lower():
        print(f" > {name} turned right.")
        
    if "sprint" in command.lower():
        if int(lenght[1]) in range(-200,200):
            n = command.split()
            for i in range(int(n)+1): y+=i
        else:
            forward_command(name,command)
                


    if "left_1" == command.lower():
        if len(lis) >=1 :
            lis.pop()
        print(f" > {name} turned left.")

    if "left" != command.lower() :
        co_ordinates(name,command,x,y)

    if len(lis) == 0 :
        
        comms = commands(name)
        
        if "back" in comms.lower():
            num = comms.split()
            if int(comms[1]) in range(-200,200):
                back_commands(name,comms,num[1])
                x_,y_,comms=increment_sprint(comms,num[1],x,y)
                return x_,y_,comms.lower(),lis,lis_2
            else:
                forward_command(name,comms)
                return x,y,comms.lower(),lis,lis_2
    
        elif "forward" in comms.lower():
            if int(comms[1]) in range(-200,200):
                num=forward_command(name,comms)[0]
                x_,y_,comms=increment_forward(comms,num,x,y)
                return x_,y_,comms.lower(),lis,lis_2
            else:
                forward_command(name,comms)
                return x,y,comms.lower(),lis,lis_2

        else:
            lis += ["right"]
            print(f" > {name} turned left.")
            co_ordinates(name,comms,x,y)
    
    while "left" != command.lower() :
        
        com = commands(name)
        
        lenght = com.split()

        if "right" in com.lower():
            lis += ["right"]
    
        if "right" == com.lower():
            print(f" > {name} turned right.")
            co_ordinates(name,com,x,y)

        
        if "off" == com:
            lis.clear()
            return x,y,com.lower(),lis,lis_2

        if "forward" in com.lower() or "sprint" in com.lower():        
            if len(lis) == 1:
                if int(lenght[1]) in range(-100,100):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): x+=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 #remember this

                    else:
                        num = forward_command(name,com)[0]
                        x += int(num)
                        co_ordinates(name,com,x,y)

                else:
                    print(f"{name}: Sorry, I cannot go outside my safe zone.")
                    co_ordinates(name,com,x,y)

        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) == 2:
                if int(lenght[1]) in range(-200,200):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): y-=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 

                    else:
                        num_2 = forward_command(name,com)[0]
                        y -= int(num_2)
                        co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)

        
        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) == 3:
                if int(lenght[1]) in range(-100,100):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): x-=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 
                    else:
                        num_3 = forward_command(name,com)[0]
                        x -= int(num_3)
                        co_ordinates(name,com,x,y)
                else:
                    print(f"{name}: Sorry, I cannot go outside my safe zone.")
                    co_ordinates(name,com,x,y)


        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) ==  4:
                if int(lenght[1]) in range(-200,200):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): y+=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 
                    else:   
                        num_3 = forward_command(name,com)[0]
                        y += int(num_3)
                        return x,y,com.lower(),lis,lis_2
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)


        if "back" in com.lower():
            if len(lis) ==  1: 
                if int(lenght[1]) in range(-100,100):
                    num_0 = forward_command(name,com)[0]
                    x -= int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)

                    

        if "back" in com.lower():
            if len(lis) ==  2: 
                if int(lenght[1]) in range(-200,200):
                    num_0 = forward_command(name,com)[0]
                    y += int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)

                    

        if "back" in com.lower():
            if len(lis) ==  3: 
                if int(lenght[1]) in range(-100,100):
                    num_0 = forward_command(name,com)[0]
                    x += int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)

            

        if "back" in com.lower():
            if len(lis) ==  4: 
                if int(lenght[1]) in range(-200,200):
                    num_0 = forward_command(name,com)[0]
                    y -= int(num_0)
                    back_commands(name,com,num_0)
                    return x,y,com.lower(),lis,lis_2
                else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)


        if "sprint" in com.lower():
            if int(lenght[1]) in range(-200,200):
                num_x = forward_command(name,com)[0]
                for i in range(int(num_x)+1): y+=i
                sprint_commands(name,com,int(num_x))
                return x,y,com.lower(),lis,lis_2 
            else:
                    forward_command(name,com)
                    co_ordinates(name,com,x,y)


        if "left" == com.lower():
            x_1,y_2,comm,lis,l_1= increment_right(name,"left_1",x,y,lis,lis_2)
            return x_1,y_2,comm.lower(),lis,l_1
        
        
def increment_left(name,command,x,y,lis,lis_2):
    """"
    Responsible for keeping track of left and incrementing
    or decrementing accordingly.
    """

    lenght = command.split()

    if "left" == command.lower():
        print(f" > {name} turned left.")
        
    if "right_1" == command.lower() :
        if len(lis) >= 1:
            lis.pop()
        print(f" > {name} turned right.")
    
    if "right" != command.lower() :
        co_ordinates(name,command,x,y)

    if len(lis) == 0 :
        comms = commands(name)
        if "forward" in comms.lower():
            num=forward_command(name,comms)[0]
            x_,y_,comms=increment_forward(comms,num,x,y)
            return x_,y_,comms.lower(),lis,lis_2

        elif "back" in comms.lower():
            num = comms.split()
            back_commands(name,comms,num[1])
            x_,y_,comms=increment_sprint(comms,num[1],x,y)
            return x_,y_,comms.lower(),lis,lis_2

        else:
            lis += ["left"]
            print(f" > {name} turned right.")
            co_ordinates(name,comms,x,y)
    
        

    while "right" != command.lower() :
        
        com = commands(name)

        lenght = com.split()

        if "left" in com.lower():
            lis += ["left"]

        if "left" == com.lower():
            print(f" > {name} turned left.")
            co_ordinates(name,com,x,y)

        
        if "off" == com:
            lis.clear()
            return x,y,com.lower(),lis,lis_2

        if "forward" in com.lower() or "sprint" in com.lower():        
            if len(lis) == 1:
                if int(lenght[1]) in range(-100,100):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): x-=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 #remember this
                    else:
                        num = forward_command(name,com)[0]
                        x -= int(num)
                        co_ordinates(name,com,x,y)
                else:
                    print(f"{name}: Sorry, I cannot go outside my safe zone.")
                    return x,y,com.lower(),lis,lis_2

        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) == 2:
                if int(lenght[1]) in range(-200,200):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): y-=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 #remember this
                    else:
                        num_2 = forward_command(name,com)[0]
                        y -= int(num_2)
                        co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2
            
        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) == 3:
                if int(lenght[1]) in range(-100,100):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): x+=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 #remember this
                    else:
                        num_3 = forward_command(name,com)[0]
                        x += int(num_3)
                        co_ordinates(name,com,x,y)
                else:
                    print(f"{name}: Sorry, I cannot go outside my safe zone.")
                    return x,y,com.lower(),lis,lis_2

        if "forward" in com.lower() or "sprint" in com.lower():
            if len(lis) ==  4:
                if int(lenght[1]) in range(-200,200):
                    if "sprint" in com.lower():
                        num_x = forward_command(name,com)[0]
                        for i in range(int(num_x)+1): y+=i
                        sprint_commands(name,com,int(num_x))
                        return x,y,com.lower(),lis,lis_2 #remember this
                    else:   
                        num_3 = forward_command(name,com)[0]
                        y += int(num_3)
                        #lis_2.clear()
                        return x,y,com.lower(),lis,lis_2
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2

        if "back" in com.lower():
            if len(lis) ==  1: 
                if int(lenght[1]) in range(-100,100):
                    num_0 = forward_command(name,com)[0]
                    x += int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2

        if "back" in com.lower():
            if len(lis) ==  2: 
                if int(lenght[1]) in range(-200,200):
                    num_0 = forward_command(name,com)[0]
                    y += int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2
                

        if "back" in com.lower():
            if len(lis) ==  3: 
                if int(lenght[1]) in range(-100,100):
                    num_0 = forward_command(name,com)[0]
                    x -= int(num_0)
                    back_commands(name,com,num_0)
                    co_ordinates(name,com,x,y)
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2
            

        if "back" in com.lower():
            if len(lis) ==  4: 
                if int(lenght[1]) in range(-200,200):
                    num_0 = forward_command(name,com)[0]
                    y -= int(num_0)
                    back_commands(name,com,num_0)
                    return x,y,com.lower(),lis,lis_2
                else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2

        if "sprint" in com.lower():
            if int(lenght[1]) in range(-200,200):
                num_x = forward_command(name,com)[0]
                for i in range(int(num_x)+1): y+=i
                sprint_commands(name,com,int(num_x[0]))
                return x,y,com.lower(),lis,lis_2 #remember this
            else:
                    forward_command(name,com)
                    return x,y,com.lower(),lis,lis_2

        if "right" == com.lower():
            x_1,y_2,comm,lis,l_1= increment_left(name,"right_1",x,y,lis,lis_2)
            return x_1,y_2,comm.lower(),lis,l_1

        
def increment_sprint(command,number,x,y):
    """
    Responsible for incrementing the sprint position and the decrementing the back postion.
    """
    lenght = command.split()
    if "sprint" in command.lower() and len(lenght) == 2 and int(number) in range(-200,200):
        for i in range(int(number)+1): y+=i
        return x,y,command.lower()
    

    elif "back" in command.lower() and len(lenght) == 2 and int(number) in range(-200,200):
        y -= int(number)
        return x,y,command.lower()

    else:
        return x,y,command.lower()
   

def robot_start():
    """This is the entry function, do not change"""
    """"The main engine responsible for operating the code accordingly."""
    x = 0
    y = 0
    right_coms = []
    left_coms = []

    name = robot_name()


    while True :
        
        com =commands(name)
        if com == "off":
            break
        
        elif "forward" in com.lower() or "back" in com.lower() or "sprint" in com.lower() or "right" == com or "left" == com :
            cod_2,sign =forward_command(name,com)
            sprint_commands(name,com,cod_2)
            back_commands(name,com,cod_2)
            x,y,com,right_coms,left_coms=tracker(name,com,cod_2,x,y,right_coms,left_coms)
            co_ordinates(name,com,x,y)
    
        if len(right_coms) == 4 :
            right_coms.clear()
        if com == "off":
            break

    
if __name__ == "__main__":
    robot_start()
    
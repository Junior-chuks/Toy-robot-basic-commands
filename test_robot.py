import unittest
import robot
from test_base import captured_io
from io import StringIO
from unittest.mock import patch



class MyFunctions(unittest.TestCase):
    def test_name(self):
        """
        Checks if the function takes in a user input and displays it . 
        """
        with captured_io(StringIO("Junior\n")) as (out,er):
            self.assertTrue(robot.robot_name()=="Junior",True)
        output = out.getvalue().strip()

        self.assertEqual('''What do you want to name your robot? Junior: Hello kiddo!''',output)

    
    def test_commands(self):
        """
        Checks if the function takes in user inputs and return those inputs
        and if it detects invalid commands and also displays a list of command 
        if the user inputs help.
        """
        with captured_io(StringIO("forward 10\nback 50\nsprint 5\nleft\nright\nFORWARD 5\n")) :
            self.assertEqual(robot.commands('JARVIS'),'forward 10')
            self.assertEqual(robot.commands('JARVIS'),'back 50')
            self.assertEqual(robot.commands('JARVIS'),'sprint 5')
            self.assertEqual(robot.commands('JARVIS'),'left')
            self.assertEqual(robot.commands('JARVIS'),'right')
            self.assertEqual(robot.commands('JARVIS'),'FORWARD 5')
            
        with captured_io(StringIO("where\nhelp\noff\n"))  as (out,err):
            robot.commands("JARVIS")
            robot.commands("JARVIS")
            robot.commands("JARVIS")

        output = out.getvalue().strip()
        self.assertEqual("""JARVIS: What must I do next? JARVIS: Sorry, I did not understand 'where'.
JARVIS: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
Forward
Back
Right
Left
Sprint
JARVIS: What must I do next? JARVIS: Shutting down..""",output
        )
            

    def test_forward_command(self):
        """
        Checks if the function returns a number and empty string 
        when the commands are passed in as an argument .Also checks 
        if it moves forward within the specified range.
        """
        with captured_io("") as (out,err):
            self.assertEqual(robot.forward_command("Boss",'FORWARD 15'),('15', ""))
            self.assertEqual(robot.forward_command("Boss",'FORWARD 205'),('205', ""))

        output = out.getvalue().strip()
        self.assertEqual("""> Boss moved forward by 15 steps.
Boss: Sorry, I cannot go outside my safe zone.""",output)
        
            
    def test_co_ordinates(self):
        "Checks if the function displays the exact coordinates."

        with captured_io("") as (out,err):
            robot.co_ordinates("ICE","back 5",0,-5)
        output = out.getvalue().strip()
        self.assertEqual("> ICE now at position (0,-5).",output)


    def test_back_commands(self):
        "Checks if the function moves back when told to."

        with captured_io("") as (out,err):
            robot.back_commands("Loki","back 30",30)
        output = out.getvalue().strip()
        self.assertEqual("> Loki moved back by 30 steps.",output)


    def test_sprint_command(self):
        """
        Checks if the function sprints when told to.
        """

        with captured_io("") as out:
            robot.sprint_commands("Jarvis","sprint 5",5)
        output = out[0].getvalue().strip()
        self.assertEqual("""> Jarvis moved forward by 5 steps.
 > Jarvis moved forward by 4 steps.
 > Jarvis moved forward by 3 steps.
 > Jarvis moved forward by 2 steps.
 > Jarvis moved forward by 1 steps.""",output)


    def test_x_range(self):
        """
        Checks if the function returns a number passed in a an argument.
        """
        self.assertEqual(robot.x_range(23),23)


    def test_tracker(self):
        """
        Checks if the function keeps track of its position and functions accordingly.
        """
        with captured_io(StringIO("Jarvis\nforward 5\nright\nforward 14\nright\nforward 25\noff\n")) as out:
            robot.robot_start()
        output = out[0].getvalue().strip()
    
        self.assertEqual("""What do you want to name your robot? Jarvis: Hello kiddo!
Jarvis: What must I do next?  > Jarvis moved forward by 5 steps.
 > Jarvis now at position (0,5).
Jarvis: What must I do next?  > Jarvis turned right.
 > Jarvis now at position (0,5).
Jarvis: What must I do next?  > Jarvis moved forward by 14 steps.
 > Jarvis now at position (14,5).
Jarvis: What must I do next?  > Jarvis turned right.
 > Jarvis now at position (14,5).
Jarvis: What must I do next?  > Jarvis moved forward by 25 steps.
 > Jarvis now at position (14,-20).
Jarvis: What must I do next? Jarvis: Shutting down..""",output)


if __name__=="__main__":
    unittest.main()
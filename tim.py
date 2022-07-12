# Here I create the player class.
# In my case it is a Tim class which inherits the Turtle class
# Inherit cause I want to easily use same functionality as `Turtle class`
from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.shapesize(1)
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    # also, the player will need some `controls` so I could control the player
    # (sorry,in the past I was playing with making games Unity)
    def up(self):
        self.forward(20)
    # Lastly, for the player as soon as the player reaches the other side of the screen,
    # his position will be resetedto the starting point.
    def reset_position(self):
        self.goto(0, -280)


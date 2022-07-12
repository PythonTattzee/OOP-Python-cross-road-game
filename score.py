# Here I create the Score class which again inherists the Turtle class
# and have some attributes that I will need to use later to update it.
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        # Here is the number of points for my score object
        self.point = 0
        self.goto(0, 230)
        self.write(self.point, align="center", font=("Arial", 50, "normal"))
        # Here is the number of level for my game
        self.level = 1
        self.goto(-340, 260)
        self.write(self.point, align="center", font=("Arial", 20, "normal"))

    # Then I created the method which will overwrite the old score
    def update_score(self):
        self.clear()
        self.goto(0, 230)
        self.write(self.point, align="center", font=("Arial", 50, "normal"))
        self.goto(-340, 260)
        self.write(f"Level {self.level}", align="center", font=("Arial", 20, "normal"))

    # Then I created the method which will overwrite the old score
    def increase_score(self):
        self.point += 1
        self.update_score()

    # Then I created the method which will overwrite the old level number
    def increase_level(self):
        self.level += 1
        self.update_score()

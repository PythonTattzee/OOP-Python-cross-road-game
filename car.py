# Here I created the carRuling class
# which is responsible for all the car objects created from it.
from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "purple", "green"]
POSITIONS = [(random.randint(380, 680), 0), (random.randint(380, 680),50), (random.randint(380, 680), 100), (random.randint(380, 680), 150),(random.randint(380, 680), 200), (random.randint(380, 680),-50),(random.randint(380, 680),-100),(random.randint(380, 680),-150), (random.randint(380, 680),-200)]

# First, I created one car which inherits the Turtle class.
class CarRuling(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars=[]
        self.create_car()
        # also, needed to keep a track on a speed, so I can influence that later
        self.car_speed = 20

    # Also, there should be multiple cars, so it should be the list of cars,
    # so we need some kind of loop that creates the new car numerous times.
    # So, at the beginning I created the POSITIONS list constant with different positions.
    # I could create the list of colors and iterate through the list of colors, but I went with positions.
    # Also,in order to make it a little-bit more interesting I added random numbers into the list.

    # Now inside the car class we can iterate through the list and create car for each position.
    # Also, I created the COLORS list constant to randomly choose the color from it.

    def create_car(self):
        for pos in POSITIONS:
            self.car = Turtle("square")
            self.car.color(random.choice(COLORS))
            self.car.shapesize(1, 2)
            self.car.penup()
            self.car.goto(pos)
            self.cars.append(self.car)

    # also, we will need to move all of those cars,
    # so we will need to create new move method where we are going
    # to change only the x coordinates and it should be endlessly.
    # Also, as soon as the cars reach the other side
    # the x coordinates need to reset to start position.
    # Also, i keep the track of the speed because later I will need it to level up the game.

    def move(self):
        for key in self.cars:
            key.backward(random.randint(0,self.car_speed))
            # Here in if statement, as soon as the player reaches
            # the other side of the screen, his position
            # will be reseted to the starting point.
            if key.xcor() < -380:
                key.setx(380)
    # here I increase the speed everytime the player reaches the other side of the road
    def level_up(self):
        self.car_speed += 10

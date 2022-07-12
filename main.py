# Today was a challenge for me.
# Because today I needed to make the Game entirely from scretch
# using the Turtle module
# and I didn't want to use any given hints. Just me, `Pycharm` an `Goodle`.
# So here is the result.
#
# So the game rules are that the turtle needs to cross the road without colliding with cars.
# So I thought I will need the `player class` and the `car class that 'rules' the cars`.
# Also, I will need some `score holding class` to handle the score
# and surely I will need the `main.py` to compose it all together

# I started with creating the stracture and main.py
# where we create the screen with specific width
# and we made it to stay open until the click.

from turtle import Screen
from tim import Tim
from car import CarRuling
from score import Score
import time

# Here I crete the screen object with specific size and title.
screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Crossing the road")

screen.tracer(0)

# After that I created the car class where it should be bunch of cars
# that create the traffic and they are moving same direction.

#create car_ruling object from a CarRuling class
car_ruling = CarRuling()
#create tim (aka player object) object from a Tim class
tim = Tim()
#create score (aka player object) object from a Score class
score = Score()

#here I call the event listener (sorry, I have a tiny background in Unity c#)
screen.listen()
screen.onkey(tim.up,"Up")
screen.onkey(tim.down,"Down")

# This is a trigger to switch the while loop
game_is_on = True

# While loop, so we could end and restart the game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # we make the car move by calling the method move from carRuling class:
    car_ruling.move()
    # next I needed to detect the collision of player with a car,
    # so I loop through the list of cars and for each car:
    # if the player collides with it game ends.
    # to detect the collision I used the distance function
    # from a Turtle class
    for car in car_ruling.cars:
        if tim.distance(car) < 12:
            game_is_on = False
    # here if the player reaches the other side of the road
    # the position of a player resets to the starting position
    # and the score updates and the level number increases
    if tim.ycor() > 280:
        score.increase_score()
        score.increase_level()
        tim.reset_position()
        car_ruling.level_up()
# here we call exitonclick() function
# to make screen close only of we click on it with a mouse.
screen.exitonclick()
# YES!:) Sorry I am a beginner and I am already on a lesson day 24 for PYTHON and so far I love it.
# I have a little background of programming but those were four monthes courses for front-end and PHP
# and back than I didn't really grasped the topic.
# Since than I really wanted to come back
# to learning programming but I was too scared 'what if I fail again'.
# After that, some time has passed and now I am 32 and now I want to learn more.
# Recently,I found good course on Udemy and now I am going through it.
# And so far I love it. Also, all the tasks are really like a fun sharades for me.
# I like to solve problems in python.
# My goal is to change my life to better quality and give myself new knowledge.












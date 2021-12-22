"""
A TURTLE OBJECT ACTS AS THE BALL WHOSE HEADING DIRECTION ANGLE IS VARIED DEPENDING ON COLLISIONS AGAINST THE WALLS 
OR THE PADDLES TO MIMIC BOUNCING. 
"""

from time import sleep
from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed(7)
        self.play = False
        self.setposition(0, 0)
        deg1 = randint(-45, 45)
        deg2 = deg1 + 180
        self.setheading(choice([deg1, deg2]))

    # Detect collision with walls and move
    def moveball(self):
        if 277 - abs(self.ycor()) <= 6:
            self.setheading(-self.heading()) 
        self.forward(20)
    
    # Detect collision with paddles
    def checkpad(self, player):
        if round(self.distance(player)) <= 40 and abs(self.xcor()) >= 440 and abs(self.xcor()) < 475:
                return True
        return False

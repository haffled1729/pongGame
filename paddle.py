"""
A LENGTHENED TURTLE OBJECT IS USED AS A PADDLE
"""

from turtle import Turtle

POSITION1 = (-470, 0)
POSITION2 = (470, 0)

class Paddle(Turtle):
    def __init__(self, player) -> None:
        super().__init__()
        # self.number = player
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=0.5)
        self.setheading(90)

        if player == 1:
            self.setposition(POSITION1)
        elif player == 2:
            self.setposition(POSITION2)

    def moveup(self):
        if self.ycor() <= 225:
            self.forward(15)
    
    def movedown(self):
        if self.ycor() >= -225:
            self.backward(15)
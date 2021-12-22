"""
A TURTLE OBJECT IS USED TO WRITE THE SCORE AS WELL AS DRAW THE BORDERS ON THE SCREEN
"""

DIFFICULTY = 0.99              # Controls screen update time by influencing sleep time

from turtle import Turtle
FONT = ('Courier', 20, 'bold')

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.difficulty = 1
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.scores()
    
    def board(self):       # Draw the borders and the middle line
        self.clear()
        self.goto(0, 290)
        self.setheading(270)
        self.pendown()
        for i in range(1,30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.setheading(0)
        self.goto(-490,290)
        self.pendown()
        self.forward(980)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(980)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.penup()
    
    # Increment scores and draw the score on the screen for both the players
    def scores(self, player_no = 0):
        self.board()
        if player_no == 1:
            self.l_score += 1
        elif player_no == 2:
            self.r_score += 1
        self.difficulty *= DIFFICULTY
        self.goto(-245, 300)
        self.pendown()
        self.write(self.l_score,align="center", font=FONT)
        self.penup()
        self.goto(245, 300)
        self.pendown()
        self.write(self.r_score,align="center", font=FONT)
        self.penup()
        self.goto(-245, -350)
        self.pendown()
        self.write("W and S keys",align="center", font=FONT)
        self.penup()
        self.goto(245, -350)
        self.pendown()
        self.write("↑ and ↓ keys",align="center", font=FONT)
        self.penup()
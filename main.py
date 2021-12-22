"""
THE MAIN INTERFACE OF THE PONG GAME
"""

from random import randint, randrange
from turtle import Screen, heading
from score import Score
from time import sleep
from paddle import Paddle
from ball import Ball

#Initial Setup
scr = Screen()
scr.setup(width=1200, height=700)
scr.bgcolor("black")
scr.tracer(0)  #Turn off tracer to enable manual screen update

score = Score()
player1 = Paddle(1)
player2 = Paddle(2)
playball = Ball()


game_On = True
scr.listen()

while game_On:
    def kickoff():         # To initiate motion of the ball, created within scope to be only triggered by the spacebar keypress
        playball.play = True
    
    sleep(0.06 * score.difficulty)  # Screen Update time is reduced with each score, increading the speed and thus difficulty
    scr.update()
    
    if playball.checkpad(player1) or playball.checkpad(player2):   
        playball.setheading(playball.heading() + 180 - randrange(6, 30, 3)) # Bounce the ball back along with a randomness within 30 degrees
        while(playball.checkpad(player1) or playball.checkpad(player2)):  # Wait for the ball to travel a little bit
            playball.moveball()
            sleep(0.05 * score.difficulty)
            scr.update()
    elif playball.xcor() >= 490:   # If the ball has crossed the border on the right side
        score.scores(1)
        playball.home()
        playball.setheading(randint(135, 225))
        playball.play = False
    elif playball.xcor() <= -490:  # If the ball has crossed the border on the left side
        score.scores(2)
        playball.home()
        playball.setheading(randint(-45, 45))
        playball.play = False
    scr.onkeypress(key="space", fun=kickoff)
    scr.onkeypress(key="w", fun=player1.moveup)   # For player 1 - left
    scr.onkeypress(key="s", fun=player1.movedown)   
    scr.onkeypress(key="Up", fun=player2.moveup)    #For player 2 - right
    scr.onkeypress(key="Down", fun=player2.movedown)  
    if playball.play:
        playball.moveball()

scr.exitonclick()

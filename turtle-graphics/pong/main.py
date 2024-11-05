from turtle import *
from paddle import Paddle
from ball import Ball
from score import Score



if __name__ == '__main__':
   screen = Screen()
   screen.setup(width=800, height=600)
   screen.bgcolor('black')
   screen.title("Pong")
   screen.tracer(0)
   
   # create paddles
   left_paddle = Paddle(350,0)
   right_paddle = Paddle(-350,0)
   
   # create ball
   ball = Ball()
   
   # create scoreboard
   score = Score()
   
   # attach screen listners
   screen.listen()
   screen.onkey(key='w', fun=lambda: left_paddle.move('up'))
   screen.onkey(key='a', fun=lambda: left_paddle.move('down'))
   screen.onkey(key='s', fun=lambda: right_paddle.move('up'))
   screen.onkey(key='d', fun=lambda: right_paddle.move('down'))
   
   while score.score < 10:
       screen.update()
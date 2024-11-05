from turtle import *

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.pencolor('white')
        self.fillcolor('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
        
    def move(self, direction):  
        if direction == 'up':
            self.goto(self.xcor(), self.ycor()+20)
        elif direction == 'down':
            self.goto(self.xcor(), self.ycor()-20)
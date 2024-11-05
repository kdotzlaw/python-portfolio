from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pencolor('white')
        self.fillcolor('white')
        self.penup()
        self.speed('fastest')
        self.goto(0,0)
        
    def move(self):
        # 
        
    def bounce(self):
        pass
        
   
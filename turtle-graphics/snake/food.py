from turtle import *
import random

MIN = -280
MAX = 280
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.pencolor('black')
        self.fillcolor('red')
        self.redo()
        

    def redo(self):
         # randomly choose position
        randx = random.randint(MIN, MAX)
        randy = random.randint(MIN, MAX)
        self.goto(randx, randy)
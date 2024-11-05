from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(0,270)
        self.shape('turtle')
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))
        
        
    def increase(self):
        self.score += 1
        self.clear()
        # write score to screen
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'bold'))
        
    def gameOver(self, reason):
        self.goto(0,0)
        self.write(f"Game Over: {reason}", align='center', font=('Arial', 24, 'bold'))
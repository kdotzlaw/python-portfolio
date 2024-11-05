'''
- Screen is 400w x 500h with center at 0,0
- turtles start on lhs of screen and are evenly spaced
- turtles move to the right until they reach the right edge of the screen
- turtles are drawn at the same x coordinate but different y coordinates
'''

from turtle import Turtle, Screen
import random

def drawTurtles():
    # color list
    colors = ['red','orange','yellow','green','blue','purple']
    y = -170
    # create turtles
    for i in range(len(colors)):
        # can specify shape of turtle
        t = Turtle(shape='turtle')
        t.color(colors[i])
        t.penup()
        y+=50
        # draw at specific coordinates
        t.goto(x =-230, y=y)
        

if __name__ == '__main__':
    
    # set up screen
    screen = Screen()
    screen.setup(width=500, height=400)
    play = True
    while play:
        drawTurtles()
        # use screen textInput() to get turtle bet
        inp = screen.textinput(title="bet",prompt="Which turtle do you want to bet on? Enter a color: ")
        # start race
        if inp:
            race = True
        
        while race:
            # move turtles to the right
            for t in screen.turtles():
                # randomly choose dist for each turtle
                dist = random.randint(1,10)
                t.forward(dist)
                # check if turtle has reached the right edge of the screen
                if t.xcor() > 230:
                    # turtle wins
                    race = False
                    if t.pencolor() == inp:
                        print("You won!")
                        
                    else:
                        print("You lost! \n" + t.pencolor() + " won!")
                    inp = screen.textinput(title="Play Again? ",prompt="Would you like to play again? (y/n): ")
                    if inp == 'y':
                        play = True
                        # clear screen
                        screen.clear()
                    else:
                        play = False
                
    screen.exitonclick()
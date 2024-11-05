from turtle import *

# move turtle in a certain direction
def moveSpace():
    t.forward(100)
    
def move(direction):
   if direction == 'up':
       t.setheading(90)
       t.forward(100)
   elif direction == 'down':
       t.setheading(270)
       t.forward(100)
   elif direction == 'left':
       t.setheading(180)
       t.forward(100)
   elif direction == 'right':
       t.setheading(0)
       t.forward(100)
   else:
       # clear the screen
       t.clear()
       # dont draw when moving back to starting position
       t.penup()
       t.home()
       # re enable drawing
       t.pendown()

if __name__ == '__main__':
    # create a turtle
    t = Turtle()
    # set the screen
    screen = Screen()
 
    #set screen to listen to events/key presses
    screen.listen()
    # turtle.onkey(function, key pressed)
    #screen.onkey(key='space', fun=moveSpace)
    screen.onkey(key='w', fun=lambda: move('up'))
    screen.onkey(key='a', fun=lambda: move('left'))
    screen.onkey(key='s', fun=lambda: move('down'))
    screen.onkey(key='d', fun=lambda: move('right'))
    screen.onkey(key='c', fun=lambda: move('clear'))
    screen.exitonclick()
 
    
    
    
    
 

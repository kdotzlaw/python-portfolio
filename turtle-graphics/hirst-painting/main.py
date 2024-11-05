import colorgram
import turtle
import random

def extract_colors():
    rgb_colors = []
    colors = colorgram.extract("C:\\Users\\katri\\Documents\\python-portfolio\\turtle-graphics\\hirst-painting\\image.jpg",30)
    for color in colors:
        rgb_colors.append(color.rgb)

    return rgb_colors



if __name__ == '__main__':
    
    rgb_colors = extract_colors()
    turtle.colormode(255)
    # use OOP
    t = turtle.Turtle()
    # pen settings
    t.penup() # dont draw when turtle is moving
    #t.hideturtle()
    t.speed("fastest")

    distance = 50
    radius = 20
    total = 100
    
    # set starting position
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    
    # go from 1 - total+1 to eliminate 0%10
    for i in range(1,total+1): # for each row
 
        # choose a random color from list
        c = random.choice(rgb_colors)
        t.color(c)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.forward(distance)
        # every row, reset heading and move forward
        if i % 10 == 0:
            # turn right
            t.setheading(90)
            t.forward(distance)
            # turn left
            t.setheading(180)
            t.forward(distance*(total/10))
            # reset heading
            t.setheading(0)
    # set screen
    screen = turtle.Screen()
    screen.exitonclick()
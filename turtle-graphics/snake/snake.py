from turtle import *
# Finals
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.draw()
        self.head = self.segments[0]
       

    # move all segments of the snake in specified direction
    def move(self, direction):
        # set direction of heading
        if direction == 'up':
            self.head.setheading(90)
        elif direction == 'down':
            self.head.setheading(270)
        elif direction == 'left':
            self.head.setheading(180)
        elif direction == 'right':
            self.head.setheading(0)
        
        # move all segments - head moves forward
        # move all segments to location of previous segment
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
   
   
    # draws all segments of the snake
    def draw(self):
        for pos in STARTING_POSITION:
            # create a new segment
            segment = Turtle('square')
            segment.pencolor('black')
            # set the color
            segment.fillcolor('green')
            # dont draw when moving to starting position
            segment.penup()
            # set the position
            segment.goto(pos)
            # add the segment to the snake
            self.segments.append(segment)
       

    def grow_snake(self, position):
        # add a new segment to the snake to the end
        segment = Turtle('square')
        segment.pencolor('black')
        # set the color
        segment.fillcolor('green')
        # dont draw when moving to starting position
        segment.penup()
        # set the position
        segment.goto(position)  
        # add the segment to the snake
        self.segments.append(segment)
        
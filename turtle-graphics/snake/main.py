from turtle import *
import time
from snake import Snake
from food import Food
from score import Score
'''
LEFT: 180
RIGHT: 0
UP: 90
DOWN: 270
'''
if __name__ == '__main__':
    play = True
    # setup screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake")
    screen.tracer(0)
    
    # create snake
    snake = Snake()
    food = Food()
    score = Score()
    
    # attach screen listners
    screen.listen()
    screen.onkey(key='w', fun=lambda: snake.move('up'))
    screen.onkey(key='a', fun=lambda: snake.move('left'))
    screen.onkey(key='s', fun=lambda: snake.move('down'))
    screen.onkey(key='d', fun=lambda: snake.move('right'))
   
    while play:
        # update screena
        screen.update()
        time.sleep(0.1)
        
        # snake moves with key press
        # check for food collision
        if snake.head.distance(food) < 15:
             # add segment to snake
            snake.grow_snake(snake.segments[len(snake.segments) - 1].position())
            # draw new food
            food.redo()
            # score increases
            score.increase()
        # check for wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            # crashing into wall ends gamea
            play = False
            score.gameOver('You crashed into the wall')
            print('game over-wall collision')
        # detect tail collision ie head is in any segment
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                play = False
                score.gameOver('Ya ate your tail')
                print('game over -tail collision')
                
            
     
    # only close on click
    screen.exitonclick()
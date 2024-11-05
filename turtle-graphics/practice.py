from turtle import *


def spiral():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps)
            right(30)
def star():
    # red star with yellow fill
    color('red')
    fillcolor('yellow')
    # turn on fill
    begin_fill()
    while True:
        forward(200)
        left(170)
        # check if turtle is back at the starting position
        if abs(pos()) < 1:
            break
    end_fill()
if __name__ == '__main__':
    #spiral()
    star()
    
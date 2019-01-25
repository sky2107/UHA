import turtle
from turtle import Turtle


keith  = Turtle()
keith.speed(20)
keith.goto(-400,50)
x_axes = 0
width = 200
height = 200

print(keith.window_width())
print(keith.window_height())
while True:
    
    keith.forward(10)
    x_axes +=10

    # up
    keith.left(90)
    keith.forward(50)
    
    keith.right(90)
    keith.forward(10)

    x_axes +=10
    # down
    keith.right(90)
    keith.forward(50)

    keith.left(90)

    if x_axes > 800:
        keith.goto(-400, 50)
        x_axes = 0
    


keith.done()
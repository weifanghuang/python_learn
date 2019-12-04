import turtle
import time

turtle.color("red")
turtle.pensize(2)
turtle.goto(-3, -3)
turtle.speed(1)
for i in range(9):
    turtle.forward(120)
    turtle.right(135)
turtle.up()
turtle.forward(99)
turtle.goto(-66, -66)
turtle.color("black")
turtle.write("kim")
time.sleep(3)

import turtle
import math
import time


def archimedian_turtle(some_turtle, step, nloops, diff=10):
    for _ in range(nloops):
        for i in range(3):
            some_turtle.forward(step)
            some_turtle.right(90)
        some_turtle.forward(step + diff)
        turn_angle = 180 - (math.atan(step / diff) * (180 / math.pi))
        some_turtle.right(turn_angle)
        step += diff


def make_art():
    window = turtle.Screen()
    # opens a screen
    window.bgcolor("red")
    # sets background color of screen to "red"
    jimmy = turtle.Turtle()
    jimmy.shape('turtle')
    jimmy.color('yellow')
    jimmy.speed(40)

    archimedian_turtle(jimmy, step=100, nloops=200, diff=40)
    window.exitonclick()


make_art()

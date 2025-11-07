import turtle
bob = turtle.Turtle()
from random import *

def polygon(size, sides, c):
    bob.color(c)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(size)
        bob.right(angle)
    bob.end_fill()


turtle.colormode(255)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()


def stick(c):
    bob.color(c)
    bob.circle(100)
    jump(100, -100)
    polygon(100, 4, "Brown")
    bob.right(90)
    bob.forward(90)
    
def rectangle(length1, length2, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(2):
        bob.forward(length1)
        bob.right(90)
        bob.forward(length2)
        bob.right(90)
    bob.end_fill()
    
def sqr():
    polygon(149, 4, "blue")
    jump(55,240)
    rectangle(30,165,"white")
    jump(0,150)
    bob.left(90)
    rectangle(30,155,"white")

    
    

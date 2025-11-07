
from myfunctionsproject import *
turtle.colormode(255)
turtle.tracer(False)

'''
for times in range(100):
    x = randint(-500, 200)
    y = randint(-700, 200)
    size = randint(10, 1009)
    jump(x, y)
    bob.circle(100)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    c = (r,g,b)
'''
'''
stick("Brown")
'''
turtle.bgcolor("black")

bob.speed(0)
for times in range(6):
    rectangle(950, 30, "Blue")
    jump(0, 60 * times)

for times in range(5):
    rectangle(950, 30, "White")
    jump(0, 60 * times + 30)

jump(-1, 240)
sqr()

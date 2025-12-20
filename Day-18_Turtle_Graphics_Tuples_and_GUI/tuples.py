import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

directions = [0,90,180,270,360]


for _ in range(200):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random_color())


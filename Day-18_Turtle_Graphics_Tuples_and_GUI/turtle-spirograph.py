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

timmy_the_turtle.speed("fastest")

# This one is my version of spirograph 

# for _ in range(180):
#     for _ in range(180):
#         timmy_the_turtle.forward(5)
#         timmy_the_turtle.right(2)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.right(2)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
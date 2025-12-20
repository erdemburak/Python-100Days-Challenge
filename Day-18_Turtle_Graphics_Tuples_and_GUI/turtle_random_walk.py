from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270,360]


for _ in range(200):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
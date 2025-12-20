from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red","orange")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

"""
This one draws a dashed line 

for i in range(20):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    
"""

# Drawing Differend Shapes
# This part is my version (was just trying to solve the stuation i knew this shoul be written much better)
# # Triangle
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)
# # Square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# # Pentagon
# for _ in range(5):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)
# # Hexagon
# for _ in range(6):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
# # Heptagon
# for _ in range(7):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(51.43)
# # Octagon
# for _ in range(8):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)
# # Nonagon
# for _ in range(9):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)
# # Decagon
# for _ in range(10):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3,11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()

from turtle import Turtle
import turtle as t
import random

# Create an instance, called timmy_the_turtle, of the class Turtle from the turtle module
tim = Turtle()
t.colormode(255)

headings = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

for _ in range(500):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(headings))

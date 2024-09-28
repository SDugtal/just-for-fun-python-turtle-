import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)  # Correct function and adjusted brightness
    h += 1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)  # Adjusted length for better screen fitting
        t.left(144)

turtle.done()

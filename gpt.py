import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')  # Set the background color to black
t.color('white')  # Set the turtle color to white
t.speed(0)  # Set the turtle speed to the fastest

# Drawing a white spiral
for i in range(130):
    t.forward(i * 5)  # Move forward by increasing lengths
    t.right(144)  # Turn right by 144 degrees

turtle.done()

import turtle
turtle.bgcolor('black')
t=turtle.Turtle()
colors=['red','dark red']
for number in range(400):
    t.forward(number+10)
    t.right(70)
    t.pencolor(colors[number%2])
    t.speed(40)
turtle.done()    

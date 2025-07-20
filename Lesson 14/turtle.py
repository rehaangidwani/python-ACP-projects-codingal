import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")  
d = turtle.Turtle()
d.pensize(3)
d.pencolor("white")
d.fillcolor("purple")
d.begin_fill()
for _ in range(4):
    d.forward(100)  
    d.right(90)     
turtle.done()
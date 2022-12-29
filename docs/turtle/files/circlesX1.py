"""draw circles
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("circle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(9)


t.pu()
t.goto(20, 30)
t.pd()
t.seth(0)

t.pensize(10)
t.pencolor("light blue")
t.circle(100)
t.seth(90)
t.pencolor("pink")
t.circle(100)
t.seth(180)
t.pencolor("light green")
t.circle(100)
t.seth(270)
t.pencolor("yellow")
t.circle(100)


s.exitonclick()

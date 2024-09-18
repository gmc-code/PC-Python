"""draw dots -- for testing only
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("dots")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


t.pu()
t.goto(20, 30)
t.pd()
t.seth(0)

t.dot(200, "light blue")
t.dot(150, "pink")
t.dot(100, "light green")
t.dot(50, "yellow")


s.exitonclick()

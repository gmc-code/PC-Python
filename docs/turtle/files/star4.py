"""draw stars
"""
import turtle


def star(t, length=50, points=5, start_pos=(0, 0), start_h=0):
    ang = (360 * ((points-1)/2))/points
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    for _ in range(points):
        t.fd(length)
        t.lt(ang)


s = turtle.Screen()
s.bgcolor("white")
s.title("star")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(9)

start_poss = [(-300, -200),(-200,0),(-100, 200),(0, -200),(100, 0), (200, 200)]
points = [5, 7, 9, 11, 13, 15]
for i in range(6):
    star(t, length=180, start_pos=start_poss[i], start_h=0, points=points[i])

t.ht()
s.exitonclick()

import turtle

s = turtle.Screen()
s.bgcolor("yellow")
print(s.bgcolor())
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=None, starty=None)


t = turtle.Turtle()
print(t.pen())
t.speed(10)
print(t.shape())
t.shape("turtle")
print(t.get_shapepoly())
t.shapesize(2, 2, 0)
print(t.get_shapepoly())
t.pd
for _ in range(4):
    t.fd(250)
    t.left(90)


s.exitonclick()

import turtle

s = turtle.Screen()
s.bgpic("docs/turtle/images/mario.gif")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=0, starty=0)

# turtle drawing
t = turtle.Turtle()

for _ in range(10):
    t.teleport(-400, -230)
    t.shapesize(10, 10, 12)
    t.color("blue")
    t.pensize(10)
    # t.penup(); t.setpos(-400, -230); t.pendown()
    t.fd(800)
    t.clear()

    # same turtle - new drawing
    t.teleport(-400, -230)
    t.shapesize(5, 5, 6)
    t.color("red")
    t.pensize(5)
    # t.penup(); t.setpos(-400, -255); t.pendown()
    t.fd(800)
    t.clear()

turtle.done()
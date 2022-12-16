import turtle

s = turtle.Screen()
s.bgpic("docs/turtle/images/mario.gif")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=0, starty=0)

# turtle drawing
t = turtle.Turtle()
t.shapesize(10, 10, 12)
t.color("blue")
t.pensize(10)
t.penup(); t.setpos(-400, -250); t.pendown()
t.fd(800)

s.resetscreen()

# same turtle - new drawing
t.color("red")
t.pensize(10)
t.penup(); t.setpos(-400, -285); t.pendown()
t.fd(800)


turtle.done()

import turtle

s = turtle.Screen()
s.bgpic("docs/turtle/images/mario.gif")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=40, starty=20)

# turtle drawing
t = turtle.Turtle()
t.shapesize(10, 10, 12)
t.color("blue")
t.pensize(10)
t.penup(); t.setpos(-400, -250); t.pendown()
t.fd(800)

# turtle.screensize(canvwidth=1200, canvheight=800, bg="yellow")
s.setup(width=1200, height=800, startx=0, starty=0)

# same turtle - new drawing
t.color("red")
t.pensize(10)
t.penup(); t.setpos(-400, -285); t.pendown()
t.fd(800)

turtle.done()
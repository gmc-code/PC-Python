import turtle

s = turtle.Screen()
s.bgpic("docs/turtle/images/mario.gif")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=0, starty=0)

# turtle drawing
t = turtle.Turtle()
t.speed(10)
t.color("blue", "red")
t.pensize(10)
t.begin_fill()
t.circle(120)
t.end_fill()


s.resetscreen()

# same turtle - new drawing
t.color("green", "yellow")
t.pensize(5)
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()

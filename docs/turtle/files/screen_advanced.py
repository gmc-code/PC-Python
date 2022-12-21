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
t.pu()
t.goto(110, -290)
t.pd()
t.begin_fill()
t.circle(200)
t.end_fill()

img = s.bgpic(picname=None)
print(img)
s.bgpic("nopic")

turtle.done()

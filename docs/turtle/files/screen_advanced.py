import turtle


s = turtle.Screen()
s.bgcolor("black")
# s.bgpic("docs/turtle/spiro_d.gif")
s.title("Turtle Screen")
s.setup(width=400, height=400, startx=None, starty=None)
s.tracer(1, 0)
s.delay(1)
s.colormode(1)
s.bgcolor(0.9,0.9,1)
t = turtle.Turtle()
t.speed(10)
t.pd
for _ in range(4):
    t.fd(250); t.left(90)
s.screensize(canvwidth=600, canvheight=600)
for _ in range(4):
    t.fd(100); t.left(60)
s.setup(width=700, height=700, startx=None, starty=None)
s.update()
s.exitonclick()


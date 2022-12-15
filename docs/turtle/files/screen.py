import turtle


s = turtle.Screen()
s.bgcolor("black")
print(s.bgcolor())
# s.bgpic("docs/turtle/spiro_d.gif")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=None, starty=None)
# s.tracer(0, 0)
s.delay(0)
s.colormode(255)
s.bgcolor(225,225,255)
s.delay(10000)
s.colormode(1)
s.bgcolor(0.9,0.9,1)
s.setworldcoordinates(-50,-100,50,100)
t = turtle.Turtle()
for _ in range(72):
    t.left(10)

for _ in range(8):
    t.left(45); t.fd(10) 
      # a regular octagon
#s.exitonclick()
turtle.done()

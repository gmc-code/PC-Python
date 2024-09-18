import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
def isosceles(t, base, height, start_pos):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(0)
    
    start_x = start_pos[0]
    start_y = start_pos[1]
    t.fd(base)
    t.goto(start_x + base / 2, start_y + height)
    t.goto(start_x, start_y)


isosceles(t, base=100, height=50, start_pos=(20, 30))
# --end triangle

s.exitonclick()

import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def window_pos(start_pos, x_add, y_add):
    return (start_pos[0] + x_add, start_pos[1] + y_add)

def window(t, length=10, start_pos=(0, 0)):
    sh.square(t, length=length/2, start_pos=start_pos, fillc="light blue")
    sh.square(t, length=length/2, start_pos=window_pos(start_pos, length/2, 0), fillc="light blue")
    sh.square(t, length=length/2, start_pos=window_pos(start_pos, 0, length/2), fillc="light blue")
    sh.square(t, length=length/2, start_pos=window_pos(start_pos, length/2, length/2), fillc="light blue")


window(t, length=200, start_pos=(0, 0))
t.pencolor("red")
t.pu(); t.goto((0, 0)); t.pd(); t.dot(10, "red")
t.pu(); t.goto((-55, -15)); t.pd()
t.write("(0, 0)", move=False, align='left', font=('Arial', 14, 'normal'))

t.pu(); t.goto((100, 0)); t.pd(); t.dot(10, "red")
t.pu(); t.goto((92, -25)); t.pd()
t.write("(5, 0)", move=False, align='left', font=('Arial', 14, 'normal'))

t.pu(); t.goto((0, 100)); t.pd(); t.dot(10, "red")
t.pu(); t.goto((-55, 85)); t.pd()
t.write("(0, 5)", move=False, align='left', font=('Arial', 14, 'normal'))

t.pu(); t.goto((100, 100)); t.pd(); t.dot(10, "red")
t.pu(); t.goto((92, 75)); t.pd()
t.write("(5, 5)", move=False, align='left', font=('Arial', 14, 'normal'))

t.ht()
s.update()
s.exitonclick()

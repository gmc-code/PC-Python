import turtle

# t = turtle.Turtle()
# # t.shape("square")
# # t.shapesize(1, 2)
# # t.shearfactor(-0.5)
# # t.shapetransform()

# t.setheading(90)
# t.write("Home = ", True, align="left")
# t.setheading(45)
# t.write((0,0), True)

# turtle.done()

t = turtle.Turtle()
t.speed(9)
# for i in range(6):
#     t.forward(100)
#     t.left(60)

# # t.penup()
# for a in range(80, -1, -1):
#     # t.stamp()
#     t.left(a)
#     t.forward(20)

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green'] 
for x in range(120):
    t.pencolor(colors[x % 6])
    t.width(x // 12 + 3)
    t.forward(x)
    t.left(30)

turtle.done()
====================================================
Turtle drawing
====================================================

Turtle methods
----------------------------------------

| t = Turtle() create a new Turtle object and open its window

Position:
| t.home() move the turtle to (0, 0), pointing east (depending on mode)
| t.setposition(x, y), t.setpos(x, y), t.goto(x, y): move to coordinates (x, y)
| t.setx(n) set the turtle.s x coordinate, leave y unchanged
| t.sety(n) set the turtle.s y coordinate, leave x unchanged
| t.position(), t.pos(): return the current position (x, y)
| t.distance(x, y): Return the distance from the turtle to coordinates (x, y)

Direction:
| t.left(d), t.lt(d): turn left, anticlockwise, d degrees
| t.right(d), t.rt(d): turn right, clockwise, d degrees
| t.setheading(d), t.seth(d): change heading to direction d
| t.heading() return the current direction (angle)

Movement:
| t.speed(n): how fast the turtle moves (0 to 10)
| t.forward(n), t.fd(): move in the current direction n pixels
| t.backward(n),t.back(n), t.bk(n): move in the reverse direction n pixels

----

Drawing
| t.penup(), t.up(), t.penup(): raise the pen, stoping drawing
| t.pendown(), t.down(), t.pd():  lower the pen for drawing 
| t.isdown(): return True if the pen is down, False if up.
| t.pensize(w), t.width(w): return or set linewidth to w pixels

| t.color(pencolor, fillcolor): change the pencolor and fillcolor
| t.pencolor(color): change the pen colour
| t.fillcolor(color): change the fill colorur

| t.begin_fill(): The starting point is remembered for a filled polygon.
| t.end_fill(): Current fill color is filled after closing the polygon.
| t.filling(): Return True if begin_fill has been called or False if not, or if end_fill has been called. 

----

| t.dot(): Dot is left at the current position.
| t.stamp(): Impression of turtle shape is left at the current position.
| t.shape(name): Return or set shapes, “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.

| t.write(str, move, align, font): write a message to the screen

| t.clear(): Clear the turtle's drawing.
| t.reset(): Clear the turtle's drawing, place it at home and return it to it's default settings.

----

t.hideturtle(), t.ht(): Make the turtle invisible to speed up the drawing.
t.showturtle(), t.st(): Make the turtle visible.
t.isvisible(): Return True if the Turtle is shown, False if it's hidden.



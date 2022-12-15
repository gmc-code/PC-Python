====================================================
Introduction to turtle
====================================================

turtle documentation
----------------------------------------

| Docs: https://docs.python.org/3.11/library/turtle.html#module-turtle
| See the docs for a full lisitng of methods.

----

Tutorial
--------------

| Tutorial: https://www.geeksforgeeks.org/python-turtle-tutorial/
| This has a large number of examples for specific syntax.

----

| Turtle uses tkinter for the underlying graphics.
| Many of the methods have dual use. Passing arguments sets something or does something. Without arguments, they act as functions returning data.

----

Methods of TurtleScreen/Screen: Window control
------------------------------------------------

| s = turtle.Screen()
| s.bgcolor(color)
| s.title(string) show the string in the titlebar of the turtle graphics window

----

Using screen events
----------------------------------------

| turtle.mainloop(), turtle.done() keeps the window open, Starts event loop - calling Tkinter's mainloop function. When used, it must be the last statement in the file.

----

Turtle methods
----------------------------------------

| t = Turtle() create a new Turtle object and open its window

Turtle motion
Move and draw

| **Pen control: Drawing state**
| t.pendown(), t.pd(), t.down() lowers the pen for drawing
| t.penup(), t.pu(), t.up() raises the pen
| t.isdown() returns True if the pen is down
| t.pensize(n), t.width(n) sets linewidth to n pixels or returns it.
| t.pen(pen=None, \*\*pendict) return or set the pen's attributes.

| t.home() moves the turtle to (0, 0), pointing east

| t.heading() return the current direction (angle)
| t.setheading(d) change heading to direction d
| t.position() return the current position at a tuple (x, y)
| t.goto(x, y) move to coordinates (x, y)
| t.left(d) turn left, anticlockwise, d degrees
| t.right(d) turn right, clockwise, d degrees
| t.speed(n) how fast the turtle moves (0 .. 10)
| t.setx(n) set the turtle's x coordinate, leave y unchanged
| t.sety(n) set the turtle's y coordinate, leave x unchanged
| t.forward(n) move in the current direction n pixels
| t.backward(n) move in the reverse direction n pixels

| t.pencolor(r, g, b) change the color to the specified RGB value or named color
| t.pencolor(r, g, b) change the color to the specified RGB value or named color

| t.begin_fill(): The starting point is remembered for a filled polygon.
| t.end_fill(): Current fill color is filled after closing the polygon.

| t.dot(): Dot is left at the current position.
| t.stamp(): Impression of turtle shape is left at the current position.
| t.Shape(): Standard shapes are 'turtle', 'classic', 'arrow' or 'circle'.


| t.write(s, font) write a message to the screen you can specify font and size,
"""'
https://cs111.wellesley.edu/content/libraries/turtleBeads.py
Turtle-based graphics library for drawing various shapes centered on the
cursor.

turtleBeads.py

In general, these functions draw things centered at the cursor, and put
the cursor back where it started afterwards. Set the pensize and pencolor
before drawing a shape to control what is drawn. For most shapes you can
also use fillcolor and begin_fill/end_fill to fill in the shape.

This module also causes built-in turtle commands to print descriptions of
what they draw, and offers the `describeAs` and `endDescription`
functions to provide custom descriptions of collections of turtle
commands. These printed descriptions can be used to verify that drawing
matches a specified desired drawing.
"""

__version__ = "1.1.2"

import math
import random

import turtle as t


# Setup function
#---------------

def setupTurtle():
    """
    Sets up the turtle window using default size, speed, pen size, and
    pen/fill colors.
    """
    try:
        t.setup()
    except Exception:
        pass
    t.setup()
    t.reset()
    t.pensize(1.5)
    t.color("black", "black")
    # TODO: Move turtle window to front


# Print control
#--------------

PRINT_RESULTS = True
"""
Whether or not to print each time we draw something. Includes printing
for built-in turtle functions forward, back, circle, and begin/end_fill.
"""

PRINT_LINES = True
"""
Global to enable/disable printing for the forward and backward commands
(and their aliases). Useful because turtleBeads wants to use those
commands as part of larger shapes but print a higher-level summary of the
larger shape instead.
"""

DESCRIPTION_STACK = []
"""
A stack of custom descriptions of what is currently being drawn. Most
relevant description is at the start.
"""


def describeAngle(angle, normalize=360):
    """
    Converts an angle (in floating-point degrees) to a string description
    of that angle. The second argument (default 360) should be either
    a number or None, and controls normalization. When it's exactly the
    integer 180 (not 180.0), angles 0, and 180 will be described as
    "horizontal" and angles 90 and 270 will be described as "vertical".
    When it's exactly the integer 360, angles 0, 90, 180, and 270 will be
    described using the cardinal directions (according to the default
    right-handed coordinate system). If normalize is None, then no
    normalization is performed, and, for example, negative angles will
    remain negative. The angle will always be rounded to the nearest
    tenth of a degree.
    """
    if type(normalize) == int and normalize == 180:
        norm = ((round(angle, 1) % 180) + 180) % 180
        if norm == 0.0:
            return "horizontal"
        elif norm == 90.0:
            return "vertical"
        # otherwise fall out
    elif type(normalize) == int and normalize == 360:
        norm = ((round(angle, 1) % 360) + 360) % 360
        if norm == 0.0:
            return "East"
        elif norm == 90.0:
            return "North"
        elif norm == 180.0:
            return "West"
        elif norm == 270.0:
            return "South"
        # otherwise fall out
    elif normalize is not None:
        norm = ((round(angle, 1) % normalize) + normalize) % normalize
    else:
        norm = round(angle, 1)

    return withTenths(norm) + 'Â°'


def describeColor(color):
    """
    Describes a color.
    """
    if isinstance(color, (list, tuple)):
        return "RGB" + repr(color)
    else:
        return color


def withTenths(val):
    """
    Returns a string containing the given floating-point value rounded to
    the tenths place, with the decimal and zero dropped if it's an even
    number.
    """
    result = "{:.1f}".format(val)
    if result[-1] == '0':
        result = result[:-2]
    return result


def describePen(pensize, pencolor):
    """
    Returns a string describing the pen format for the given size &
    color.
    """
    return "{}-pensize {}".format(withTenths(pensize), describeColor(pencolor))


def decorateBuiltins():
    """
    Handles the decoration of built-in turtle functions so that they
    print a report when called. Note that this function monkey-patches
    the turtle module, but does not affect already-imported specific
    names from that module. So if you do `from turtle import *` followed
    by `turtleBeads.decorateBuiltins` the names you imported won't link
    to the decorated functions. However, if you call `decorateBuiltins`
    first, the functions you import will be decorated.
    """
    def wrapLineFcn(basefcn):
        """
        Wrapper for line functions (fd/bk/etc.) that announces the line
        drawn.
        """
        def wrapped(*args, **kwargs):
            """ PLACEHOLDER """
            if (
                PRINT_RESULTS
            and len(DESCRIPTION_STACK) == 0
            and PRINT_LINES
            and t.isdown()
            ):
                # Preliminary info
                wasAt = t.position()
                angle = describeAngle(t.heading(), normalize=180)
                fmt = describePen(t.pensize(), t.pencolor())

                # Call the wrapped function
                basefcn(*args, **kwargs)

                # Gather final info
                nowAt = t.position()

                print(
                    "A {} {} line from ({}, {}) to ({}, {}).".format(
                        fmt,
                        angle,
                        round(wasAt[0]),
                        round(wasAt[1]),
                        round(nowAt[0]),
                        round(nowAt[1])
                    )
                )
            else:
                basefcn(*args, **kwargs)

        wrapped.__name__ = basefcn.__name__
        wrapped.__doc__ = basefcn.__doc__ + """

    This version also prints a description of the line it draws if the
    pen is down.
"""
        return wrapped

    # Wrap forward & backward functions
    for lf in (t.fd, t.forward, t.bk, t.back, t.backward):
        setattr(t, lf.__name__, wrapLineFcn(getattr(t, lf.__name__)))

    orig_circle = t.circle

    def loudCircle(radius, degrees=360):
        """ PLACEHOLDER """
        global PRINT_LINES
        if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0 and t.isdown():
            # Collect preliminary info
            wasAt = t.position()
            wasFacing = t.heading()
            fmt = describePen(t.pensize(), t.pencolor())

            # Draw the circle (w/out reporting lines)
            wasPrintingLines = PRINT_LINES
            PRINT_LINES = False
            orig_circle(radius, degrees)
            PRINT_LINES = wasPrintingLines

            # Collect final info
            nowAt = t.position()
            nowFacing = t.heading()

            # Compute center
            center = (
                wasAt[0] + math.cos(math.radians(wasFacing + 90)) * radius,
                wasAt[1] + math.sin(math.radians(wasFacing + 90)) * radius
            )

            if degrees >= 360:
                print(
                    (
                        "A {} circle centered at ({}, {}) with radius"
                      + " {}."
                    ).format(
                        fmt,
                        round(center[0]),
                        round(center[1]),
                        withTenths(radius)
                    )
                )
            else:
                print(
                    "A {} arc from ({}, {}) facing {} to ({}, {}) facing {}."
                    .format(
                        fmt,
                        round(wasAt[0]),
                        round(wasAt[1]),
                        describeAngle(wasFacing),
                        round(nowAt[0]),
                        round(nowAt[1]),
                        describeAngle(nowFacing)
                    )
                )
        else:
            orig_circle(radius, degrees)

    loudCircle.__name__ = t.circle.__name__
    loudCircle.__doc__ = t.circle.__doc__ + """

    This version also prints a description of the circle or arc it
    draws if the pen is down.
"""

    t.circle = loudCircle

    orig_bf = t.begin_fill

    def loudBeginFill():
        """ PLACEHOLDER """
        orig_bf()
        if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0:
            print("Start of filled shape.")

    orig_ef = t.end_fill

    def loudEndFill():
        """ PLACEHOLDER """
        color = t.fillcolor()
        orig_ef()
        if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0:
            print("Filled in shape using {}.".format(color))

    loudBeginFill.__name__ = t.begin_fill.__name__
    loudBeginFill.__doc__ = t.begin_fill.__doc__ + """

    This version also announces that filling has begun.
"""
    loudEndFill.__name__ = t.end_fill.__name__
    loudEndFill.__doc__ = t.end_fill.__doc__ + """

    This version also announces that filling has ended, along with the
    current fill color.
"""

    t.begin_fill = loudBeginFill

    t.end_fill = loudEndFill

    orig_write = t.write

    def loudWrite(
        text,
        move=False,
        align="left",
        font=("Arial", 8, "normal")
    ):
        """ PLACEHOLDER """
        if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0:
            # Collect preliminary info
            wasAt = t.position()
            angle = describeAngle(t.heading())
            fmt = "{}pt {}{}".format(
                font[1],
                font[0],
                ' ' + font[2] if font[2] != "normal" else ''
            )

            # Draw the text
            orig_write(text, move=move, align=align, font=font)

            # Print a message
            print(
                "The text '{}' in {} font at {}{}".format(
                    text,
                    fmt,
                    (round(wasAt[0]), round(wasAt[1])),
                    (
                        ''
                        if angle == "East"
                        else (
                            " running " + angle
                            if angle in ("North", "West", "South")
                            else (
                                " tilted at " + angle
                            )
                        )
                    )
                )
            )
        else:
            orig_write(text, move=move, align=align, font=font)

    loudWrite.__name__ = t.write.__name__
    loudWrite.__doc__ = t.write.__doc__ + """

    This version also announces the text that is drawn.
"""
    t.write = loudWrite


def redefineBuiltins():
    """
    Defines `turtle` built-in functions as global variables in this
    module, meaning that `turtle` doesn't have to be imported. If called
    after `decorateBuiltins`, the globals defined will be the decorated
    versions. This also creates a few lowerCamelCase versions of turtle
    functions which have inconsistent naming, like begin_fill/end_fill
    and pencolor/fillcolor.
    """
    global fd, bk, forward, back, backward, circle, begin_fill,\
        end_fill, write, beginFill, endFill, penColor, fillColor,\
        setHeading, setPosition, setX, setY, penUp, penDown, penSize,\
        bgColor

    # Pass-throughs into global namespace
    fd = t.fd
    forward = t.fd
    bk = t.bk
    back = t.bk
    backward = t.bk
    circle = t.circle
    begin_fill = t.begin_fill
    end_fill = t.end_fill
    write = t.write

    # lowerCamelCase versions
    endFill = t.end_fill
    beginFill = t.begin_fill
    penColor = t.pencolor
    fillColor = t.fillcolor
    setHeading = t.setheading
    setPosition = t.setpos
    setX = t.setx
    setY = t.sety
    penUp = t.penup
    penDown = t.pendown
    penSize = t.pensize
    penColor = t.pencolor


def beSilent():
    """
    Disables printed output of turtle drawing. Re-enable it with
    `beLoud`.
    """
    global PRINT_RESULTS
    PRINT_RESULTS = False


def beLoud():
    """
    Re-enables printed output of turtle drawing if it's been turned off
    using `beSilent`.
    """
    global PRINT_RESULTS
    PRINT_RESULTS = True


def describeAs(description):
    """
    Sets the given description and turns announcements off until
    `endDescription` is called. Calling `endDescription` will
    print the provided description. Calling `describeAs` again add a
    sub-description which will not be printed, and the matching call to
    `endDescription` will not print anything (so that only the
    'outermost' `describeAs`/`endDescription` pair takes effect).

    While a custom description is active, default description messages
    will not be printed.
    """
    global DESCRIPTION_STACK
    DESCRIPTION_STACK.append(description)


def endDescription():
    """
    Removes one entry from the description stack, printing it out if it
    was the last one. When the final description is removed, normal
    printing of automatic descriptions will resume.

    Prints a warning message if the description stack is empty.

    The warning and/or the description will be suppressed if `beSilent`
    has been called.
    """
    global DESCRIPTION_STACK
    if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0:
        print(
            "Warning: called endDescription but no description was active."
        )
    else:
        done = DESCRIPTION_STACK.pop()
        if PRINT_RESULTS and len(DESCRIPTION_STACK) == 0:
            print(done)


def quietLines():
    """
    Disables printed output for forward/back commands and their aliases.
    Re-enable with `loudLines`.
    """
    global PRINT_LINES
    PRINT_LINES = False


def loudLines():
    """
    Re-enables printed output for forward/back commands if it was
    disabled with `quietLines`.
    """
    global PRINT_LINES
    PRINT_LINES = True


# Apply decorations even on import
decorateBuiltins()

# Create re/extra definitions in this module
redefineBuiltins()


# Trace control
#--------------

def noTrace():
    """
    Disables turtle tracing, so that drawing will be near-instant (much
    faster than even speed 0). However, nothing will be displayed until
    you call showPicture.
    """
    t.tracer(0, 0)


def doTrace():
    """
    Re-enables tracing, so that the turtle will move along the path that
    it draws and you can see each line being drawn. This function first
    updates the picture to display any lines drawn since tracing was
    disabled (if it had been).
    """
    t.update()
    # TODO: What args here?
    t.tracer(1, 1)


def showPicture():
    """
    Shows any lines drawn so far. Required when noTrace has been called
    to disable real-time drawing.
    """
    t.update()


# Movement shortcuts
#-------------------

def realign():
    """
    Sets the turtle's heading back to the default (0 degrees = facing
    right).
    """
    t.setheading(0)


def teleport(x, y):
    """
    Penup + goto + pendown.
    """
    downNow = t.isdown()
    t.penup()
    t.goto(x, y)
    if downNow:
        t.pendown()


def leap(dist):
    """
    Penup + fd + pendown. You can use a negative number to go backwards.
    """
    downNow = t.isdown()
    t.penup()
    t.fd(dist)
    if downNow:
        t.pendown()


def hop(dist):
    """
    Lifts the pen and moves the given distance to the left of the current
    turtle position without changing the orientation of the turtle (hops
    sideways). Use a negative number to hop to the right. Puts the pen
    back down when it's done if the pen was down beforehand.
    """
    downNow = t.isdown()
    t.penup()
    t.lt(90)
    t.fd(dist)
    t.rt(90)
    if downNow:
        t.pendown()


# Drawing parameters
#-------------------

BASE_CURVE_STEPS = 32  # Default number of sides of a circle
MAX_CURVE_STEPS = 128  # Maximum number of sides for a circle
TARGET_SEGMENT_LENGTH = 3  # Ideal length for each side of a circle


# "Beads" functions
#------------------

def drawCircle(radius):
    """
    Draws a circle centered at the given position with the given radius,
    and puts the turtle back where it started when it's done.

    Actually, it draws a many-sided polygon, but the difference should
    usually be hard to see.
    """
    downNow = t.isdown()

    # Start a description if there isn't a custom description active
    describing = False
    if len(DESCRIPTION_STACK) == 0 and downNow:
        describing = True
        x, y = t.position()
        fmt = describePen(t.pensize(), t.pencolor())
        describeAs(
            "A {} circle centered at ({}, {}) with radius {}".format(
                fmt,
                round(x),
                round(y),
                withTenths(radius)
            )
        )

    steps = BASE_CURVE_STEPS
    segmentLength = (2 * math.pi * radius) / steps
    while segmentLength > TARGET_SEGMENT_LENGTH and steps < MAX_CURVE_STEPS:
        steps += 1
        segmentLength = (2 * math.pi * radius) / steps
    start = t.pos()
    starth = t.heading()
    t.penup()
    t.lt(90)
    t.fd(radius)
    t.rt(90)
    if downNow:
        t.pendown()
    t.fd(segmentLength / 2)
    t.rt(360 / steps)
    for i in range(steps - 1):
        t.fd(segmentLength)
        t.rt(360 / steps)
    t.penup()
    t.fd(segmentLength / 2)
    t.goto(start[0], start[1])
    t.seth(starth)
    if downNow:
        t.pendown()

    if describing:
        endDescription()


def ellipsePointAt(major, minor, angle):
    """
    Takes an angle in degrees and computes the ellipse point for that many
    degrees clockwise from the top of the ellipse where the given minor
    radius is vertical and the given major radius is horizontal. Uses the
    trammel drawing method from:

    https://www.joshuanava.biz/engineering-3/methods-of-drawing-an-ellipse.html

    The angle specified is interpreted as the trammel angle, not an angle
    of a ray from the center of the ellipse through the given point.
    """
    rad = math.radians(90 - angle)
    yIntercept = -(major - minor) * math.sin(rad)
    xValue = major * math.cos(rad)
    yValue = yIntercept + major * math.sin(rad)

    return (xValue, yValue)


def drawEllipse(radius, aspectRatio, arcAngle=None):
    """
    Draws an ellipse with the given radius and aspect ratio. If aspectRatio
    is less than 1, the given radius will be the ellipse's larger radius,
    and the ellipse will stretch farther to the sides of the turtle than
    in front of and behind it, otherwise the given radius will be the
    smaller radius, and the ellipse will stretch farther to the front and
    back than to the sides (the given radius is always the distance from
    the turtle's current position to the sides of the ellipse directly
    left and right of the turtle).

    There is an optional argument 'arcAngle,' which will cause this
    function to draw only part of an ellipse. The ellipse segment is
    drawn starting at the left of the current cursor position if the
    aspect ratio is greater than or equal to 1, or starting behind the
    current cursor position if the aspect ration is less than 1.
    """
    # Measure starting position/orientation
    downNow = t.isdown()
    startPos = t.pos()
    startHeading = t.heading()

    headingAdjust = 0

    # Start a description if there isn't a custom description active
    describing = False
    if len(DESCRIPTION_STACK) == 0 and downNow:
        describing = True
        fmt = describePen(t.pensize(), t.pencolor())
        if aspectRatio < 1:
            majorlen = radius
            minorlen = radius * aspectRatio
            majorAngle = describeAngle(t.heading() + 90, normalize=180)
        else:
            majorlen = radius * aspectRatio
            minorlen = radius
            majorAngle = describeAngle(t.heading(), normalize=180)

        if majorAngle in ("horizontal", "vertical"):
            major = majorAngle + " major axis"
        else:
            major = "major axis at " + majorAngle

        axes = "a {}-unit {} and a {}-unit minor axis".format(
            withTenths(majorlen),
            major,
            withTenths(minorlen)
        )

        describeAs(
            "{a} {fmt} ellipse centered at ({x}, {y}) with {axes}".format(
                a=(
                    "A"
                    if arcAngle is None
                    else str(round(arcAngle)) + "Â° of a"
                ),
                fmt=fmt,
                x=round(startPos[0]),
                y=round(startPos[1]),
                axes=axes
            )
        )

    # Decide minor/major axes and start angle based on aspect ratio:
    if aspectRatio >= 1:
        minor = radius
        major = radius * aspectRatio
        startAngle = 0

        # Get into position to start the ellipse:
        t.penup()
        t.lt(90)
        t.fd(minor)
        t.rt(90)
        if downNow:
            t.pendown()
        here = (0, minor)

    else:
        minor = radius * aspectRatio
        major = radius
        startAngle = -90
        headingAdjust = -90

        # Get into position to start the ellipse:
        t.penup()
        t.lt(90)
        t.fd(major)
        t.rt(90)
        if downNow:
            t.pendown()
        here = (-major, 0)

    # Compute number of segments to draw based on estimated segment length:
    steps = BASE_CURVE_STEPS
    segmentLength = (2 * math.pi * major) / steps
    while segmentLength > TARGET_SEGMENT_LENGTH and steps < MAX_CURVE_STEPS:
        steps += 1
        segmentLength = (2 * math.pi * major) / steps

    # Actually draw the ellipse:
    stop = False
    for i in range(1, steps + 1):
        nextAngle = startAngle + i * 360 / steps
        if arcAngle is not None and nextAngle > startAngle + arcAngle:
            stop = True
            there = ellipsePointAt(major, minor, startAngle + arcAngle)
        else:
            there = ellipsePointAt(major, minor, nextAngle)
        vec = (there[0] - here[0], there[1] - here[1])

        # Compute heading in unrotated ellipse and distance to travel:
        towardsNext = math.degrees(math.atan2(vec[1], vec[0]))
        dist = (vec[0] * vec[0] + vec[1] * vec[1]) ** 0.5

        # Draw segment:
        t.setheading(startHeading + headingAdjust + towardsNext)
        t.fd(dist)

        # Update here -> there
        here = there

        if stop:
            break

    # Return to original position and heading:
    t.penup()
    t.goto(startPos[0], startPos[1])
    t.setheading(startHeading)
    if downNow:
        t.pendown()

    if describing:
        endDescription()


def drawDot(radius):
    """
    Draws a circle filled with the current pen color of the given radius.
    Does not move the turtle. For large circles, this may be more round
    than the result of the drawCircle function, and it will also be
    faster, but the limitation is that the circle will always be filled
    in, and the pen color will be used as the fill color (can't have
    separate border + fill colors).
    """
    if not isinstance(radius, (int, float)):
        raise TypeError(
            f"Cannot draw a dot with a radius which is not a number"
            f" (you gave us {radius!r})."
        )
    if radius < 0:
        raise ValueError(
            f"Cannot draw a dot with a negative radius (you gave us"
            f" {radius})."
        )
    # Start a description if there isn't a custom description active
    describing = False
    if len(DESCRIPTION_STACK) == 0 and t.isdown():
        describing = True
        x, y = t.position()
        describeAs(
            "A {} dot at ({}, {}) with radius {}".format(
                describeColor(t.pencolor()),
                round(x),
                round(y),
                round(radius)
            )
        )
    oldSize = t.pensize()
    t.pensize(radius * 2)
    t.fd(0)
    t.pensize(oldSize)

    if describing:
        endDescription()


def drawSquare(size):
    """
    Draws a square of the given size centered on the current turtle
    position. Puts the turtle back when it's done.
    """
    drawRectangle(size, size)


def drawRectangle(length, width):
    """
    Draws a rectangle of the given length (in front of and behind the turtle)
    and width (to the left and right of the turtle) centered on the current
    turtle position. Puts the turtle back when it's done.
    """
    downNow = t.isdown()

    # Start a description if there isn't a custom description active
    describing = False
    if len(DESCRIPTION_STACK) == 0 and downNow:
        describing = True
        fmt = describePen(t.pensize(), t.pencolor())
        x, y = t.position()

        # If it's square
        if width == length:
            angle = describeAngle(t.heading(), normalize=90)
            describeAs(
                (
                    "A {fmt} {side} by {side} square centered at"
                  + " ({x}, {y}){angle}."
                ).format(
                    fmt=fmt,
                    side=length,
                    x=round(x),
                    y=round(y),
                    angle=(
                        " tilted at " + angle
                        if angle != "0Â°"
                        else ""
                    )
                )
            )
        else:  # it has long/short axes

            # Figure out the real length/width/angle where length is longer
            dlen = length
            dwid = width
            dangle = t.heading()
            if width > length:
                dlen = width
                dwid = length
                dangle = t.heading() + 90

            angle = describeAngle(dangle, normalize=180)
            if angle in ("horizontal", "vertical"):
                angleString = "a {} long axis".format(angle)
            else:
                angleString = "a long axis at {}".format(angle)

            describeAs(
                (
                    "A {fmt} {length} by {width} rectangle centered at"
                  + " ({x}, {y}) with {angle}."
                ).format(
                    fmt=describeColor(t.pencolor()),
                    length=dlen,
                    width=dwid,
                    x=round(x),
                    y=round(y),
                    angle=angleString
                )
            )

    t.penup()
    t.lt(90)
    t.fd(width / 2)
    t.rt(90)
    t.bk(length / 2)
    if downNow:
        t.pendown()
    t.fd(length)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.fd(length)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.penup()
    t.fd(length / 2)
    t.rt(90)
    t.fd(width / 2)
    t.lt(90)
    if downNow:
        t.pendown()

    if describing:
        endDescription()


POLYGON_NAMES = [
    "point",
    "line",
    "hinge",
    "triangle",
    "quadrilateral",
    "pentagon",
    "hexagon",
    "heptagon",
    "octagon"
    "nonagon",
    "decagon",
    None,  # it's called a "hendecagon," "undecagon," or "endecagon" but
    # who the heck knows that?
    "dodecagon",
]
"""
Names of polygons with various numbers of sides.
"""


def polygon_name(n):
    """
    The name for a polygon with N sides.
    """
    if n in range(len(POLYGON_NAMES)) and POLYGON_NAMES[n] is not None:
        return POLYGON_NAMES[n]
    else:
        return str(n) + '-gon'


def drawPolygon(sideLength, numSides):
    """
    Draws a polygon with the given side length and number of sides,
    centered at the current position. numSides must be at least 3, or
    nothing will be drawn. The polygon created is always equilateral, and
    always has one side perpendicular to the current heading that's to the
    left of the current turtle position (left based on the current turtle
    heading).
    """
    if numSides < 3:
        return

    downNow = t.isdown()

    # Start a description if there isn't a custom description active
    describing = False
    if len(DESCRIPTION_STACK) == 0 and downNow:
        describing = True
        fmt = describePen(t.pensize(), t.pencolor())
        x, y = t.position()
        angle = describeAngle(t.heading() + 90, normalize=360)
        describeAs(
            (
                "A {fmt} {shape} with side length {side} centered at"
              + " ({x}, {y}) with a flat side facing {angle}."
            ).format(
                fmt=fmt,
                shape=polygon_name(numSides),
                side=sideLength,
                x=round(x),
                y=round(y),
                angle=angle
            )
        )

    # (sideLength/2) / center-side distance = tan(theta/2)
    # so center-side distance = (sideLength/2) / tan(theta/2)
    sideAngle = 360 / numSides
    centerSideDist = (
        (sideLength / 2)
      / math.tan(math.radians(sideAngle) / 2)
    )
    t.penup()
    t.lt(90)
    t.fd(centerSideDist)
    t.rt(90)
    if downNow:
        t.pendown()
    t.fd(sideLength / 2)
    t.rt(sideAngle)
    for i in range(numSides - 1):
        t.fd(sideLength)
        t.rt(sideAngle)

    t.fd(sideLength / 2)
    t.penup()
    t.rt(90)
    t.fd(centerSideDist)
    t.lt(90)
    if downNow:
        t.pendown()

    if describing:
        endDescription()


# Path drawing
#-------------

def pointRep(point):
    """
    A rounded-off representation of a 2-item x/y point.
    """
    x, y = point
    return f"({str(round(x))}, {str(round(y))})"


def drawPath(
    points,
    startArrow=None,
    startArrowSize=12,
    endArrow=None,
    endArrowSize=12,
):
    """
    Given a list of x/y coordinate pairs, draws a line from the start to
    the end, passing through each point. The points list must be
    indexable. The startArrow and endArrow arguments are optional, and
    should be None (for no arrow at that end) or one of the strings
    "dot", "square", or "triangle" for different shapes. The
    corresponding size arguments control how big these ending symbols
    are. If the path is empty, nothing is drawn, or if it has only one
    point, just the arrows are drawn (both at that location, angled
    according to the turtle's current orientation).
    """
    if len(points) == 0:
        return

    arrowsDesc = ""
    if startArrow is not None:
        arrowsDesc += (
            f" with a size-{round(startArrowSize)} {startArrow} at the start"
        )
    if endArrow is not None:
        if startArrow is None:
            arrowsDesc += (
                f" with a size-{round(endArrowSize)} {endArrow} at the end"
            )
        else:
            arrowsDesc += (
                f" and a size-{round(endArrowSize)} {endArrow} at the end"
            )

    if len(points) == 1:
        desc = f"A point at {pointRep(points[0])}{arrowsDesc}"
    elif len(points) == 2:
        desc = (
            f"A line from {pointRep(points[0])} to"
            f" {pointRep(points[1])}{arrowsDesc}"
        )
    elif len(points) == 3:
        desc = (
            f"A path from {pointRep(points[0])} to"
            f" {pointRep(points[1])} to"
            f" {pointRep(points[2])}{arrowsDesc}"
        )
    elif len(points) == 4:
        desc = (
            f"A path from {pointRep(points[0])} to"
            f" {pointRep(points[3])} passing through"
            f" {pointRep(points[1])} and"
            f" {pointRep(points[2])}{arrowsDesc}"
        )
    else:
        middle = (
            ', '.join(pointRep(point) for point in points[1:-2])
          + ', and ' + pointRep(points[-2])
        )
        desc = (
            f"A path from {pointRep(points[0])} to {pointRep(points[2])}"
            f" passing through {middle}{arrowsDesc}"
        )
    describeAs(desc)

    # Go to first point
    teleport(*points[0])
    if len(points) > 1:
        # Set heading for first point to angle start arrow
        t.setheading(t.towards(*points[1]))

    # draw start arrow
    if startArrow == "dot":
        drawDot(startArrowSize)
    elif startArrow == "square":
        t.begin_fill()
        drawSquare(startArrowSize)
        t.end_fill()
    elif startArrow == "triangle":
        leap(startArrowSize / 2)
        t.rt(90)
        t.begin_fill()
        drawPolygon(startArrowSize, 3)
        t.end_fill()
        t.lt(90)
        leap(-startArrowSize / 2)
    # else no start arrow

    for point in points[1:]:
        # Go to next point
        t.setheading(t.towards(*point))
        t.forward(t.distance(*point))

    # draw end arrow
    if endArrow == "dot":
        drawDot(endArrowSize)
    elif endArrow == "square":
        t.begin_fill()
        drawSquare(endArrowSize)
        t.end_fill()
    elif endArrow == "triangle":
        leap(-endArrowSize / 2)
        t.lt(90)
        t.begin_fill()
        drawPolygon(endArrowSize, 3)
        t.end_fill()
        t.rt(90)
        leap(endArrowSize / 2)

    endDescription()


# Text drawing
#-------------

FONT_SIZE = 18
TEXT_ALIGN = "center"
FONT = "Arial"
FIXED_WIDTH_FONT_ASPECT_RATIO = 0.6


def fontsize(size):
    """
    Sets the current font size. The default font size is 18. The argument
    must be a number, and will be rounded to the nearest integer (and
    made positive if it was negative).
    """
    global FONT_SIZE
    FONT_SIZE = int(abs(size))


def align(where):
    """
    Sets the current text alignment. The default is "center". The
    argument must be one of the strings "center", "left", or "right",
    or there will be no effect.
    """
    global TEXT_ALIGN
    if where in ("center", "left", "right"):
        TEXT_ALIGN = where


def font(name):
    """
    Sets the current font. The default is 'Arial'. If you select a font
    that isn't installed, I'm not sure what will happen.
    """
    global FONT
    FONT = name


def fixedWidthFont():
    """
    Sets the font to 'Courier New' which is a fixed-width font that
    should be available on almost all systems, since it's a web default
    font. This overrides any prior font selection.

    Since Courier New is a fixed-width font, it has a fixed aspect ratio,
    which is approximately `FIXED_WIDTH_FONT_ASPECT_RATIO` (in the demos
    drawn when you run this file, the red lines have length equal to the
    font size, and the blue lines use `FIXED_WIDTH_FONT_ASPECT_RATIO` as
    the aspect ratio to match the font width).
    """
    global FONT
    FONT = 'Courier New'


def drawText(text):
    """
    Draws the given text using the current font, font size, and alignment
    (see the `font`, `fixedWidthFont`, `fontsize` and `align` functions).
    The text is drawn due North of the current turtle position, no matter
    what direction the turtle is facing, and cannot be rotated. Either
    the left edge, the center, or the right edge of the text will be
    directly above the turtle, depending on the current alignment
    setting. The turtle is not moved by this command.

    If the text contains a newline character, multiple lines of text will
    be written.
    """
    # Note: This will be loudWrite, which will describe itself
    t.write(text, False, TEXT_ALIGN, (FONT, FONT_SIZE, "normal"))


def fontSizeForTextInBox(
    text,
    width,
    height,
    minSize=4,
    maxSize=28,
    aspectRatio=FIXED_WIDTH_FONT_ASPECT_RATIO
):
    """
    Returns a font size number for fitting fixed-width text (using the
    default fixed-width font) into a box with the given width and
    height. This function does not account for any padding.

    The minimum and maximum sizes can be overridden, or set to None to
    disable them (not recommended). A custom aspect ratio can be
    specified to account for an alternate font, although results will
    never be perfect for non-fixed-width fonts.

    TODO: This does not handle multi-line strings properly.

    TODO: Account for custom world coordinates (tough)?
    """
    perChar = width / len(text)
    result = min(height, perChar / aspectRatio)
    if minSize is not None:
        result = max(minSize, result)
    if maxSize is not None:
        result = min(maxSize, result)
    return result


def drawTextInBox(
    text,
    width,
    height,
    minSize=4,
    maxSize=28,
    aspectRatio=FIXED_WIDTH_FONT_ASPECT_RATIO
):
    """
    Draws the given text, centered in a box that's centered on the
    turtle's current position. The box dimensions provided are used to
    scale the font size so that the text fits in the box. An actual box
    is not drawn (but you could call `drawRectangle` to add one).

    The `minSize`, `maxSize`, and `aspectRatio` arguments are passed
    through to `fontSizeForTextInBox`.

    The turtle is returned to its original heading + position when the
    drawing is done, and the font size is changed back to the default.
    If the font is not already Courier New, it will be set to that font
    temporarily.

    Unlike drawText, the text is centered vertically on the turtle's
    position.

    TODO: Get this working for multi-line strings.
    """
    global FONT, FONT_SIZE, TEXT_ALIGN
    origHeading = t.heading()
    origFont = FONT
    origFontSize = FONT_SIZE
    origAlign = TEXT_ALIGN
    fixedWidthFont()
    # Description will come from drawText
    fontSize = fontSizeForTextInBox(
        text,
        width,
        height,
        minSize,
        maxSize,
        aspectRatio
    )
    fontsize(fontSize)
    # Move down to center text
    t.setheading(0)
    hop(-fontSize / 2)

    # Draw the text
    drawText(text)

    # Restore position, heading, font, font size, and text alignment
    hop(fontSize / 2)
    t.setheading(origHeading)
    align(origAlign)
    font(origFont)
    fontsize(origFontSize)


# Random Color Functions
#-----------------------

def randomPastelColor():
    """
    Returns a random pastel color.
    """
    return random.choice([
        # Purple
        "Plum",
        "Thistle",
        # Bluish
        "LightSkyBlue",
        "PaleTurquoise",
        # Green-blue
        "Aquamarine",
        # Greenish
        "PaleGreen",
        # Yellowish/cream
        "LightYellow",
        "BlanchedAlmond",
        # Redish
        "LightPink",
        "MistyRose",
    ])


def randomVibrantColor():
    """
    Returns a random well-saturated color.
    """
    return random.choice([
        "Blue",
        "Navy",
        "Red",
        "DarkRed",
        "Green",
        "ForestGreen",
        "Yellow",
        "Purple",
        "SaddleBrown",
        "SeaGreen",
        "Orange",
        "VioletRed",
    ])


def randomMutedColor():
    """
    Returns a random faded color.
    """
    return random.choice([
        "Aquamarine3",
        "DarkSeaGreen3",
        "DarkOrange3",
        "GoldenRod3",
        "DarkSlateGray4",
        "IndianRed3",
        "Salmon3",
        "MediumPurple2",
        "Plum3",
        "OliveDrab3",
        "PaleGreen3",
    ])


def randomWarmColor():
    """
    Returns a random well-saturated warm color.
    """
    return random.choice([
        # Pinks
        "DeepPink",
        "Salmon",
        # Reds
        "Red",
        "DarkRed",
        "Tomato",
        # Oranges
        "Orange",
        "DarkOrange",
        "Coral",
        # Yellows & browns
        "Yellow",
        "SaddleBrown",
        "Sienna",
        # Greens
        "Chartreuse",
        "YellowGreen",
    ])


def randomCoolColor():
    """
    Returns a random well-saturated cool color.
    """
    return random.choice([
        "Purple",
        "BlueViolet",
        "Blue",
        "DodgerBlue",
        "RoyalBlue",
        "Navy",
        "DarkSlateBlue",
        "Turquoise",
        "SeaGreen",
        "DarkGreen",
        "ForestGreen",
    ])


# Testing
#--------

def test_TurtleBeads():
    """
    Tests this module by drawing various shapes in a grid.
    """
    setupTurtle()

    noTrace()

    teleport(-200, 200)
    drawCircle(50)
    print("Circle done...")

    teleport(-100, 200)
    drawEllipse(50, 0.5)
    print("Ellipse 1 done...")

    teleport(0, 200)
    drawEllipse(40, 1.5)
    print("Ellipse 2 done...")

    teleport(100, 200)
    drawDot(25)
    print("Filled circle done...")

    teleport(200, 200)
    drawSquare(50)
    print("Square done...")

    teleport(-200, 100)
    drawRectangle(50, 75)
    print("Rectangle 1 done...")

    teleport(-100, 100)
    drawRectangle(75, 50)
    print("Rectangle 2 done...")

    teleport(0, 100)
    drawPolygon(40, 3)
    print("Polygon 1 done...")

    teleport(100, 100)
    drawPolygon(40, 5)
    print("Polygon 2 done...")

    teleport(200, 100)
    drawPolygon(20, 12)
    print("Polygon 3 done...")

    teleport(-180, 0)
    drawText("Hello\nWorld")

    fixedWidthFont()
    teleport(-80, 0)
    drawText("Hello\nWorld")
    print("Text done...")

    # Still fixed-width font
    teleport(80, 24)
    align("left")
    text = 'Helloj'
    for fs in range(24, 8, -4):
        fontsize(fs)
        drawText(text)
        width = len(text) * fs * FIXED_WIDTH_FONT_ASPECT_RATIO
        height = fs
        # Blue width line
        t.color('blue')
        fd(width)
        leap(-width)
        # Red height line
        t.color('red')
        t.lt(90)
        fd(height)
        leap(-height)
        t.rt(90)
        hop(-fs)
        text += ' helloj'
        t.color('black')
    print("Text measurement done...")

    showPicture()

    teleport(-200, -80)
    for i in range(10):
        t.fillcolor("navy")
        t.begin_fill()
        t.lt(18.182 * i)
        drawSquare(20.1827 + 1.802938 * i)
        t.rt(18.182 * i)
        t.end_fill()
        leap(50)
    print("Row of squares is done...")

    teleport(-200, -160)
    for i in range(10):
        t.fillcolor("navy")
        t.begin_fill()
        t.lt(18.182 * i)
        drawEllipse(20.1827 + 1.802938 * i, 1.345 + 0.03 * i)
        t.rt(18.182 * i)
        t.end_fill()
        leap(50)
    print("Row of ellipses is done...")
    showPicture()


if __name__ == "__main__":
    test_TurtleBeads()
    input("Press enter when done...")
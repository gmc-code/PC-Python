==========================
Transpose an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.transpose

| Rotate or flip an image using method constants.

----

Transpose variations
----------------------------

| The various flip and rotate methods are below.
| All 7 variations of the original by flipping and/or rotating are below.
| Transpose.TRANSPOSE is the equivalent of rotating 270 and flipping left to right.
| Transpose.TRANSVERSE is the equivalent of rotating 90 and flipping left to right.

.. code-block:: python

    from PIL import Image


    with Image.open("shapes/shapes.png") as im:
        im2 = im.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        im2.save("transforms/flip_lr.png")
        im2 = im.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
        im2.save("transforms/flip_tb.png")
        im2 = im.transpose(method=Image.Transpose.ROTATE_90)
        im2.save("transforms/r_90.png")
        im2 = im.transpose(method=Image.Transpose.ROTATE_180)
        im2.save("transforms/r_180.png")
        im2 = im.transpose(method=Image.Transpose.ROTATE_270)
        im2.save("transforms/r_270.png")
        im2 = im.transpose(method=Image.Transpose.TRANSPOSE)
        im2.save("transforms/tp.png")
        im2 = im.transpose(method=Image.Transpose.TRANSVERSE)
        im2.save("transforms/tv.png")


| All 8 possible orientations are shown.

.. image:: images/transforms.png
    :scale: 50%
    :align: center



    


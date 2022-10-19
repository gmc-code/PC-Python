==========================
Invert an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/ImageChops.html#PIL.ImageChops.invert

----

Invert
---------------------------

| Use the ImageChops.invert method to invert an image.

.. py:function:: ImageChops.invert(image)

    | returns an inverted image
    | **image** is the image to invert.

| The code below inverts an image.
| The original png is in RGBA mode so when inverted a black and white image is returned.
| After converting to RGB mode, the colours are inverted as expected.

.. code-block:: python

    from PIL import Image, ImageChops

    im = Image.open("shapes/shapes_grid.png") 

    im_inv = ImageChops.invert(im)
    im_inv.save("new_images/shapes_grid_inverted.png")

    im_rgb= im.convert(mode='RGB')
    im_rgb_inv = ImageChops.invert(im_rgb)
    im_rgb_inv.save("new_images/shapes_grid_rgb_inverted.png")



 .. image:: images/inverted_shapes.png
    :scale: 50%
    :align: center


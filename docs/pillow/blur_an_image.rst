==========================
Blur  an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
| See: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

----

Blur
----------------------

| Use the **.filter(ImageFilter.GaussianBlur(5))** method to blur an image.

.. code-block:: python

from PIL import Image, ImageFilter


with Image.open("shapes/x.png") as im:
    new_im = im.filter(ImageFilter.GaussianBlur(5))
    new_im.save("shapes/x_blur5.png")
    new_im = im.filter(ImageFilter.GaussianBlur(10))
    new_im.save("shapes/x_blur10.png")
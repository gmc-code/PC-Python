==========================
Save an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save

----

Same file type
----------------

| The code below saves an image.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        im.save("arrows/arrow_0.png")     

----

Save as JPEG
--------------------
    
| The file extension in the new file name is used to specify the file type for saving.
| PNGs need to have the alpha channel removed to save the image as a jpg.
| Use the **.convert('RGB')** method to convert a png image to a jgp before attempting to save it.
| Use the **.save** method specifying the quality parameter as **quality=95** for best quality.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.png") as im:
        new_im = im.convert('RGB')
        new_im.save("shapes/box.jpg", quality=95)

----

Save as PNG
--------------------
    
| The file extension in the new file name is used to specify the file type for saving.
| PNGs need to have the alpha channel removed to save the image as a jpg.
| compress_level is a number between 0 and 9: 1 gives best speed, 9 gives best compression, 0 gives no compression at all. Default is 6.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.jpg") as im:
        new_im.save("shapes/box.png", compress_level=9)


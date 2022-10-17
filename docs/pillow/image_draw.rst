==========================
Image draw
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
| See: https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/

| The ImageDraw module provides simple 2D graphics for Image objects. You can use this module to create new images, annotate or retouch existing images, and to generate graphics on the fly for web use.

----

Blur
----------------------

| Use the **.filter(ImageFilter.BLUR)** method to blur an image.

.. code-block:: python

    from PIL import Image, ImageFilter

    with Image.open("test_images/alph_blocks.png") as im:
        new_im = im.filter(ImageFilter.BLUR)
        new_im.save("filters/blur.png")


.. image:: images/blocks_blur.png
    :scale: 50%
    :align: center
        
----

Sharpen
----------------------

| Use the **.filter(ImageFilter.SHARPEN)** method to sharpen an image.

.. code-block:: python

    from PIL import Image, ImageFilter

    with Image.open("test_images/alph_blocks.png") as im:
        new_im = im.filter(ImageFilter.SHARPEN)
        new_im.save("filters/sharpen.png")


.. image:: images/blocks_sharp.png
    :scale: 50%
    :align: center
    

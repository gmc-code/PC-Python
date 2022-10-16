==========================
Blur  an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
| See: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

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
    

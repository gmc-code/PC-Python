===============================
Load an image for pixel access
===============================

| See: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#merging-images
| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.load
| See: https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html#pixelaccess

----

Multiply
---------------------------

| Use the Image.load method to load the pixel data.
| In normal cases, the Image class automatically loads an opened image when it is accessed for the first time.
| If the file associated with the image was opened by Pillow, then this method will close it.

.. py:function:: Image.load(image)

    | image is the image which will have its pixel data loaded.

| The code below converts and image to black and white using its pixel values.

.. code-block:: python

    from PIL import Image


    b = Image.open("shapes/box.png") 
    o = Image.open("shapes/o.png") 

    imb= b.convert(mode='RGB')
    imo= o.convert(mode='RGB')

    merged = ImageChops.multiply(imb, imo)
    merged.save("new_images/merged.png")
    merged_inv = ImageChops.invert(merged)
    merged_inv.save("new_images/merged_inverted.png")

    merged_pixels = merged.load()
    # access pixels via [x, y] 
    for col in range(merged.size[0]):
        for row in range(merged.size[1]):
            if merged_pixels[col, row] != (255, 255, 255):
                merged_pixels[col, row] = (0, 0, 0)

    merged.save("new_images/merged_black.png")
    merged_inv = ImageChops.invert(merged)
    merged_inv.save("new_images/merged_black_inverted.png")


 .. image:: images/merged_b_o.png
    :scale: 75%
    :align: center


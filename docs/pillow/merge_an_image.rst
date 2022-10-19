==========================
Merge an image
==========================

| See: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#merging-images

----

Multiply
---------------------------

| Use the ImageChops.multiply method to overlay 2 images of the same size.
| If an image is multiplied with an image with a solid black image, the result is black. 
| If an image is multiplied with a solid white image, the image is unaffected.

.. py:function:: ImageChops.multiply(im1, im2)

    | im1 and im2 are the images to multiply.

| The code below overlays a box with a circle.

.. code-block:: python

    from PIL import Image, ImageChops


    b = Image.open("shapes/box.png") 
    o = Image.open("shapes/o.png") 

    imb= b.convert(mode='RGB')
    imo= o.convert(mode='RGB')

    merged = ImageChops.multiply(imb, imo)

    merged.save("new_images/merged_b_o.png")


 .. image:: images/merged_b_o.png
    :scale: 75%
    :align: center



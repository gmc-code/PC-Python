==========================
Rotate an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate

----

Rotate to 90
----------------------------

| The code below rotates an image 90 degrees counterclockwise and saves it with another name.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        im2 = im.rotate(90)
        im2.save("arrows/arrow_90.png")
            
----

Rotate to 90, 180, 270
----------------------------

| The code below rotates an image 90, 180 and 270 degrees and saves them.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        angles = [90, 180, 270]
        for ang in angles:
            im2 = im.rotate(ang)
            im2.save("arrows/arrow_" + str(ang) +".png")

----

Rotate to 45, 135, 225, 315
----------------------------

| The code below rotates an image 45, 135, 225, 315 degrees and saves them.

.. code-block:: python

    from PIL import Image
    
    with Image.open("arrows/Narrow.png") as im:
        angles = [45, 135, 225, 315]
        for ang in angles:
            im2 = im.rotate(ang)
            im2.save("arrows/arrow_" + str(ang) +".png")

----

Rotate and expand
----------------------------

| The code below rotates an image 90, 180 and 270 degrees and saves them.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        angles = [90, 180, 270]
        for ang in angles:
            im2 = im.rotate(ang, expand=1)
            im2.save("arrows/arrow_" + str(ang) +".png")

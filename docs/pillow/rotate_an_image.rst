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

    with Image.open("arrows/arrow_0.png") as im:
        im2 = im.rotate(90)
        im2.save("arrows/arrow_90.png")

.. image:: images/arrows2.png
    :scale: 25%
    :align: center
    
----

Rotate to 90, 180, 270
----------------------------

| The code below rotates an image 90, 180 and 270 degrees and saves them.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/arrow_0.png") as im:
        angles = [90, 180, 270]
        for ang in angles:
            im2 = im.rotate(ang)
            im2.save("arrows/arrow_" + str(ang) +".png")

.. image:: images/arrows4.png
    :scale: 25%
    :align: center
    
----

Rotate to 45, 135, 225, 315
----------------------------

| The code below rotates an image 45, 135, 225, 315 degrees and saves them.

.. code-block:: python

    from PIL import Image
    
    with Image.open("arrows/arrow_0.png") as im:
        angles = [45, 135, 225, 315]
        for ang in angles:
            im2 = im.rotate(ang)
            im2.save("arrows/arrow_" + str(ang) +".png")

.. image:: images/arrows4x.png
    :scale: 25%
    :align: center

----

Rotate and expand
----------------------------

| The code below rotates an image 90, 180 and 270 degrees and saves them.

.. code-block:: python

    from PIL import Image

    with Image.open("rotations/egg.png") as im:
        angles = [0, 90, 180, 270]
        for ang in angles:
            im2 = im.rotate(ang, expand=1)
            im2.save("rotations/egg_" + str(ang) +".png")

.. image:: images/eggs4hor.png
    :scale: 25%   
    :align: center

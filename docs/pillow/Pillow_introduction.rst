==========================
Pillow Introduction
==========================

| https://pypi.org/project/Pillow/

.. code-block:: python

    from PIL import Image
    #Open image using Image module
    im = Image.open("images/cuba.jpg")
    #Show actual Image
    im.show()
    #Show rotated Image
    im = im.rotate(45)
    im.show()
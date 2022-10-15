==========================
Open an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/open_files.html#file-handling


| The code below shows how to open an image and show it.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        im.show()
        


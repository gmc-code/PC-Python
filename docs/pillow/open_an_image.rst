==========================
Open an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/open_files.html#file-handling


| The code below opens an image and shows it.
| Use **with** to automatically close the file resource.
| To refer to the image object as **img** use **as img**.
| The file below is assumed to be in the same folder as the python script.

.. code-block:: python

    from PIL import Image

    with Image.open("Narrow.png") as img:
        img.show()
         
| The file below is in the "arrows" folder within the folder containing the python script.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as img:
        img.show()
        

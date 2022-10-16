==========================
Show an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.show

| The code below opens an image and shows it.
| The **.show()** method uses the default app for opening the image extension.
| A temporary file is created for display.
| In Windows, the default app is usually Photos.
| This can be changed in Windows to suit. Type "default apps" in windows search. Then scroll down to "Choose default apps by file type".


.. code-block:: python

    from PIL import Image

    with Image.open("tri.png") as im:
        im.show()
         
.. image:: images/tri.png
    :scale: 50%
        

==========================
Open an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/open_files.html#file-handling

----

Open file in same folder
---------------------------

| The code below opens an image and shows it.
| Use **with** to automatically close the file resource.
| To refer to the image object as **im** use **as im**.
| The file below is assumed to be in the same folder as the python script.

.. code-block:: python

    from PIL import Image

    with Image.open("Narrow.png") as im:
        im.show()

----

Open file in subfolder
---------------------------

| The file below is in the "arrows" folder within the folder containing the python script.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        im.show()

----

Open file from url
---------------------------

| The code belwo uses the **urllib.request** library to help open an image url.

.. code-block:: python

    from PIL import Image
    from urllib.request import urlopen

    url = "https://pc-python.readthedocs.io/en/latest/_images/Narrow.png"

    with Image.open(urlopen(url)) as im:
        im.show()


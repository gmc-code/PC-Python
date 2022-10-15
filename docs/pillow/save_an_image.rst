==========================
Save an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save

----

Same file type
----------------


| The code below saves an image.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        im.save("arrows/arrow_0.png")     

----

Different file type
--------------------
    
| The file extension in the new file name is used to specify the file type for saving.
| PNGs need to have the alpha channel removed to save the image as a jpg.
| Use the **.convert('RGB')** method to convert a png image to a jgp before attempting to save it.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.png") as im:
        new_im = im.convert('RGB')
        new_im.save("shapes/box.jpg")


----

Convert a folder to jpgs using pathlib
-------------------------------------------

| See: https://docs.python.org/3/library/pathlib.html

| Use the built in **pathlib** library for the file handling.
| Convert pngs to jpgs and save in the new folder.

| Get the current working directory, cwd, with **Path.cwd()**.
| Create the path to the shapes folder: **cwd / "shapes"**.
| List the files in the shapes folder: **shapes.iterdir()**
| Build the path to the new directory for the converted files: **cwd / "shapes_jpgs"**
| After checking that it does not already exist, make the new directory for the converted files: **new_shapes.mkdir()**
| Get the file extension via: **f.suffix**
| Get the file name via: **f.name**
| Get the file name without the extension via: **f.stem**


.. code-block:: python

    from PIL import Image
    from pathlib import Path

    # https://docs.python.org/3/library/pathlib.html

    im_dir = "shapes"
    im_new_dir = "shapes_jpgs"
    cwd = Path.cwd()
    shapes = cwd / im_dir
    shape_files = shapes.iterdir()
    new_shapes = cwd / im_new_dir
    if not(new_shapes.exists()):
        new_shapes.mkdir()
    for f in shape_files:
        if f.suffix == ".png":
            with Image.open(im_dir + "/" + f.name) as im:
                new_im = im.convert('RGB')
                new_im.save(im_new_dir + "/" + f.stem + ".jpg")

----

Convert a folder to jpgs using os
---------------------------------------

| See: https://docs.python.org/3/library/pathlib.html

| Use the built in **os** library for the file handling.
| Convert pngs to jpgs and save in the new folder.

| List the files in the shapes folder: **os.listdir(im_dir)**
| After checking that it does not already exist, make the new directory for the converted files: **os.mkdir(im_new_dir)**
| Check that the file is a png file via: **f.endswith(".png")**
| Get the file name without the extension via: **fn, fext = os.path.splitext(f)**

.. code-block:: python

    from PIL import Image
    import os

    im_dir = "shapes"
    im_new_dir = "shapes0_jpgs"
    shape_files = os.listdir(im_dir)

    if not(os.path.exists(im_new_dir)):
        os.mkdir(im_new_dir)

    for f in shape_files:
        if f.endswith(".png"):
            with Image.open(im_dir + "/" + f) as im:
                new_im = im.convert('RGB')
                fn, fext = os.path.splitext(f)
                new_im.save(im_new_dir + "/" + fn + ".jpg")



==========================
Resize an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize

----

Resize to a specific size
----------------------------

| The code below resizes an image and saves it with another name.

.. code-block:: python

    from PIL import Image

    full_path = path.resolve()

    print(full_path)   
    
    with Image.open("shapes/o.png") as im:
        (curr_width, curr_height) = (im.width, im.height)
        (width, height) = (im.width // 2, im.height // 2)
        box_to_resize = (0, 0, width, height)
        im_new = im.resize((curr_width, curr_height), box=box_to_resize)
        im_new.save("shapes/o_section.png")




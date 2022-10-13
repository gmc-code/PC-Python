==========================
Images with Pillow
==========================

| See https://www.youtube.com/watch?v=5QR-dG68eNE
| See: https://www.youtube.com/watch?v=6Qs3wObeWwc

| The code below shows how to open an image and print out some info about it.

.. code-block:: python

    from PIL import Image

    im = Image.open("pixel_flip_hor.png")
    print(im.format, im.size, im.mode)
    # PNG (700, 700) RGBA


================================================
Pizza orders Lesson 1: Introduction to Tkinter
================================================

Lesson 1: Introduction to Tkinter
---------------------------------
- **Objective**: Set up the basic Tkinter window.
- **Content**:
  - Introduction to Tkinter.
  - Creating a basic window.
  - Adding a title and configuring the window size.

Lesson 1: Introduction to Tkinter
=================================

Objective
---------
Set up the basic Tkinter window.

Content
-------

1. Introduction to Tkinter
   - Tkinter is a standard GUI (Graphical User Interface) library for Python.
   - It provides tools to create desktop applications with windows, buttons, text fields, and more.

2. Creating a Basic Window

.. code-block:: python

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.title("Pizza Order System")
    root.geometry("400x300")

    # Run the application
    root.mainloop()

- ``import tkinter as tk``: Imports the Tkinter library and assigns it the alias ``tk``.
- ``root = tk.Tk()``: Creates the main application window.
- ``root.title("Pizza Order System")``: Sets the title of the window.
- ``root.geometry("400x300")``: Sets the size of the window to 400 pixels wide and 300 pixels tall.
- ``root.mainloop()``: Starts the Tkinter event loop, which waits for user interactions.

1. Additional Examples
   - Setting a minimum and maximum window size:

.. code-block:: python

   root.minsize(300, 200)
   root.maxsize(600, 400)

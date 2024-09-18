==========================
Text files
==========================

| See: https://www.w3schools.com/python/python_ref_file.asp
| See: https://www.w3schools.com/python/python_file_handling.asp

| See: https://docs.python.org/3/library/functions.html#open
| See: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

| Corey Schafer video See: https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=11
| Socratica video See: https://www.youtube.com/watch?v=4mX0uPQFLDU&list=RDCMUCW6TXMZ5Pq6yL6_k5NZ2e0Q&index=7

| Download the test csv file :download:`12days.txt <files/12days.txt>`

----

Reading files
--------------------------

| The code below opens a file for reading, reads the file, prints the file contents, then closes the file.
| ``f`` is commonly used to refer to the file object from opening a file.

.. code-block:: python
    
    filepath = "files/12days.txt"
    f = open(filepath, "r")
    print(f.read())
    f.close()

| The syntax used in each line of the code above is described below.

----
 
Open file:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Use the ``open()`` function to open a file.

| The most used syntax is:

.. py:function:: open(file, mode='r')

    :param file: a string for the file path to the file from the current directory.
    :param mode: a string; "r" to read; "w" to write; "a" to append; "r+" to read and write; "b" for binary; "t" for text. Defaults are "rt" for read text.

    | Open file and return a corresponding file object.

| The recommended syntax is:

.. py:function:: open(file, mode='r', encoding="utf-8")


| For advanced parameter usage see: https://docs.python.org/3/library/functions.html#open
| The full Syntax for advanced use:

.. py:function:: open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

    :param file: a string for the file path to the file from the current directory.
    :param mode: a string; "r" to read; "w" to write; "a" to append; "r+" to read and write; "b" for binary; "t" for text. Defaults are "rt" for read text.
    :param buffering: an optional integer used to set the buffering policy.
    :param encoding: defaults to system; "utf-8" is recommended; see: https://docs.python.org/3/library/codecs.html#standard-encodings
    :param errors: an optional string that specifies how encoding and decoding errors are to be handled.
    :param newline: a string; can be None, '', '\n', '\r', or '\r\n'
    :param closefd: if a filename is given closefd must be True otherwise, an error will be raised.
    :param opener: A custom opener can be used by passing a callable as opener.

    | Open file and return a corresponding file object.

----

Close file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Use the ``close()`` method to close the file object after opening it.

Syntax:

.. py:function:: f.close()


----

Read method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Use the ``read`` method to read the whole of a small file.

Syntax:

.. py:function:: fileobject.read(size)

    :param size: the number of characters (in text mode) or bytes (in binary mode) that are read; default 0 or omitted for whole file.

----

Context manager approach
--------------------------

| The recommended approach for opening files is to use a context manager, **"with ... as ..."**, so that the file is closed automatically.
| See: https://realpython.com/python-with-statement/
| The code below reads the whole file and prints it.

.. code-block:: python
    
    filepath = "files/12days.txt"
    with open(filepath, "r") as f:
        f_contents = f.read()
        print(f_contents)

----

Readlines
--------------------------

| To read all the lines of a file into a list, list(f) or f.readlines() can be used.
| Use readlines to create a list of lines of the file.

Syntax:

.. py:function:: f.readlines(size)

    :param size: optional; the number of characters or bytes returned exceed the size number, no more lines will be returned after that are returned.


.. code-block:: python
    
    filepath = "files/12days.txt"
    with open(filepath, "r") as f:
        f_contents = f.readlines()
        print(f_contents)

| The code above prints a list of lines returned by ``f.readlines()``.

.. code-block::

    ['1 partridge in a pear tree\n', '2 turtle-doves\n', ...]

----

Iterating through the file
-----------------------------

| Use ``for line in f`` to efficiently iterate over the lines of the file.
| This prints each line.

.. code-block:: python
    
    filepath = "files/12days.txt"
    with open(filepath, "r") as f:
        for f_line in f:
            print(f_line, end="")


----
 
Write to a file
-----------------------------

| Use ``w`` as the mode to write to a file.
| The code below writes "Test" to the file called "new_file.txt".
| If the file exists, it overwrites it.
| If the file doesn't exist, it creates it.

.. code-block:: python
    
    filepath = "files/new_file.txt"
    with open(filepath, "w") as f:
        f.write("Test")


----
 

Appending to a text file
-----------------------------

| Use ``a`` as the mode to append to the end of a file.
| If the file exists, it appends it.
| If the file doesn't exist, it creates it.

| In the code below, the file is first opened in "w" mode to clear it and write to it.
| Then the file is opened in "a" mode to add text to the end of it.
| "\n" add a line ending to put the second text on a next line.


.. code-block:: python
    
    filepath = "files/new_file.txt"
    # overwrite file if it exists
    with open(filepath, "w") as f:
        f.write("Test 1")
    # open again for appending
    with open(filepath, "a") as f:
        f.write("\nTest 2")

----

Copying parts of a text file
-----------------------------

| In the code below, rf is the read file object.
| wf is the file object for writing.
| Multiple lines can be written to the same file within the **with open** context mamnager.

| The code below copies each line of the file **12days.txt** to the file **12days_copy.txt**.

.. code-block:: python
    
    rfilepath = "files/12days.txt"
    wfilepath = "files/12days_copy.txt"
    with open(rfilepath, "r") as rf:
        with open(wfilepath, "w") as wf:
            for line in rf:
                wf.write(line)

.. code-block:: 

    1 partridge in a pear tree
    2 turtle-doves
    3 French hens
    ...

| Every second line can be copied by enumerating the file object, rf, then using the modulus operator, %, to get every second line.

.. code-block:: python

    step = 2
    rfilepath = "files/12days.txt"
    wfilepath = "files/12days_copy.txt"
    with open(rfilepath, "r") as rf:
        with open(wfilepath, "w") as wf:
            for lineno, f_line in enumerate(rf):
                if lineno % step == 0:
                    wf.write(f_line)

.. code-block:: 

    1 partridge in a pear tree
    3 French hens
    5 golden rings
    ...


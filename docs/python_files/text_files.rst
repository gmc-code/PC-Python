==========================
Text files
==========================

| See: https://www.w3schools.com/python/python_ref_file.asp
| See: https://www.w3schools.com/python/python_file_handling.asp

| See: https://docs.python.org/3/library/functions.html#open
| See: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

| See video guide at: https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=11

----

Reading files
=====================================

| The code below opens a file for reading, prints the file name and mode used, reads and prints the file contents and then closes the file.
| ``f`` is commonly used to refer to the file object from reading a file.

.. code-block:: python
    
    f = open("files/12days.txt", "r")
    print(f.name)
    print(f.mode)
    print(f.read())
    f.close()

| The syntax used in the code above is decribed below.
 
Open file
-------------

| Use the ``open()`` function to open a file.

Syntax:

.. py:function:: open(filename, mode, encoding=None)

    :param filename: a strng for the file path to the file from the current directory.
    :param mode: a tring; "r" to read; "w" to write; "a" to append; "r+" to read and write; "b" for binary; "t" for text. Defaults are "rt" for read text.
    :param encoding: defaults to system; "utf-8" is recommended; see: https://docs.python.org/3/library/codecs.html#standard-encodings

----

Close file
-------------

| Use the ``close()`` method to close the file object after opening it.

Syntax:

.. py:function:: fileobject.close()

    :param fileobject: the object returned from opening a file.

----

name attribute
-----------------

| Use the ``name`` attribute to get the file name of a file object.

Syntax:

.. py:attribute:: fileobject.name

    :param fileobject: the object returned from opening a file.

----

mode attribute
-----------------

| Use the ``mode`` attribute to get the mode used when opening the file.

Syntax:

.. py:attribute:: fileobject.mode

    :param fileobject: the object returned from opening a file.

----

read method
-----------------

| Use the ``read`` method to read the whole of a small file.

Syntax:

.. py:function:: fileobject.read(size)

    :param size: the number of characters (in text mode) or bytes (in binary mode) that are read; default 0 for whole file.

----

Context manager approach
--------------------------

| The recommended approach for opening files is to use a context manager, "with ... as ...", so that the file is closed automatically.
| See: https://realpython.com/python-with-statement/
| The code below reads the whole file and prints it.

.. code-block:: python
    
    with open("files/12days.txt", "r") as f:
        f_contents = f.read()
        print(f_contents)

----

Readlines
--------------------------

| Use readlines to create a list of lines of the file.

Syntax:

.. py:function:: fileobject.readlines(size)

    :param size: optional; the number of characters or bytes returned exceed the size number, no more lines will be returned after that are returned.


.. code-block:: python
    
    with open("files/12days.txt", "r") as f:
        f_contents = f.readlines()
        print(f_contents)

| The code above prints a list of lines returned by ``f.readlines()``.
| ['1 partridge in a pear tree\n', '2 turtle-doves\n', ...]

----

Iterating through the file
-----------------------------

| Use ``for line in f`` to efficiently iterate over the lines of the file.

.. code-block:: python
    
    with open("files/12days.txt", "r") as f:
        for f_line in f:
            print(f_line, end="")

| This prints each line.

----
 

    ##Writing Files:
    ###The Error:
    #with open("files/12days.txt", "r") as f:
        #f.write("Test")

    ###Writing Starts:
    #with open("test2.txt", "w") as f:
        #pass
        #f.write("Test")
        #f.seek(0)
        #f.write("Test")
        #f.seek("R")

    ##Copying Files:
    #with open("files/12days.txt", "r") as rf:
        #with open("test_copy.txt", "w") as wf:
            #for line in rf:
                #wf.write(line)

    #Copying the/your image:
    ###The Error
    #with open("bronx.jpg", "r") as rf:
        #with open("bronx_copy.jpg", "w") as wf:
            #for line in rf:
                #wf.write(line)

    ###Copying the image starts, without chunks:
    #with open("bronx.jpg", "rb") as rf:
        #with open("bronx_copy.jpg", "wb") as wf:
            #for line in rf:
                #wf.write(line)

    ###Copying the image with chunks:
    #with open("bronx.jpg", "rb") as rf:
        #with open("bronx_copy.jpg", "wb") as wf:
            #chunk_size = 4096
            #rf_chunk = rf.read(chunk_size)
            #while len(rf_chunk) > 0:
                #wf.write(rf_chunk)
                #rf_chunk = rf.read(chunk_size)
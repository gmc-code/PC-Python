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


Open file
-------------

| Use the ``open()`` funnction to open a file.

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

.. py:function:: fileobject.name

    :param fileobject: the object returned from opening a file.

----

mode attribute
-----------------

| Use the ``mode`` attribute to get the mode used when opening the file.

Syntax:

.. py:function:: fileobject.mode

    :param fileobject: the object returned from opening a file.

----

read method
-----------------

| Use the ``read`` method to read the whole of a small file.

Syntax:

.. py:function:: fileobject.read(size)

    :param size: the number of characters (in text mode) or bytes (in binary mode) that are read; default 0 for whole file.

----

| ``f`` is commonly used to refer to the file object from reading a file.
| The code below opens the file for reading, prints the file name and mode used, prints the file contents and then closes the file.

.. code-block:: python
    
    f = open("files/12days.txt", "r")
    print(f.name)
    print(f.mode)
    print(f.read())
    f.close()

----

Context manager approach
--------------------------

| The recommended approach for opening files is to use a context manager, "with", so that the file is closed automatically.
| The code below reads the whole file and prints it.

.. code-block:: python
    
    with open("files/12days.txt", "r") as f:
        f_contents = f.read()
        print(f_contents)


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

| This returns a list of lines:
| ['1 partridge in a pear tree\n', '2 turtle-doves\n', ...]


----


        ###With the extra lines:
        #f_contents = f.readline()
        #print(f_contents)
        #f_contents = f.readline()
        #print(f_contents)

        ###Without the extra lines:
        #f_contents = f.readline()
        #print(f_contents, end = '')
        #f_contents = f.readline()
        #print(f_contents, end = '')

        ###Iterating through the file:
        #for line in f:
            #print(line, end = '')

        ###Going Back....:
        #f_contents = f.read()
        #print(f_contents, end = '')

        ###Printing by characters:
        #f_contents = f.read(100)
        #print(f_contents, end = '')
        #f_contents = f.read(100)
        #print(f_contents, end = '')
        #f_contents = f.read(100)
        #print(f_contents, end = '')

        ###Iterating through small chunks:
        #size_to_read = 100
        #f_contents = f.read(size_to_read)
        #while len(f_contents) > 0:
            #print(f_contents)
            #f_contents = f.read(size_to_read)

        ###Iterating through small chunks, with 10 characters:
        #size_to_read = 10
        #f_contents = f.read(size_to_read)
        #print(f_contents, end = '')
        #f.seek(0)
        #f_contents = f.read(size_to_read)
        #print(f_contents, end = '')
        #print(f.tell())
        #while len(f_contents) > 0:
            #print(f_contents, end = '*')
            #f_contents = f.read(size_to_read)
    #print(f.mode)
    #print(f.closed)
    #print(f.read())


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
==========================
Text files
==========================

See: https://docs.python.org/3/library/functions.html#open
See: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
See: https://www.w3schools.com/python/python_file_handling.asp
See video guide at: https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=11

----

Reading files
=====================================

| List

Syntax:

.. py:function:: open(filename, mode, encoding=None)

    :param filename: a strng for the file path to the file from the current directory.
    :param mode: a tring; "r" to read; "w" to write; "a" to append; "r+" to read and write; "b" for bonart; "t" for text.
    Defaults are "rt" for read text.
    :param encoding: defaults to system; "utf-8" is recommended; see: https://docs.python.org/3/library/codecs.html#standard-encodings

| A list comprehension consists of brackets containing an expression followed by a for clause.
| 

.. code-block:: python
    
    #File Objects

    ##The Basics:
    #f = open("files/12days.txt", "r")
    #f = open("files/12days.txt", "w")
    #f = open("files/12days.txt", "a")
    #f = open("files/12days.txt", "r+")
    #print(f.name)
    #print(f.mode)
    #f.close()

    ##Reading Files:
    #with open("files/12days.txt", "r") as f:
        #pass

        ##Small Files:
        #f_contents = f.read()
        #print(f_contents)

        ##Big Files:
        #f_contents = f.readlines()
        #print(f_contents)

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
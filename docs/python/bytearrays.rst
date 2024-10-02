==========================
Bytearrays
==========================

| `bytearray` objects in Python can be modified.
| The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.

Syntax:

.. py:method:: bytearray = bytearray(x, encoding, error)

    Returns a bytearray object. It can create empty bytearray object of the specified size or convert objects into bytearray objects.
    :param x: If x is an integer, an empty bytearray object of the specified size will be created.
    :param x: If x is a String, the encoding is required.
    :param x: If x is an iterable, such as a list, it must be of integers from 0 to 255.
    :param encoding:  The encoding of the string such as 'utf-8'
    :param error: Specifies what to do if the encoding fails.

| An example is below.

.. code-block:: python

    x = bytearray(4)
    print(x)
    # Output is bytearray(b'\x00\x00\x00\x00')

.. code-block:: python

    x = bytearray("abc123", "utf-8")
    print(x)
    # Output is bytearray(b'abc123')

----

bytearray Methods
-----------------------

The `bytearray` type in Python provides a variety of methods for manipulating and interacting with byte data. Below are some commonly used methods:

----

append
----------------

.. py:method:: append(x)

    Append a single byte to the end of the bytearray.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.append(68)
        print(my_ba)
        # Output is bytearray(b'ABCD')

----

append
----------------

.. py:method:: extend(iterable)

    Extend the bytearray by appending elements from the iterable.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.extend([68, 69])
        print(my_ba)
        # Output is bytearray(b'ABCDE')

----

append
----------------

.. py:method:: insert(i, x)

    Insert a single byte at a given position.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.insert(1, 68)
        print(my_ba)
        # Output is bytearray(b'ADBC')

----

append
----------------

.. py:method:: remove(x)

    Remove the first occurrence of a byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67, 66])
        my_ba.remove(66)
        print(my_ba)
        # Output is bytearray(b'ACB')

----

append
----------------

.. py:method:: pop([i])

    Remove and return a byte at a given position. If no index is specified, removes and returns the last byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        byte = my_ba.pop(1)
        print(byte)
        # Output is 66
        print(my_ba)
        # Output is bytearray(b'AC')

----

append
----------------

.. py:method:: clear()

    Remove all bytes from the bytearray.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.clear()
        print(my_ba)
        # Output is bytearray(b'')

----

append
----------------

.. py:method:: count(x)

    Return the number of occurrences of a byte.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67, 66])
        count = my_ba.count(66)
        print(count)
        # Output is 2

----

append
----------------

.. py:method:: find(sub[, start[, end]])

    Return the lowest index where the subsequence is found.

    Example:

    .. code-block:: python

        my_ba = bytearray(b'Hello, World!')
        index = my_ba.find(b'World')
        print(index)
        # Output is 7

----

append
----------------

.. py:method:: reverse()

    Reverse the bytes in place.

    Example:

    .. code-block:: python

        my_ba = bytearray([65, 66, 67])
        my_ba.reverse()
        print(my_ba)
        # Output is bytearray(b'CBA')

----

append
----------------

.. py:method:: decode(encoding='utf-8', errors='strict')

    Decode the bytearray to a string using the specified encoding.

    Example:

    .. code-block:: python

        my_ba = bytearray(b'Hello, World!')
        string = my_ba.decode('utf-8')
        print(string)
        # Output is Hello, World!


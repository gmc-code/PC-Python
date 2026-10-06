==========================
Bytes
==========================

| `bytes` objects in Python are immutable, so they don't have methods that modify the object in place like `bytearray` does.
| The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
| However, the methods provide a range of functionalities for working with `bytes` objects, allowing you to search, split, join, replace, and decode byte sequences.

Syntax:

.. py:method:: bytes_var = bytes(x, encoding, error)

    Returns a bytes object. It can create empty bytes object of the specified size or convert objects into bytes objects.

    :param x: If x is an integer, an empty bytes object of the specified size will be created.
    :param x: If x is a String, the encoding is required.
    :param x: If x is an iterable, such as a list, it must be of integers from 0 to 255.
    :param encoding:  The encoding of the string such as 'utf-8'
    :param error: Specifies what to do if the encoding fails.

| An example is below.

.. code-block:: python

    x = bytes(4)
    print(x)
    # Output is b'\x00\x00\x00\x00'

.. code-block:: python

    x = bytes("abc123", "utf-8")
    print(x)
    # Output is b'abc123'

.. code-block:: python

    num_list = [1, 2, 3, 4, 5]
    num_list_bytes = bytes(num_list)
    print(num_list_bytes)
    # Output is b'\x01\x02\x03\x04\x05'

.. code-block:: python

    num_list = range(256)
    num_list_bytes = bytes(num_list)
    print(num_list_bytes)
    '''Output is
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
    '''

----

bytes Methods
------------------------

The `bytes` type in Python provides a variety of methods for interacting with and manipulating byte data. Below are some commonly used methods:

----

count
----------------------------

.. py:method:: count(sub[, start[, end]])

    Return the number of non-overlapping occurrences of the substring `sub`.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        count = my_bytes.count(b'o')
        print(count)  # Output: 2

----

find
----------------------------

.. py:method:: find(sub[, start[, end]])

    Return the lowest index where the substring `sub` is found.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        index = my_bytes.find(b'World')
        print(index)  # Output: 7

----

index
----------------------------

.. py:method:: index(sub[, start[, end]])

    Like `find()`, but raises a `ValueError` if the substring is not found.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        index = my_bytes.index(b'World')
        print(index)  # Output: 7

----

split
----------------------------

.. py:method:: split(sep=None, maxsplit=-1)

    Split the bytes object into a list of byte objects, using `sep` as the delimiter.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        parts = my_bytes.split(b', ')
        print(parts)  # Output: [b'Hello', b'World!']

----

join
----------------------------

.. py:method:: join(iterable)

    Concatenate any number of bytes objects, with the bytes object acting as a separator.

    Example:

    .. code-block:: python

        parts = [b'Hello', b'World!']
        joined = b', '.join(parts)
        print(joined)  # Output: b'Hello, World!'

----

replace
----------------------------

.. py:method:: replace(old, new[, count])

    Return a copy of the bytes object with all occurrences of the substring `old` replaced by `new`.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        replaced = my_bytes.replace(b'World', b'Python')
        print(replaced)  # Output: b'Hello, Python!'

----

strip
----------------------------

.. py:method:: strip([chars])

    Return a copy of the bytes object with leading and trailing whitespace removed.

    Example:

    .. code-block:: python

        my_bytes = b"  Hello, World!  "
        stripped = my_bytes.strip()
        print(stripped)  # Output: b'Hello, World!'

----

startswith
----------------------------

.. py:method:: startswith(prefix[, start[, end]])

    Return `True` if the bytes object starts with the specified prefix.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        result = my_bytes.startswith(b'Hello')
        print(result)  # Output: True

----

endswith
----------------------------

.. py:method:: endswith(suffix[, start[, end]])

    Return `True` if the bytes object ends with the specified suffix.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        result = my_bytes.endswith(b'World!')
        print(result)  # Output: True

----

decode
----------------------------

.. py:method:: decode(encoding='utf-8', errors='strict')

    Decode the bytes object to a string using the specified encoding.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        string = my_bytes.decode('utf-8')
        print(string)  # Output: Hello, World!




==========================
bytes
==========================

| `bytes` objects in Python are immutable, so they don't have methods that modify the object in place like `bytearray` does.
| However, they do have a variety of methods that allow you to interact with and manipulate the data.
| These methods provide a range of functionalities for working with `bytes` objects, allowing you to search, split, join, replace, and decode byte sequences.


bytes Methods
------------------------

The `bytes` type in Python provides a variety of methods for interacting with and manipulating byte data. Below are some commonly used methods:

----

count
~~~~~~~~~~~~~~

.. py:method:: count(sub[, start[, end]])

    Return the number of non-overlapping occurrences of the substring `sub`.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        count = my_bytes.count(b'o')
        print(count)  # Output: 2

----

find
~~~~~~~~~~~~~~

.. py:method:: find(sub[, start[, end]])

    Return the lowest index where the substring `sub` is found.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        index = my_bytes.find(b'World')
        print(index)  # Output: 7

----

index
~~~~~~~~~~~~~~

.. py:method:: index(sub[, start[, end]])

    Like `find()`, but raises a `ValueError` if the substring is not found.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        index = my_bytes.index(b'World')
        print(index)  # Output: 7

----

split
~~~~~~~~~~~~~~

.. py:method:: split(sep=None, maxsplit=-1)

    Split the bytes object into a list of byte objects, using `sep` as the delimiter.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        parts = my_bytes.split(b', ')
        print(parts)  # Output: [b'Hello', b'World!']

----

join
~~~~~~~~~~~~~~

.. py:method:: join(iterable)

    Concatenate any number of bytes objects, with the bytes object acting as a separator.

    Example:

    .. code-block:: python

        parts = [b'Hello', b'World!']
        joined = b', '.join(parts)
        print(joined)  # Output: b'Hello, World!'

----

replace
~~~~~~~~~~~~~~

.. py:method:: replace(old, new[, count])

    Return a copy of the bytes object with all occurrences of the substring `old` replaced by `new`.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        replaced = my_bytes.replace(b'World', b'Python')
        print(replaced)  # Output: b'Hello, Python!'

----

strip
~~~~~~~~~~~~~~

.. py:method:: strip([chars])

    Return a copy of the bytes object with leading and trailing whitespace removed.

    Example:

    .. code-block:: python

        my_bytes = b"  Hello, World!  "
        stripped = my_bytes.strip()
        print(stripped)  # Output: b'Hello, World!'

----

startswith
~~~~~~~~~~~~~~

.. py:method:: startswith(prefix[, start[, end]])

    Return `True` if the bytes object starts with the specified prefix.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        result = my_bytes.startswith(b'Hello')
        print(result)  # Output: True

----

endswith
~~~~~~~~~~~~~~

.. py:method:: endswith(suffix[, start[, end]])

    Return `True` if the bytes object ends with the specified suffix.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        result = my_bytes.endswith(b'World!')
        print(result)  # Output: True

----

decode
~~~~~~~~~~~~~~

.. py:method:: decode(encoding='utf-8', errors='strict')

    Decode the bytes object to a string using the specified encoding.

    Example:

    .. code-block:: python

        my_bytes = b"Hello, World!"
        string = my_bytes.decode('utf-8')
        print(string)  # Output: Hello, World!




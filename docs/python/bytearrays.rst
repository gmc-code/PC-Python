==========================
bytearrays
==========================

| `bytearray` objects in Python come with a variety of methods that allow you to manipulate and interact with the byte data. Here are some of the most commonly used methods:
| These methods provide a lot of flexibility for working with bytearrays, allowing you to manipulate the data in various ways.

### Common Methods for `bytearray`


bytearray Methods
=================

The `bytearray` type in Python provides a variety of methods for manipulating and interacting with byte data. Below are some commonly used methods:

.. py:class:: bytearray

    .. py:method:: append(x)
        :noindex:

        Append a single byte to the end of the bytearray.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            my_ba.append(68)
            print(my_ba)  # Output: bytearray(b'ABCD')

    .. py:method:: extend(iterable)
        :noindex:

        Extend the bytearray by appending elements from the iterable.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            my_ba.extend([68, 69])
            print(my_ba)  # Output: bytearray(b'ABCDE')

    .. py:method:: insert(i, x)
        :noindex:

        Insert a single byte at a given position.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            my_ba.insert(1, 68)
            print(my_ba)  # Output: bytearray(b'ADBC')

    .. py:method:: remove(x)
        :noindex:

        Remove the first occurrence of a byte.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67, 66])
            my_ba.remove(66)
            print(my_ba)  # Output: bytearray(b'ACB')

    .. py:method:: pop([i])
        :noindex:

        Remove and return a byte at a given position. If no index is specified, removes and returns the last byte.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            byte = my_ba.pop(1)
            print(byte)  # Output: 66
            print(my_ba)  # Output: bytearray(b'AC')

    .. py:method:: clear()
        :noindex:

        Remove all bytes from the bytearray.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            my_ba.clear()
            print(my_ba)  # Output: bytearray(b'')

    .. py:method:: count(x)
        :noindex:

        Return the number of occurrences of a byte.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67, 66])
            count = my_ba.count(66)
            print(count)  # Output: 2

    .. py:method:: find(sub[, start[, end]])
        :noindex:

        Return the lowest index where the subsequence is found.

        Example:
        .. code-block:: python

            my_ba = bytearray(b'Hello, World!')
            index = my_ba.find(b'World')
            print(index)  # Output: 7

    .. py:method:: reverse()
        :noindex:

        Reverse the bytes in place.

        Example:
        .. code-block:: python

            my_ba = bytearray([65, 66, 67])
            my_ba.reverse()
            print(my_ba)  # Output: bytearray(b'CBA')

    .. py:method:: decode(encoding='utf-8', errors='strict')
        :noindex:

        Decode the bytearray to a string using the specified encoding.

        Example:
        .. code-block:: python

            my_ba = bytearray(b'Hello, World!')
            string = my_ba.decode('utf-8')
            print(string)  # Output: Hello, World!



1. **`append(x)`**: Appends a single byte to the end of the bytearray.

   .. code-block:: python

      my_ba = bytearray([65, 66, 67])
      my_ba.append(68)
      print(my_ba)  # Output: bytearray(b'ABCD')


2. **`extend(iterable)`**: Extends the bytearray by appending elements from the iterable.

   .. code-block:: python

      my_ba = bytearray([65, 66, 67])
      my_ba.extend([68, 69])
      print(my_ba)  # Output: bytearray(b'ABCDE')


3. **`insert(i, x)`**: Inserts a single byte at a given position.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67])
   my_ba.insert(1, 68)
   print(my_ba)  # Output: bytearray(b'ADBC')


4. **`remove(x)`**: Removes the first occurrence of a byte.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67, 66])
   my_ba.remove(66)
   print(my_ba)  # Output: bytearray(b'ACB')


5. **`pop([i])`**: Removes and returns a byte at a given position. If no index is specified, removes and returns the last byte.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67])
   byte = my_ba.pop(1)
   print(byte)  # Output: 66
   print(my_ba)  # Output: bytearray(b'AC')


6. **`clear()`**: Removes all bytes from the bytearray.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67])
   my_ba.clear()
   print(my_ba)  # Output: bytearray(b'')


7. **`count(x)`**: Returns the number of occurrences of a byte.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67, 66])
   count = my_ba.count(66)
   print(count)  # Output: 2


8. **`find(sub[, start[, end]])`**: Returns the lowest index where the subsequence is found.

   .. code-block:: python

   my_ba = bytearray(b'Hello, World!')
   index = my_ba.find(b'World')
   print(index)  # Output: 7


9. **`reverse()`**: Reverses the bytes in place.

   .. code-block:: python

   my_ba = bytearray([65, 66, 67])
   my_ba.reverse()
   print(my_ba)  # Output: bytearray(b'CBA')


10. **`decode(encoding='utf-8', errors='strict')`**: Decodes the bytearray to a string using the specified encoding.

   .. code-block:: python

    my_ba = bytearray(b'Hello, World!')
    string = my_ba.decode('utf-8')
    print(string)  # Output: Hello, World!



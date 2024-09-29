==========================
bytearrays
==========================

| `bytearray` objects in Python come with a variety of methods that allow you to manipulate and interact with the byte data. Here are some of the most commonly used methods:
| These methods provide a lot of flexibility for working with bytearrays, allowing you to manipulate the data in various ways.

### Common Methods for `bytearray`

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



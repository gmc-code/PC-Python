==========================
bytes
==========================

| `bytes` objects in Python are immutable, so they don't have methods that modify the object in place like `bytearray` does.
| However, they do have a variety of methods that allow you to interact with and manipulate the data. Here are some commonly used methods for `bytes`:
| These methods provide a range of functionalities for working with `bytes` objects, allowing you to search, split, join, replace, and decode byte sequences.

### Common Methods for `bytes`

1. **`count(sub[, start[, end]])`**: Returns the number of non-overlapping occurrences of the substring `sub`.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      count = my_bytes.count(b'o')
      print(count)  # Output: 2


2. **`find(sub[, start[, end]])`**: Returns the lowest index where the substring `sub` is found.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      index = my_bytes.find(b'World')
      print(index)  # Output: 7


3. **`index(sub[, start[, end]])`**: Like `find()`, but raises a `ValueError` if the substring is not found.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      index = my_bytes.index(b'World')
      print(index)  # Output: 7


4. **`split(sep=None, maxsplit=-1)`**: Splits the bytes object into a list of byte objects, using `sep` as the delimiter.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      parts = my_bytes.split(b', ')
      print(parts)  # Output: [b'Hello', b'World!']


5. **`join(iterable)`**: Concatenates any number of bytes objects, with the bytes object acting as a separator.

   .. code-block:: python

      parts = [b'Hello', b'World!']
      joined = b', '.join(parts)
      print(joined)  # Output: b'Hello, World!'


6. **`replace(old, new[, count])`**: Returns a copy of the bytes object with all occurrences of the substring `old` replaced by `new`.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      replaced = my_bytes.replace(b'World', b'Python')
      print(replaced)  # Output: b'Hello, Python!'


7. **`strip([chars])`**: Returns a copy of the bytes object with leading and trailing whitespace removed.

   .. code-block:: python

      my_bytes = b"  Hello, World!  "
      stripped = my_bytes.strip()
      print(stripped)  # Output: b'Hello, World!'


8. **`startswith(prefix[, start[, end]])`**: Returns `True` if the bytes object starts with the specified prefix.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      result = my_bytes.startswith(b'Hello')
      print(result)  # Output: True


9. **`endswith(suffix[, start[, end]])`**: Returns `True` if the bytes object ends with the specified suffix.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      result = my_bytes.endswith(b'World!')
      print(result)  # Output: True


10. **`decode(encoding='utf-8', errors='strict')`**: Decodes the bytes object to a string using the specified encoding.

   .. code-block:: python

      my_bytes = b"Hello, World!"
      string = my_bytes.decode('utf-8')
      print(string)  # Output: Hello, World!



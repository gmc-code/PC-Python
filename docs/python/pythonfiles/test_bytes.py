'''
Sure! Here's a summary of some commonly used byte methods in Python:

1. **`decode()`**: Converts bytes to a string using a specified encoding.
2. **`count(sub)`**: Returns the number of times a specified byte or substring appears in the bytes object.
3. **`strip([chars])`**: Removes specified leading and trailing bytes.
4. **`split([sep])`**: Splits the bytes object into a list of substrings based on a specified delimiter.
5. **`startswith(prefix)`**: Checks if the bytes object starts with the specified prefix.
6. **`endswith(suffix)`**: Checks if the bytes object ends with the specified suffix.
7. **`find(sub)`**: Returns the lowest index where the specified byte or substring is found.
8. **`index(sub)`**: Similar to `find()`, but raises a `ValueError` if the byte or substring is not found.
9. **`replace(old, new)`**: Replaces occurrences of a specified byte or substring with another.

These methods are useful for various operations when working with binary data in Python¹².

If you have any specific questions about these methods or need examples, feel free to ask!

Source: Conversation with Copilot, 01/10/2024
(1) Python Bytes: Everything you need to know!. https://embeddedinventor.com/python-bytes-everything-you-need-to-know/.
(2) Python bytes() method - GeeksforGeeks. https://www.geeksforgeeks.org/python-bytes-method/.
(3) Python Byte Arrays: A Comprehensive Guide - OpenGenus IQ. https://iq.opengenus.org/python-byte-arrays/.
(4) Python bytes (). https://www.programiz.com/python-programming/methods/built-in/bytes.
(5) bytes () in Python - Built-In Functions with Examples. https://diveintopython.org/functions/built-in/bytes.


'''
'''
# my_bytes = bytes([num for num in range(256)])
# print(list(my_bytes))
# print(my_bytes)
printable_bytes = bytes([num for num in range(32,127)])
print(printable_bytes)
print(printable_bytes[45])
# b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

my_ba = bytearray([num for num in range(32,127)])
print(my_ba)  # Output: bytearray(b'ABC')
my_ba[0] = 68  # Modify the first byte
print(my_ba)  # Output: bytearray(b'DBC')
print(my_ba[45])
'''
b = b'example'
print(dir(b))
# ['capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
b = b'example'
help(b)

===========================
Bytes & Bytearrays
===========================

| In Python, **bytes** and **bytearrays** are binary data types used to store sequences of raw 8-bit integers (values from ``0`` to ``255``).
| While text strings (``str``) store human-readable characters using Unicode, **bytes** store raw machine-readable binary data such as images, audio files, network packets, or file streams.
| Python provides two primary types: ``bytes`` (immutable / unchangeable) and ``bytearray`` (mutable / changeable).

.. code-block:: python

    # Creating a bytes object using the b prefix
    raw_data = b"Hello"

    print(type(raw_data))  # Output: <class 'bytes'>
    print(raw_data[0])     # Output: 72 (ASCII integer value for 'H')

----

The Bytes Data Type (bytes)
===========================

The ``bytes`` data type represents an **immutable** sequence of integers in the range ``0 <= x < 256``:

- **Literals with b Prefix**: Defined by prefixing quotes with `b`, such as ``b"text"`` (ASCII characters only).
- **Integer Sequence**: Accessing an index returns the integer ASCII code, not a string character.
- **Immutability**: Once created, individual elements of a ``bytes`` object cannot be modified or reassigned.
- **Creation via bytes()**: Can be created using the ``bytes()`` constructor with a list of integers or a specified size.

.. code-block:: python

    data = b"ABC"

    # Reading elements returns integer ASCII values
    print(data[0])  # Output: 65 (ASCII for 'A')
    print(data[1])  # Output: 66 (ASCII for 'B')

    # Creating bytes from a list of integers
    numbers = bytes([72, 101, 108, 108, 111])
    print(numbers)  # Output: b'Hello'

Quiz: The Bytes Data Type
-------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To define a bytes literal in Python, place the prefix @@b@@ before the quote marks.
    2. Bytes objects store sequences of integers ranging from 0 to @@255@@.
    3. The `bytes` data type is @@immutable@@, meaning its contents cannot be altered after creation.
    4. Accessing `b"A"[0]` returns the ASCII integer value @@65@@.
    5. Raw binary data like images and network packets are stored using @@bytes@@ in Python.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a bytes literal and print its type and first byte integer value.

.. ordering::

    sample_bytes = b"Python"
    print(type(sample_bytes))
    print(sample_bytes[0])

----

**Example 2:** Construct a bytes object from a list of ASCII integer codes.

.. ordering::

    code_list = [80, 121, 116, 104, 111, 110]
    byte_data = bytes(code_list)
    print(byte_data)

----

**Example 3:** Initialize a zero-filled bytes object of a given length.

.. ordering::

    buffer_size = 5
    empty_buffer = bytes(buffer_size)
    print(empty_buffer)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How do you write a bytes literal in Python?

        [x] b"Hello" | Correct! Adding the prefix 'b' before quotation marks creates a bytes literal.
        [ ] "Hello"b | Incorrect. The prefix 'b' must go before the opening quote.
        [ ] bytes("Hello") | Incorrect. While a constructor, literal syntax specifically uses the b prefix.
        [ ] [b]Hello[/b] | Incorrect. That is BBCode formatting, not Python syntax.


    .. multichoice::

        What range of integer values can an individual byte represent in Python?

        [x] 0 to 255 | Correct! An 8-bit byte represents 256 distinct integer values from 0 through 255.
        [ ] 0 to 100 | Incorrect. Bytes use 8 bits, allowing up to 255.
        [ ] -128 to 127 | Incorrect. Python bytes store unsigned integers from 0 to 255.
        [ ] 1 to 256 | Incorrect. Byte indexing is zero-based starting at 0 up to 255.


    .. multichoice::

        Given ``data = b"Code"``, what is returned by ``data[0]``?

        [x] 67 | Correct! Indexing returns the integer ASCII code for 'C', which is 67.
        [ ] "C" | Incorrect. Indexing a bytes object returns an integer, not a string character.
        [ ] b"C" | Incorrect. Indexing returns a single integer value, not a bytes slice.
        [ ] 0 | Incorrect. Index 0 returns the byte value at that position.


    .. multichoice::

        What happens if you try to reassign an element in a bytes object (e.g., ``b[0] = 65``)?

        [x] Python raises a TypeError because bytes are immutable | Correct! Bytes objects cannot be modified after creation.
        [ ] The byte updates successfully | Incorrect. Bytes are immutable.
        [ ] Python converts the bytes object into a list | Incorrect. Object type does not change automatically.
        [ ] The element is set to None | Incorrect. An exception is raised.


    .. multichoice::

        What is the output of ``bytes(4)``?

        [x] b'\x00\x00\x00\x00' | Correct! Passing an integer to bytes() creates a sequence of zero-bytes of that length.
        [ ] b'4' | Incorrect. Passing an integer specifies buffer size, not character content.
        [ ] [0, 0, 0, 0] | Incorrect. Result is a bytes object, not a list.
        [ ] TypeError | Incorrect. Passing an integer length is valid.


    .. multichoice::

        Which function checks the number of bytes stored in a ``bytes`` object?

        [x] len() | Correct! The len() function returns the total count of bytes.
        [ ] size() | Incorrect. Python uses len() for sequence lengths.
        [ ] count() | Incorrect. count() searches for specific occurrences inside sequences.
        [ ] bytecount() | Incorrect. No bytecount() function exists in standard Python.


    .. multichoice::

        What does ``bytes([65, 66, 67])`` evaluate to?

        [x] b'ABC' | Correct! Integers 65, 66, and 67 correspond to ASCII characters 'A', 'B', and 'C'.
        [ ] [65, 66, 67] | Incorrect. Converts the list of integers into a bytes object.
        [ ] b'656667' | Incorrect. Integers are mapped to ASCII character equivalents.
        [ ] TypeError | Incorrect. Passing a list of integers in range 0-255 is valid.


    .. multichoice::

        Why are ``bytes`` preferred over ``str`` for handling binary image files?

        [x] Images contain raw non-text binary data that doesn't map cleanly to Unicode strings | Correct! Bytes store exact binary byte representations required for media files.
        [ ] Bytes execute mathematical additions faster | Incorrect. Primary reason is accurate binary representation.
        [ ] Strings cannot store data longer than 100 characters | Incorrect. Strings have no such arbitrary small limit.
        [ ] Bytes automatically compress image file sizes | Incorrect. Bytes store uncompressed raw data.


    .. multichoice::

        What type of error occurs if you pass an integer outside 0-255 to ``bytes([300])``?

        [x] ValueError | Correct! Byte values must strictly remain within the 0 to 255 integer range.
        [ ] TypeError | Incorrect. A ValueError is raised due to out-of-range value.
        [ ] KeyError | Incorrect. KeyErrors are related to dictionary lookups.
        [ ] OverflowError | Incorrect. Python raises ValueError for byte integer range violations.


    .. multichoice::

        What is returned by ``type(b"123")``?

        [x] <class 'bytes'> | Correct! The b prefix creates an instance of the bytes class.
        [ ] <class 'str'> | Incorrect. The b prefix makes it a bytes object, not a string.
        [ ] <class 'int'> | Incorrect. It is a sequence of bytes, not an integer.
        [ ] <class 'bytearray'> | Incorrect. Literal b syntax produces immutable bytes.

----

The Bytearray Data Type (bytearray)
==================================

The ``bytearray`` data type is the **mutable** (changeable) version of ``bytes``:

- **Mutability**: Elements within a ``bytearray`` can be updated, appended, or removed in place.
- **In-place Modification**: Support item assignment like ``data[0] = 90`` or list-like methods such as ``.append()``.
- **Conversion**: Easily created from strings (with encoding), existing ``bytes``, or lists of integers.
- **Performance**: Ideal for building or modifying binary buffers dynamically in memory.

.. code-block:: python

    # Creating a bytearray from a bytes object
    mutable_bytes = bytearray(b"Hello")

    # Modifying the first byte ('H' -> 'J')
    mutable_bytes[0] = 74
    print(mutable_bytes)  # Output: bytearray(b'Jello')

    # Appending a new byte value (ASCII '!')
    mutable_bytes.append(33)
    print(mutable_bytes)  # Output: bytearray(b'Jello!')

Quiz: The Bytearray Data Type
-----------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Unlike `bytes`, the `bytearray` type is @@mutable@@ and can be changed in place.
    2. To add a new byte to the end of a `bytearray`, use the @@.append()@@ method.
    3. Updating an element in a bytearray requires providing an integer between 0 and @@255@@.
    4. You can convert a `bytearray` back into immutable `bytes` using the @@bytes()@@ function.
    5. A `bytearray` is commonly used as a dynamic memory @@buffer@@ when receiving network data.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Convert a bytes object to a bytearray and modify its first element.

.. ordering::

    original = b"cat"
    buffer = bytearray(original)
    buffer[0] = 98
    print(buffer)

----

**Example 2:** Construct an empty bytearray and append byte values.

.. ordering::

    data_stream = bytearray()
    data_stream.append(72)
    data_stream.append(105)
    print(data_stream)

----

**Example 3:** Modify a bytearray and convert it back to immutable bytes.

.. ordering::

    packet = bytearray(b"Ping")
    packet[0] = 80
    final_bytes = bytes(packet)
    print(final_bytes)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What primary advantage does ``bytearray`` offer over ``bytes``?

        [x] It is mutable and can be modified without creating a new object | Correct! Bytearrays allow in-place modification of elements.
        [ ] It can store values larger than 255 | Incorrect. Individual elements are still constrained to 0-255.
        [ ] It automatically translates text into foreign languages | Incorrect. Translation is not a native bytearray feature.
        [ ] It uses less memory for text strings | Incorrect. Mutability is its key functional distinction.


    .. multichoice::

        Given ``ba = bytearray(b"hi")``, what does ``ba.append(33)`` do?

        [x] Adds byte value 33 (ASCII '!') to the end of ba | Correct! .append() adds an integer byte to the end.
        [ ] Raises a TypeError | Incorrect. Appending valid integer byte values is fully supported.
        [ ] Overwrites 'h' with 33 | Incorrect. .append() attaches to the end, not overwrite index 0.
        [ ] Replaces 'i' with '33' | Incorrect. Appends a new byte element.


    .. multichoice::

        What is output by ``ba = bytearray([65, 66]); ba[0] = 90; print(ba)``?

        [x] bytearray(b'ZB') | Correct! Value 90 corresponds to ASCII 'Z', replacing 65 ('A').
        [ ] bytearray(b'AB') | Incorrect. Index 0 was updated to 90 ('Z').
        [ ] bytearray(b'ZA') | Incorrect. Index 0 ('A') was changed, leaving index 1 ('B') unchanged.
        [ ] TypeError | Incorrect. Item assignment is allowed on bytearrays.


    .. multichoice::

        Which method converts a ``bytearray`` instance into an immutable ``bytes`` object?

        [x] bytes(my_bytearray) | Correct! Passing a bytearray to the bytes() constructor creates an immutable copy.
        [ ] my_bytearray.to_bytes() | Incorrect. to_bytes() is an integer method.
        [ ] str(my_bytearray) | Incorrect. str() generates string representation rather than bytes object.
        [ ] my_bytearray.freeze() | Incorrect. No .freeze() method exists.


    .. multichoice::

        What happens if you execute ``ba = bytearray(b"test"); ba[0] = "T"``?

        [x] Python raises a TypeError | Correct! Bytearray elements must be integers (0-255), not string characters.
        [ ] Index 0 changes to 'T' | Incorrect. Assigning string literals raises TypeError.
        [ ] 't' changes to 'T' automatically | Incorrect. Must pass integer ASCII value (84 for 'T').
        [ ] The bytearray clears | Incorrect. TypeError halts execution before modifications occur.


    .. multichoice::

        How do you assign the letter 'A' to index 0 of ``ba = bytearray(b"hello")`` correctly?

        [x] ba[0] = 65 | Correct! 65 is the integer ASCII value for capital 'A'.
        [ ] ba[0] = "A" | Incorrect. Bytearrays require integer values, not string characters.
        [ ] ba[0] = b"A" | Incorrect. Assigning bytes slice to single index is invalid.
        [ ] ba.insert('A') | Incorrect. Insert requires integer value and index position.


    .. multichoice::

        Which statement about ``bytearray`` is FALSE?

        [x] Bytearray objects are immutable | Correct! This statement is false because bytearrays are mutable.
        [ ] Bytearrays store integers from 0 to 255 | Incorrect. This is true.
        [ ] Bytearrays support list-like methods like .append() and .extend() | Incorrect. This is true.
        [ ] Bytearrays can be created from bytes objects | Incorrect. This is true.


    .. multichoice::

        Given ``ba = bytearray(3)``, what are its initial contents?

        [x] Three zero bytes: bytearray(b'\x00\x00\x00') | Correct! Passing integer size initializes zeroed bytes buffer.
        [ ] Three spaces | Incorrect. Initialized with null bytes (\x00).
        [ ] Empty bytearray | Incorrect. Size parameter creates 3 elements.
        [ ] bytearray(b'333') | Incorrect. Size integer creates zero-filled buffer.


    .. multichoice::

        What is the result of ``len(bytearray(b"12345"))``?

        [x] 5 | Correct! Length corresponds to the 5 byte elements stored.
        [ ] 15 | Incorrect. Length counts element items, not total bit values.
        [ ] 0 | Incorrect. Contains 5 bytes.
        [ ] TypeError | Incorrect. len() functions normally on bytearrays.


    .. multichoice::

        Can you clear all elements in a ``bytearray`` using ``ba.clear()``?

        [x] Yes, because bytearray is mutable and supports .clear() | Correct! .clear() empties mutable bytearrays.
        [ ] No, .clear() only works on dictionaries | Incorrect. Lists and bytearrays support .clear().
        [ ] No, bytearrays cannot change size | Incorrect. Bytearrays can grow and shrink dynamically.
        [ ] Yes, but it converts it into a string | Incorrect. Object remains an empty bytearray.

----

Converting Between Strings and Bytes (.encode & .decode)
========================================================

Converting text strings to raw binary bytes and vice versa requires explicit **encoding** and **decoding**:

- **Encoding (.encode())**: Converts a human-readable text string (``str``) into raw binary bytes (``bytes``) using a specified character set (e.g., ``UTF-8``).
- **Decoding (.decode())**: Converts raw binary bytes (``bytes``) back into a text string (``str``).
- **Default Encoding**: Python uses ``UTF-8`` encoding by default if no argument is passed.
- **Type Strictness**: You cannot directly concatenate a ``str`` and a ``bytes`` object without explicitly converting one first.

.. code-block:: python

    text = "Hello, World!"

    # Encode string to bytes
    binary_data = text.encode("utf-8")
    print(binary_data)  # Output: b'Hello, World!'
    print(type(binary_data))  # Output: <class 'bytes'>

    # Decode bytes back to string
    restored_text = binary_data.decode("utf-8")
    print(restored_text)  # Output: Hello, World!
    print(type(restored_text))  # Output: <class 'str'>

Quiz: Converting Between Strings and Bytes
------------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To convert a string (`str`) into `bytes`, use the @@.encode()@@ method.
    2. To convert a `bytes` object back into a string (`str`), use the @@.decode()@@ method.
    3. The default character encoding standard used by Python is @@UTF-8@@.
    4. Attempting `b"Hello" + "World"` results in a @@TypeError@@.
    5. Decoding binary data that contains invalid byte sequences raises a @@UnicodeDecodeError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Encode a string message and transmit/print binary output.

.. ordering::

    message = "Python 3"
    encoded_bytes = message.encode("utf-8")
    print(encoded_bytes)

----

**Example 2:** Decode incoming raw network bytes into readable text.

.. ordering::

    received_data = b"Welcome user"
    decoded_text = received_data.decode("utf-8")
    print(decoded_text)

----

**Example 3:** Encode, modify via bytearray, and decode back to string.

.. ordering::

    original_text = "cat"
    raw_buffer = bytearray(original_text.encode())
    raw_buffer[0] = 98
    print(raw_buffer.decode())

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method converts a ``str`` object into a ``bytes`` object?

        [x] .encode() | Correct! .encode() transforms text strings into binary byte representations.
        [ ] .decode() | Incorrect. .decode() transforms bytes into text strings.
        [ ] .to_bytes() | Incorrect. .to_bytes() is used on integers.
        [ ] .convert() | Incorrect. No .convert() string method exists in standard Python.


    .. multichoice::

        Which method converts a ``bytes`` object back into a human-readable ``str``?

        [x] .decode() | Correct! .decode() converts raw binary bytes into string text.
        [ ] .encode() | Incorrect. .encode() goes from string to bytes.
        [ ] .str() | Incorrect. Uses method call syntax .decode().
        [ ] .parse() | Incorrect. Python uses .decode().


    .. multichoice::

        What is the default encoding used when calling ``"hello".encode()`` in Python 3?

        [x] UTF-8 | Correct! UTF-8 is the default standard encoding in Python 3.
        [ ] ASCII | Incorrect. UTF-8 is default, though ASCII is a subset.
        [ ] UTF-16 | Incorrect. UTF-8 is the built-in default parameter.
        [ ] ISO-8859-1 | Incorrect. UTF-8 is standard.


    .. multichoice::

        What happens if you attempt to execute ``b"Hello " + "World"``?

        [x] Python raises a TypeError | Correct! Cannot concatenate bytes and str objects directly.
        [ ] Output is b"Hello World" | Incorrect. Type implicit conversion does not occur automatically.
        [ ] Output is "Hello World" | Incorrect. Raises TypeError.
        [ ] Output is b"Hello "World"" | Incorrect. Raises TypeError.


    .. multichoice::

        Given ``s = "Python"``, what is the data type of ``s.encode()``?

        [x] bytes | Correct! Encoding a string outputs a bytes object.
        [ ] str | Incorrect. Encoding converts from str to bytes.
        [ ] bytearray | Incorrect. .encode() returns immutable bytes by default.
        [ ] int | Incorrect. Returns bytes sequence.


    .. multichoice::

        What error is raised when trying to decode corrupted byte sequences with ``.decode("utf-8")``?

        [x] UnicodeDecodeError | Correct! Invalid UTF-8 byte sequences trigger a UnicodeDecodeError.
        [ ] ValueError | Incorrect. Specific UnicodeDecodeError subclass is raised.
        [ ] TypeError | Incorrect. Decoding wrong sequence types raises UnicodeDecodeError.
        [ ] KeyError | Incorrect. KeyErrors occur with dictionaries.


    .. multichoice::

        What is the output of ``b"Python".decode()``?

        [x] "Python" | Correct! Decoding raw bytes b"Python" yields string literal "Python".
        [ ] b"Python" | Incorrect. .decode() strips the bytes classification and yields str.
        [ ] ['P', 'y', 't', 'h', 'o', 'n'] | Incorrect. Returns string object, not list.
        [ ] 6 | Incorrect. Returns decoded string.


    .. multichoice::

        How can you fix the expression ``b"Data: " + "123"`` to avoid a ``TypeError``?

        [x] b"Data: " + "123".encode() | Correct! Encoding "123" converts it to bytes, allowing binary concatenation.
        [ ] str(b"Data: ") + "123" | Incorrect. String conversion of bytes creates "b'Data: '123".
        [ ] b"Data: ".decode() + 123 | Incorrect. Cannot concatenate str and int.
        [ ] b"Data: " .add("123") | Incorrect. Unsupported method call.


    .. multichoice::

        What parameter can be passed to ``.decode(errors="ignore")``?

        [x] It instructs Python to skip invalid un-decodable bytes without crashing | Correct! errors="ignore" suppresses decoding errors.
        [ ] It converts all characters to uppercase | Incorrect. Handled by .upper().
        [ ] It forces conversion into integers | Incorrect. Parameter controls error handling.
        [ ] It deletes all spaces | Incorrect. Controls Unicode decoding error handling.


    .. multichoice::

        Is ``"A".encode("utf-8")`` equal to ``b"A"`` in Python?

        [x] Yes | Correct! ASCII letter 'A' encoded in UTF-8 yields exact byte literal b"A".
        [ ] No | Incorrect. Statements evaluate as equal.
        [ ] Only when running on Linux | Incorrect. Cross-platform behavioral consistency.
        [ ] Raises a SyntaxError | Incorrect. Expression is valid syntax.


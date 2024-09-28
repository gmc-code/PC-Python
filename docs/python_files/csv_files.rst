==========================
csv files
==========================

| See: https://docs.python.org/3/library/csv.html
| Corey Schafer video See: https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=15
| Socratica video See: https://www.youtube.com/watch?v=Xi52tx6phRU&list=RDCMUCW6TXMZ5Pq6yL6_k5NZ2e0Q&index=1

| csv files are comma separated files. 
| Data is separated or delimited within the same line by a comma.
| csv files are not restricted to using commas as delimiters. Other delimiters are also used, such as tabs.

| csv files are useful as tables of values with headers for each column.

----

Header rows
------------------

| csv files may have a header row that names each column.
| In the csv snippet below, the first row a header row.

.. code-block::

    Month,Abbr,Numeric
    January,Jan,1
    ...

----

Opening files: newline=''
---------------------------

| If ``newline=''`` is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \\r\\n line endings on write an extra \\r will be added. 
| It should always be safe to specify ``newline=''``, since the csv module does its own (universal) newline handling.

----

csv.reader
-------------

| Use the ``csv.reader`` function to read a csv file.

Syntax:

.. py:function:: csv.reader(f, dialect='excel', **fmtparams)

    :param f: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Return a reader object which is an iterable that behaves like a generator allowing iteration over lines in the given f.
    | Each row read from the csv file is returned as a list of strings. 
    | No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified
    | (in which case unquoted fields are transformed into floats).
    | For fmtparams see: https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters'

----

Reading files
--------------------

| Download the csv file :download:`months.csv <files/months.csv>`

| The code below opens a csv file and uses a for loop to iterate over each row of the csv_reader object.
| Each row is a list of the comma separated values.
| newline='' is recommended to avoid incorrect line endings.

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

.. code-block::

    ['Month,Abbr,Numeric']
    ['January,Jan,1']
    ['February,Feb,2']
    ...
    ['December,Dec,12']

----

Reading files with non comma delimiter
----------------------------------------------

| Download the csv file :download:`months_tabbed.csv <files/months_tabbed.csv>`

.. code-block::

    Month	Abbr	Numeric
    January	Jan	1
    February	Feb	2
    ...
    December	Dec	12


| The code below opens a csv file and uses a for loop to iterate over each row of the csv_reader object.
| Each row is a list of the **tab** separated values from the file.
| ``csv_reader = csv.reader(csv_file, delimiter="\t")`` uses the delimiter argument since the csv file used is tab delimited.
| newline='' is recommended to avoid incorrect line endings.

.. code-block:: python
    
    import csv

    csv_path = 'files/months_tabbed.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            print(row)

.. code-block::

    ['Month,Abbr,Numeric']
    ['January,Jan,1']
    ['February,Feb,2']
    ...
    ['December,Dec,12']

----

next function
-------------

| The next() function returns the next item in an iterator.

| Syntax:

.. py:function:: next(iterable, default)

    :param iterable:  An iterable object.
    :param default:  Optional. An default value to return if the iterable has reached its end.

    | The next() function returns the next item in an iterator.

| In the code below, next is used to return the first row in a csv reader object in order to skip it.

----

Using an index with the row lists
-----------------------------------

| The code below just prints the part of each row that has an index of 1.
| Use ``next(csv_reader)`` to skip the first row which has the headings: "Month,Abbr,Numeric".

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(row[1], end=", ")

.. code-block::

    Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, 


----

Padded strings
------------------

| The code below spaces out the csv data as in a manual table format.

.. code-block::

    |  Month         |  Abbr          |  Numeric       |
    |  January       |  Jan           |  1             |
    |  February      |  Feb           |  2             |
    ...
    |  December      |  Dec           |  12            |


| The list comprehension, ``padded_row = [str(i).ljust(14) for i in row]``, builds a list which pads the strings with spaces on the right to reach 14 characters in length.
| The print statement uses the string join method to concatenate the padded list elements with pipes before and after each line.

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            padded_row = [str(i).ljust(14) for i in row]
            print("|  " + '|  '.join(padded_row) + "|")

----

Reading a csv file to a list
----------------------------------

| The code below reads in the months csv file and appends each row to the list: data_list.

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    data_list = []
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data_list.append(row)
    print(data_list)

| The printed data_list is below, showing each row of the csv file as a sublist in the list: data_list.

.. code-block:: 

    [
        ["Month", "Abbr", "Numeric"],
        ["January", "Jan", "1"],
        ["February", "Feb", "2"],
        ["March", "Mar", "3"],
        ["April", "Apr", "4"],
        ["May", "May", "5"],
        ["June", "Jun", "6"],
        ["July", "Jul", "7"],
        ["August", "Aug", "8"],
        ["September", "Sep", "9"],
        ["October", "Oct", "10"],
        ["November", "Nov", "11"],
        ["December", "Dec", "12"],
    ]


----

csv writer
------------------

| Use the ``csv.writer`` function to write to a csv file.

Syntax:

.. py:function:: csv.writer(f, dialect='excel', **fmtparams)

    :param f: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Return a writer object responsible for converting the user's data into delimited strings on the given file-like object. 
    | Non-string data are stringified with str() before being written.
    | For **fmtparams** see: https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters


-----

Converting comma delimited to tab delimited files.
-------------------------------------------------------

| The code below converts a comma delimited csv file to tab delimited.
| ``delimiter="\t"`` is one of the optional fmtparams arguments that allows the delimiter to be set.

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    csv_path2 = 'files/months_tabbed.csv'

    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader)
        with open(csv_path2, 'w', newline='') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter="\t")
            for row in csv_reader:
                csv_writer.writerow(row)


| Before: 

.. code-block::

    Month,Abbr,Numeric
    January,Jan,1
    February,Feb,2
    ...
    December,Dec,12

| After:

.. code-block::

    Month	Abbr	Numeric
    January	Jan	1
    February	Feb	2
    ...
    December	Dec	12


-----

Saving a list of sublists to a csv file
-----------------------------------------------

| The code below saves a list to a csv file.
| The list represents data collected by the accelerometer on a microbit.
| The list is made up of sublists of 4 integers: a time value, x acceleration, y acceleration, z acceleration.

.. code-block:: python
    
    import csv

    data_list = [
        [87574, 208, 876, -12],
        [87677, 388, 900, 1992],
        [87780, -236, 540, -2040],
        [87884, 208, 1888, -1136],
        [87989, 560, 1284, 280],
        [88092, 1660, 1772, -1040],
    ]
    myheaders = ["time", "x", "y", "z"]
    filename = "files/microbit_data.csv"
    with open(filename, "w", newline="") as myfile:
        writer = csv.writer(myfile)
        writer.writerow(myheaders)
        writer.writerows(data_list)


----

DictReader
-----------------

| DictReader is preferred over the regular csv.reader
| See: https://docs.python.org/3/library/csv.html#csv.DictReader

Syntax:

.. py:class:: csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)


    :param f: a string for the file path to the csv file from the current directory.
    :param fieldnames:  a sequence of keys that identify the order in which values in the dictionary passed to the writerow() method are written to file **f**.
    :param restval: specify the value to be written if the dictionary is missing a key in **fieldnames**. 
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param *args, **kwds: other optional or keyword arguments are passed to the underlying writer instance.

    | Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
    | The fieldnames parameter is a sequence. 
    | If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames.
    | The dictionary preserves their original ordering.
    | If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by **restkey** (which defaults to None). 
    | If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of **restval** (which defaults to None).


----

DictReading files
--------------------

| Download the csv file :download:`months.csv <files/months.csv>`

| The code below uses DictReader, and so, produces a dictionary for each row.
| The first row, "Month,Abbr,Numeric", is used for the dictionary keys, so is not printed below.

.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

.. code-block::

    {'Month': 'January', 'Abbr': 'Jan', 'Numeric': '1'}
    {'Month': 'February', 'Abbr': 'Feb', 'Numeric': '2'}
    ...
    {"Month": "December", "Abbr": "Dec", "Numeric": "12"}

----

Using a key with the row dictionaries
--------------------------------------

| The code below just prints the part of each row that has a key of "Abbr".


.. code-block:: python
    
    import csv

    csv_path = 'files/months.csv'
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader
        (csv_file)
        
        for row in csv_reader:
            print(row["Abbr"], end=", ")

.. code-block::

    Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, 


----

DictWriter
-----------------

| DictWriter is required after using DictReader.
| See: https://docs.python.org/3/library/csv.html#csv.DictWriter

Syntax:

.. py:class:: csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

    :param f: a string for the file path to the csv file from the current directory.
    :param fieldnames:  a sequence of keys that identify the order in which values in the dictionary passed to the writerow() method are written to file **f**.
    :param restval: specify the value to be written if the dictionary is missing a key in **fieldnames**. 
    :param extrasaction: indicates what action to take if the dictionary passed to the writerow() method contains a key not found in fieldnames. If it is set to 'raise', the default value, a ValueError is raised. If it is set to 'ignore', extra values in the dictionary are ignored. 
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param *args, **kwds: other optional or keyword arguments are passed to the underlying writer instance.

    | Create an object which operates like a regular writer but maps dictionaries onto output rows. 

----

DictWriter.writeheader
--------------------------

| DictWriter.writeheader is used to write the dictionary keys to the first line of the new csv file.
| See: https://docs.python.org/3/library/csv.html#csv.DictWriter.writeheader

Syntax:

.. py:class:: DictWriter.writeheader()
    
    | Write a row with the field names (as specified in the constructor) to the writer's file object.
    | Return the return value of the csvwriter.writerow() call used internally.

----

DictWriter with fieldnames
--------------------------------------

| Download the csv file :download:`letter_frequency.csv <files/letter_frequency.csv>`

| The code below uses DictReader to write to a new csv file.
| Fieldnames need to be given to covert the dictionary rows to output for the writer.

.. code-block:: python
    
    import csv

    csv_path = 'files/letter_frequency.csv'
    csv_path2 = 'files/letter_frequency_tabbed.csv'

    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(csv_path2, 'w', newline='') as new_file:
            fieldnames = ['letter', 'frequency']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()
            for line in csv_reader:
                csv_writer.writerow(line)

.. code-block:: 

    letter	frequency
    A	0.08167
    B	0.01492
    ...
    Z	0.00074

----

DictWriter with selected fieldnames
--------------------------------------

| Download the csv file :download:`afl_premiers_2000s.csv <files/afl_premiers_2000s.csv>`

| The code below uses DictReader to write to a new csv file.
| Field names need to be given to covert the dictionary rows to output for the writer.

| The field names in the downloaded file are: "Index,Year,Premiership team,Runner-up"
| The code below uses dictionary comprehension, ``fieldnames_dict = {key: line[key] for key in fieldnames}``, on each row, to produce a new dictionary for writing to the new csv file.


.. code-block:: python
    
    import csv

    csv_path = 'files/afl_premiers_2000s.csv'
    csv_path2 = 'files/afl_premiers_2000s_tabbed.csv'

    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(csv_path2, 'w', newline='') as new_file:
            fieldnames = ["Year","Premiership team"]
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()
            for line in csv_reader:
                fieldnames_dict = {key: line[key] for key in fieldnames}
                csv_writer.writerow(fieldnames_dict)

.. code-block:: 

    Year	Premiership team
    2024	Brisbane Lions
    2023	Collingwood
    2022	Geelong Cats
    2021	Melbourne
    ...
    2000	Essendon


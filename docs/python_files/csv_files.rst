==========================
csv files
==========================

| See: https://docs.python.org/3/library/csv.html
| See video guide at: https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=15

| Census data can be exported as csv from: https://explore.data.abs.gov.au/ and https://data.gov.au/

| csv files are comma separated files. 
| Data is separated or delimited within the same line by a comma.
| Other delimiters are also used, such as tabs.

----

Opening files: newline=''
---------------------------

| If ``newline=''`` is not specified, newlines embedded inside quoted fields will not be interpreted correctly, 
| and on platforms that use \r\n linendings on write an extra \r will be added. 
| It should always be safe to specify ``newline=''``, since the csv module does its own (universal) newline handling.

----

csv.reader
-------------

| Use the ``csv.reader`` function to read a csv file.

Syntax:

.. py:function:: csv.reader(csvfile, dialect='excel', **fmtparams)

    :param csvfile: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Return a reader object which will iterate over lines in the given csvfile.
    | Each row read from the csv file is returned as a list of strings. 
    | No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified
    | (in which case unquoted fields are transformed into floats).
    | For fmtparams see: https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters'

----

Reading files
--------------------

| Download the test csv file :download:`months.csv <files/months.csv>`

| The code below opens a csv file and uses a for loop to iterate over each row of the csv_reader object.
| Each row is a list of the comma separated values.
| newline='' is recommended to avoid incorrect line endings.

.. code-block:: python
    
    import csv

    with open('files/months.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

.. code-block::

    ['Month,Abbrev,Numeric']
    ['January,Jan,1']
    ...

----

Reading files with non comma delimiter
----------------------------------------------

| Download the test csv file :download:`months_tabbed.csv <files/months_tabbed.csv>`

| The code below opens a csv file and uses a for loop to iterate over each row of the csv_reader object.
| Each row is a list of the **tab** separated values from the file.
| ``csv_reader = csv.reader(csv_file, delimiter="\t")`` uses the delimiter argument since the csv file used is tab delimited.
| newline='' is recommended to avoid incorrect line endings.

.. code-block:: python
    
    import csv

    with open('files/months_tabbed.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            print(row)

.. code-block::

    ['Month,Abbrev,Numeric']
    ['January,Jan,1']
    ...

----

Using an index with the row lists
-----------------------------------

| The code below just prints the part of each row that has an index of 1.
| Use ``next(csv_reader)`` to skip the first row which has the headings: "Month,Abbrev,Numeric".

.. code-block:: python
    
    import csv

    with open('files/months.csv', 'r', newline='') as csv_file:
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

    |  Month         |  Abbrev        |  Numeric       |
    |  January       |  Jan           |  1             |
    |  Feburary      |  Feb           |  2             |
    ...

| The list comprehension, ``padded_row = [str(i).ljust(14) for i in row]``, builds a list which pads the strings with spaces on the right to reach 14 characters in length.
| The print statement uses the string join method to concatenate the padded list elements with pipes before and after each line.

.. code-block:: python
    
    import csv

    with open('files/months.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            padded_row = [str(i).ljust(14) for i in row]
            print("|  " + '|  '.join(padded_row) + "|")

----

csv writer
------------------

| Use the ``csv.writer`` function to write to a csv file.

Syntax:

.. py:function:: csv.writer(csvfile, dialect='excel', **fmtparams)

    :param csvfile: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Return a writer object responsible for converting the user's data into delimited strings on the given file-like object. 
    | Non-string data are stringified with str() before being written.
    | For **fmtparams** see: https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters


| The code below converts a comma delimited csv file to tab delimited.
| ``delimiter="\t"`` is one of the optional fmtparams arguments that allows the delimiter to be set.

.. code-block:: python
    
    import csv

    with open('files/months.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader)

        with open('files/months_tabbed.csv', 'w', newline='') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter="\t")
            for row in csv_reader:
                csv_writer.writerow(row)

----

DictReader
-----------------

| DictReader is preferred over the regular csv.reader
| See: https://docs.python.org/3/library/csv.html#csv.DictReader

Syntax:

.. py:class:: csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

    :param csvfile: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
    | The fieldnames parameter is a sequence. 
    | If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames. 
    | The dictionary preserves their original ordering.
    | If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by **restkey** (which defaults to None). 
    | If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of **restval** (which defaults to None).


----

DictReading files
--------------------

| Download the test csv file :download:`months.csv <files/months.csv>`

| The code below uses DictReader, and so, produces a dictionary for each row.
| The first row is used for the dictionary keys, so is not printed below.

.. code-block:: python
    
    import csv

    with open('files/months.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

.. code-block::

    {'Month': 'January', 'Abbrev': 'Jan', 'Numeric': '1'}
    {'Month': 'Feburary', 'Abbrev': 'Feb', 'Numeric': '2'}
    {'Month': 'March', 'Abbrev': 'Mar', 'Numeric': '3'}

    ...


















----

.. code-block:: python
    
    import csv

    with open('files/letter_frequency.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('files/letter_frequency_tab.csv', 'w') as new_file:
            fieldnames = ['letter', 'frequency']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)


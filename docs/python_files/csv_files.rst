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

csv.reader
-------------

| Use the ``csv.reader`` function to read a csv file.

Syntax:

.. py:function:: csv.reader(csvfile, dialect='excel', newline='', **fmtparams)

    :param csvfile: a string for the file path to the csv file from the current directory.
    :param dialect: Use a set of parameters specific to a particular CSV dialect; Defaults to excel; one of ['excel', 'excel-tab', 'unix']
    :param newline: newline='' is recommended to avoid incorrect line endings.
    :param fmtparams: optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect.

    | Return a reader object which will iterate over lines in the given csvfile.
    | Each row read from the csv file is returned as a list of strings. 
    | No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified
    | (in which case unquoted fields are transformed into floats).
    | For fmtparams see: https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters'

----

Reading files
--------------------

| Download the test csv file :download:`month.csv <files/month.csv>`

| The code below opens a csv file and uses a for loop to iterate over each row of the csv_reader object.
| Each row is a list of the comma separated values.

.. code-block:: python
    
    import csv

    with open('files/month.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

.. code-block::

    ['Month,Abbrev,Numeric']
    ['January,Jan,1']
    ...


| The code below just prints the part of each row that has an index of 1.
| Use ``next(csv_reader)`` to skip the first row which has the headings: "Month,Abbrev,Numeric".

.. code-block:: python
    
    import csv

    with open('files/month.csv', 'r') as csv_file:
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

    with open('files/month.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            padded_row = [str(i).ljust(14) for i in row]
            print("|  " + '|  '.join(padded_row) + "|")

----

csv writer
------------------

| The code below spaces out the csv data as in a manual table format.

.. code-block:: python
    
    import csv

    with open('files/month.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader)

        with open('files/months_tabbed.csv', 'w',newline='') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter="\t")
            for row in csv_reader:
                csv_writer.writerow(row)



















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


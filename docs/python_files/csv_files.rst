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


----

Padded strings
------------------

| The code below spaces out the csv data as in a manual table format.

.. code-block::

    |  Month         |  Abbrev        |  Numeric       |
    |  January       |  Jan           |  1             |
    |  Feburary      |  Feb           |  2             |
    ...

| The line: ``padded_row = [str(i).ljust(14) for i in row]`` pads the strings with spaces on the right to reach 14 characters in length.
| The print statement uses the join method to concatenate the padded list elements with pipes before and after each line.

.. code-block:: python
    
    import csv

    with open('files/month.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            padded_row = [str(i).ljust(14) for i in row]
            print("|  " + '|  '.join(padded_row) + "|")






















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


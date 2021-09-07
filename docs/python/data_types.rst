==========================
Data Types
==========================

Common data types:
Data Type,Example,Description
Integers,``4`` or ``0`` or ``-5``,Positive and negative whole numbers
Floats,``3.14``,Numbers with a decimal point 
Strings,"``""Hello World""`` or ``'2.5'``",Characters enclosed by single or double quotation marks
Booleans,``True`` or ``False``,Values representing true and false values

.. csv-table:: Data_Types
    :file: Date_types.csv
    :widths: 30, 30, 90
    :header-rows: 1

Python has the following data types built-in by default, in these categories:
 
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

Datatypes:

A string is a sequence of characters surrounded by either single quotation marks (' '), or double quotation marks (" "). 
'text'
Text with quotes within it can use done using the other quote mark.
"it's"
'Jim said "Go home", then left.'

Text with both quotes within it can use done using triple quotes.
'''My favourite quote from Jim's essay was "Go home". Short and sharp.'''

Escaping via \ can be used to force the quote to be used literally rather than as the end of the string.
'it\'s'

Numbers are written without quotes.
An integer is a whole number.
2
A float is a decimal.
3.5

Booleans have the value True or False

The type() function can be used to get the data type for a variable.

String
print(type('hello'))
# <class 'str'>

Integer
print(type(1))
# <class 'int'>

Float
print(type(1.64))
# <class 'float'>

Boolean
print(type(True))
# <class 'bool'>

Data types can’t be mixed. They need to be converted so that they can be used together. The conversion of one type to another is called type casting.

An integer can be converted to a string using the str() function.
The premierships integer is converted to a string so it can be combined with the rest of the strings for printing.

team = 'Richmond'
premierships = 11
print(team + ' has won ' + str(premierships) + ' premierships.')

To specify the data type, use the following constructor functions:

int() converts a string consisting of an integer to an integer number
c = int("3")      # c will be 3

float() converts a string consisting of a decimal to a decimal number
g = float("4.23") # g will be 4.23

str() converts a number to a string with a number in it
g = float("4.23") # g will be 4.23


a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
# c1 = int("3.4")   # error
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'
print([a,b,c,d,e,f,g,h,i,j])

# [1, 2, 3, 1.0, 2.5, 3.0, 4.23, '80s', '22', '3.01']    
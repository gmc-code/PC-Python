==========================
Unpacking iterables
==========================


Unpacking to merge tuples
------------------------------

| Tuple unpacking below can be used to merge tuples.

.. code-block:: python
 
    tuple1 = ("a", "b", "c")
    tuple2 = (3, 2, 1)
    merged_tuple = (*tuple1, *tuple2)
    print(merged_tuple)

| The ouput is: ('a', 'b', 'c', 3, 2, 1)

----

Unpacking to merge lists
------------------------------

| List unpacking below can be used to merge lists.

.. code-block:: python
 
    list1 = ["a", "b", "c"]
    list2 = [3, 2, 1]
    merged_list = [*list1, *list2]
    print(merged_list)

| The ouput is: ['a', 'b', 'c', 3, 2, 1]




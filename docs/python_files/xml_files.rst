==========================
xml files
==========================

| XML stands for eXtensible Markup Language.
| XML is a markup language.
| XML was designed to store and transport data in a software- and hardware-independent way.


| docs, See: https://docs.python.org/3/library/xml.html
| docs, See: https://docs.python.org/3/library/xml.etree.elementtree.html
| W3schools, See: https://www.w3schools.com/xml/default.asp

| See: https://www.youtube.com/watch?v=73isvEt3wCU
| See: https://www.youtube.com/watch?v=5SlemSWGD1g
| See: https://www.youtube.com/watch?v=j0xr0-IAqyk

.. admonition:: Warning

    | The XML modules are not secure against erroneous or maliciously constructed data. 
    | If you need to parse untrusted or unauthenticated data use the defusedxml Package.
    | defusedxml is a pure Python package that prevents any potentially malicious operation. 

----

xml structure
-----------------------

| XML stores data in a structured way; the author must define both the tags and the document structure.
| XML is a tree of elements.
| In XML, an element is a pair of tags; a start tag and an end tag, usually with text between them. e.g. <name>Joe</name>
| Elements can contain attributes within the start tag as key value pairs. e.g <name id="1">Joe</name>
| Elements can contain text between the tags and other elements. e.g <name id="1">Joe<nickname>Joey</nickname></name>
| The examples used will not include attributes (in order to simplify the coding).

| An example of xml for employees is below.
| ``<employees>`` is the root tag.
| ``<office_worker>`` is a child tag of the root tag.
| ``<firstName>`` is a child tag of the office_worker tag.

.. code-block:: 

    <?xml version="1.0" encoding="UTF-8" ?>
    <employees>
        <office_worker>
            <firstName>John</firstName>
            <lastName>Doe</lastName>
            <gender>Male</gender>
        </office_worker>
        <office_worker>
            <firstName>Peter</firstName>
            <lastName>Jones</lastName>
            <gender>Male</gender>
        </office_worker>
        <writer>
            <firstName>Anna</firstName>
            <lastName>Smith</lastName>
            <gender>Female</gender>
        </writer>
    </employees>

----

Parse xml file
--------------------------------

| Import a part of the xml library using: ``import xml.etree.ElementTree as ET``

| Use ``ET.parse`` to parse an XML source into an element tree.

.. py:function:: ET.parse(source, parser=None)
 
    :param source: a filename or file object containing XML data. 
    :param parser: an optional parser instance. If not given, the standard XMLParser parser is used. 
    
    |  Returns an ElementTree instance.

----

| Use ``getroot()`` to get the root of the element tree object.

.. py:function:: ET.getroot()

    | Returns the root element for the tree, ET.

----

.. py:function:: ET.findall(match, namespaces=None)

    :param match: may be a tag name or a path
    :param namespaces: is an optional mapping from namespace prefix to full name. Pass '' as prefix to move all unprefixed tag names in the expression into the given namespace.

    | Finds all matching subelements, by tag name or path, starting at the root of the tree.
    | Returns a list containing all matching elements in document order.

----

| The code below opens the xml file, ``tree = ET.parse(xml_file_path)`` and parses it into the variable ``tree``.
| ``found_elememnts = tree.findall("office_worker")`` is used to get a list containing the office_worker data as a list of element objects.
| ``for elem in found_elememnts:`` iterates over each office_worker list of elements so the text of each element can be obtained.
| e.g.  ``elem.find("firstName").text``


.. code-block::  python

    import xml.etree.ElementTree as ET

    xml_file_path = "files/employees.xml"
    tree = ET.parse(xml_file_path)


    employee_type = "office_worker"
    found_elememnts = tree.findall(employee_type)
    for elem in found_elememnts:
        f_name = elem.find("firstName").text
        l_name = elem.find("lastName").text
        gen = elem.find("gender").text
        print(f'{f_name} {l_name} is a {gen.lower()} {employee_type}')

    employee_type = "writer"
    found_elememnts = tree.findall(employee_type)
    for elem in found_elememnts:
        f_name = elem.find("firstName").text
        l_name = elem.find("lastName").text
        gen = elem.find("gender").text
        print(f'{f_name} {l_name} is a {gen.lower()} {employee_type}')


| The print output is below:

.. code-block:: 

    John Doe is a male office_worker
    Peter Jones is a male office_worker
    Anna Smith is a female writer

----

.. admonition:: Tasks

    #. Avoid code duplication above by using a list of employee types and iterating over them.
    

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Avoid code duplication above by using a list of employee types and iterating over them.

                .. code-block:: python

                    import xml.etree.ElementTree as ET

                    xml_file_path = "files/employees.xml"
                    tree = ET.parse(xml_file_path)


                    employee_types = ["office_worker", "writer"]
                    for employee_type in employee_types:
                        found_elememnts = tree.findall(employee_type)
                        for elem in found_elememnts:
                            f_name = elem.find("firstName").text
                            l_name = elem.find("lastName").text
                            gen = elem.find("gender").text
                            print(f'{f_name} {l_name} is a {gen.lower()} {employee_type}')



----

Edit tag text
--------------------------------

| Elements can be referred to by numeric indices from the root or from the parent.
| e.g. The text "Peter", the firstName of the second employee (who is at at index 1 of the root), is at ``root[1][0].text``.

.. code-block:: 

    <?xml version="1.0" encoding="UTF-8" ?>
    <employees>
        ...
        <office_worker>
            <firstName>Peter</firstName>
            ...
        </office_worker>
    </employees>

| The code below changes "Peter" to "Pete" and saves the change to the file employees2.xml

.. code-block::  python

    import xml.etree.ElementTree as ET

    xml_file_path = "files/employees.xml"
    xml_file_path2 = "files/employees2.xml"
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    root[2][0].text = "Pete"
    tree.write(xml_file_path2)

----

Fixing indenting
---------------------

.. py:function:: ET.indent(tree, space='  ', level=0)

    :param tree: can be an Element or ElementTree. 
    :param space: space is the whitespace string that will be inserted for each indentation level, two space characters by default
    :param level: For indenting partial subtrees inside of an already indented tree, pass the initial indentation level as level.

    | Appends whitespace to the subtree to indent the tree visually. This can be used to generate pretty-printed XML output.


----

New Elements
---------------------

.. py:function:: ET.Element(tag, attrib={}, **extra)

    :param tag: tag is the element name
    :param attrib: attrib is an optional dictionary, containing element attributes.
    :param extra:  extra contains additional attributes, given as keyword arguments.

    | Appends whitespace to the subtree to indent the tree visually. This can be used to generate pretty-printed XML output.
    | Just use: ``ET.Element(tag)``.

----

Append element
--------------------------------

| Elements can be appended to the root.
| e.g. root.append(emp4_xml)
| ``employer4 = ET.Element("writer")`` creates an element for the new employee.
| ``child = ET.Element("firstName")`` creates an element for the firstName.
| ``child.text = "Jane"`` adds the text value to firstName element. 
| ``employer4.append(child)`` appends the  firstName element to the employer4 element.
| The other child elements are then built and appended to the employer4 element befor eit is finally appended to the root. 

.. code-block::  python

    import xml.etree.ElementTree as ET

    xml_file_path = "files/employees.xml"
    xml_file_path2 = "files/employees2.xml"
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    employer4 = ET.Element("writer")

    child = ET.Element("firstName")
    child.text = "Jane"
    employer4.append(child)

    child = ET.Element("lastName")
    child.text = "Austin"
    employer4.append(child)

    child = ET.Element("gender")
    child.text = "Female"
    employer4.append(child)

    root.append(employer4)
    ET.indent(tree, space='    ', level=0)
    tree.write(xml_file_path2)

| The code above appends the xml below:

.. code-block:: 

    <writer>
        <firstName>Jane</firstName>
        <lastName>Austin</lastName>
        <gender>Female</gender>
    </writer>

----

.. admonition:: Tasks

    #. Write a definition to append the employee data from a python dictionary to the xml and use it to add the employee dictionary: {"firstName":"Jane","lastName":"Austin","gender":"Female"}

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a definition to append the employee data from a python dictionary to the xml and use it to add the employee dictionary: {"firstName":"Jane","lastName":"Austin","gender":"Female"} using a tag of "writer"

                .. code-block:: python

                    import xml.etree.ElementTree as ET

                    xml_file_path = "files/employees.xml"
                    xml_file_path2 = "files/employees2.xml"
                    tree = ET.parse(xml_file_path)
                    root = tree.getroot()

                    def append_dict_to_xml(tag, d):
                        # create new element
                        elem = ET.Element(tag)
                        for key, val in d.items():
                            # create child element
                            child = ET.Element(key)
                            child.text = val
                            elem.append(child)
                        return elem

                    emp4_dict = {"firstName":"Jane","lastName":"Austin","gender":"Female"}
                    tag = "writer"
                    emp4_xml = append_dict_to_xml(tag, emp4_dict)
                    root.append(emp4_xml)

                    ET.indent(tree, space='    ', level=0)
                    tree.write(xml_file_path2)


    .. code-block:: 

        <employees>
            <office_worker>
                <firstName>John</firstName>
                <lastName>Doe</lastName>
                <gender>Male</gender>
            </office_worker>
            <office_worker>
                <firstName>Peter</firstName>
                <lastName>Jones</lastName>
                <gender>Male</gender>
            </office_worker>
            <writer>
                <firstName>Anna</firstName>
                <lastName>Smith</lastName>
                <gender>Female</gender>
            </writer>
            <writer>
                <firstName>Jane</firstName>
                <lastName>Austin</lastName>
                <gender>Female</gender>
            </writer>
        </employees>

    
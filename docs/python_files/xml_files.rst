==========================
xml files
==========================

| XML stands for eXtensible Markup Language.
| XML is a markup language.
| XML was designed to store and transport data in a software- and hardware-independent way.
| XML stores data in plain text format.
| With XML, the author must define both the tags and the document structure.

| XML is a tree of elements.
| In XML, an element is a pair of tags; a start tag and an end tag, usually with text between them. e.g. <name>Joe</name>
| Elements can contain attributes within the start tag as key value pairs. e.g <name id="1">Joe</name>
| Elements can contain text between the tags and other elements. e.g <name id="1">Joe<nickname>Joey</nickname></name>

| docs, See: https://docs.python.org/3/library/xml.html
| docs, See: https://docs.python.org/3/library/xml.etree.elementtree.html
| W3schools, See: https://www.w3schools.com/xml/default.asp

.. admonition:: Warning

    | The XML modules are not secure against erroneous or maliciously constructed data. 
    | If you need to parse untrusted or unauthenticated data see the defusedxml Package.
    | defusedxml is a pure Python package with modified subclasses of all stdlib XML parsers that prevent any potentially malicious operation. 
    | Use of this package is recommended for any server code that parses untrusted XML data.

----

Parse xml file
--------------------------------

| Use ``xml.etree.ElementTree.parse`` to parse an XML source into an element tree.
| Syntax:

.. py:function:: xml.etree.ElementTree.parse(source, parser=None)
 
    :param source: a filename or file object containing XML data. 
    :param parser: an optional parser instance. If not given, the standard XMLParser parser is used. 
    
    |  Returns an ElementTree instance.



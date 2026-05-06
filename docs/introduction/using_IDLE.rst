========================================
Using IDLE
========================================

Guide to Using the Python IDLE
--------------------------------------

IDLE (Integrated Development and Learning Environment) is Python's built-in
tool for writing and testing code. It is designed to be simple and lightweight.

The Interactive Shell
---------------------
When you first launch IDLE, you enter the **Shell**. This environment allows
for immediate code execution.

* **The Prompt**: The ``>>>`` symbol means Python is waiting for your input.
* **Execution**: Type a line of code (e.g., ``print("Hello")``) and press **Enter**
    to see the result immediately.
* **History**: Use ``Alt + P`` to retrieve previous commands and ``Alt + N``
    to move to the next command in your history.

The Editor (Writing Scripts)
----------------------------
The Shell is great for testing, but it does not save your work. To write
reusable programs, use the **Editor**.

1. **Open Editor**: Go to ``File > New File``.
2. **Write Code**: Enter your Python logic in this window.
3. **Save**: Go to ``File > Save`` (ensure the file ends in ``.py``).
4. **Run**: Press ``F5`` or select ``Run > Run Module``. The output will
    appear in the Shell window.

Key Features
------------

Syntax Highlighting
~~~~~~~~~~~~~~~~~~~
IDLE automatically color-codes your text:
* **Keywords**: Orange (e.g., ``if``, ``def``, ``import``)
* **Strings**: Green (e.g., ``"Hello World"``)
* **Functions**: Blue (e.g., ``print``)

Indentation
~~~~~~~~~~~
Python relies on indentation. IDLE will automatically indent your code
after you type a colon (``:``).
* To indent a block: Highlight and press ``Tab``.
* To dedent a block: Highlight and press ``Shift + Tab``.

Auto-Completion
~~~~~~~~~~~~~~~
If you forget the exact name of a method, type the start of the word
and press ``Tab`` to see a list of suggestions.

Common Shortcuts
----------------

+-------------------+----------------------------+
| Action            | Shortcut                   |
+===================+============================+
| Run Module        | F5                         |
+-------------------+----------------------------+
| New File          | Ctrl + N (Cmd + N on Mac)  |
+-------------------+----------------------------+
| Save File         | Ctrl + S (Cmd + S on Mac)  |
+-------------------+----------------------------+
| Interrupt Program | Ctrl + C                   |
+-------------------+----------------------------+

Using the Debugger
------------------
To find errors in your logic:
1. In the Shell window, click **Debug > Debugger**.
2. Run your script using **F5**.
3. Use the **Step** button to watch Python execute your code one line at a time.

.. note::
    IDLE is perfect for beginners, but as your projects grow, you may eventually
    want to explore larger IDEs like VS Code or PyCharm.


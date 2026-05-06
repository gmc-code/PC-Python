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

1. **Open Editor**: Go to ``File > New File``. ``Ctrl + N``.
2. **Write Code**: Enter your Python logic in this window.
3. **Save**: Go to ``File > Save`` (ensure the file ends in ``.py``). ``Ctrl + S``.
4. **Run**: Press ``F5`` or select ``Run > Run Module``.
    The output will appear in the Shell window.

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

+-------------------+----------------+
| Action            | Shortcut       |
+===================+================+
| Run Module        | F5             |
+-------------------+----------------+
| New File          | Ctrl + N       |
+-------------------+----------------+
| Save File         | Ctrl + S       |
+-------------------+----------------+
| Interrupt Program | Ctrl + C       |
+-------------------+----------------+

Using the Debugger
------------------
To find errors in your logic:
1. In the Shell window, click **Debug > Debugger**.
2. Run your script using **F5**.
3. Use the **Step** button to watch Python execute your code one line at a time.

.. note::
    IDLE is perfect for beginners, but as your projects grow, you may eventually
    want to explore larger IDEs like VS Code.


Configuring Options in Python IDLE
==========================================

IDLE allows you to customize the interface to make your coding environment
more comfortable. All major settings are found under the configuration menu.

Accessing the Settings
----------------------
To open the configuration window:

* **Windows**: Go to ``Options > Configure IDLE``.

Setting Font Face and Size
--------------------------
Under the **Fonts/Tabs** tab, you can adjust how your code appears:

* **Font Face**: Choose a "Monospaced" font (like Courier, Consolas, or
    Menlo). These ensure that every character is the same width, which is
    essential for keeping Python indentation aligned.
* **Font Size**: Use the slider or the dropdown menu to increase the
    point size. This is particularly helpful for high-resolution screens.
* **Bold**: You can toggle the **Bold** checkbox if you prefer thicker
    text for better visibility.

Key Configuration Options
-------------------------

Indentation Width
~~~~~~~~~~~~~~~~~
Also found in the **Fonts/Tabs** tab, the "Python Standard" is 4 spaces.
You can change this value, but it is highly recommended to keep it at 4
to remain compatible with most Python style guides (PEP 8).

Color Themes
~~~~~~~~~~~~
In the **Highlights** tab, you can change the color scheme:

* **Built-in Themes**: You can switch between "IDLE Classic", "IDLE New",
    and "IDLE Dark".
* **Custom Themes**: You can click on specific elements (like "Strings"
    or "Comments") and choose custom colors to build your own dark mode
    or high-contrast theme.

Startup Preferences
~~~~~~~~~~~~~~~~~~~
In the **General** tab, look for the "At Startup" section:

* **Open Edit Window**: Set IDLE to open a blank script file immediately
    instead of the Interactive Shell.
* **Open Shell Window**: The default setting; opens the interactive
    prompt first.

Key Bindings (Shortcuts)
-----------------------
Under the **Keys** tab, you can see a list of every shortcut IDLE uses.
If you are used to shortcuts from other editors, you can
select a different "Built-in Key Set" or create your own custom
mappings for actions like "Save" or "Find".

Saving Your Changes
-------------------
1. Click **Apply** to see the changes immediately without closing the
    window.
2. Click **OK** to save your settings and return to coding.

.. tip::
    If you use a high-DPI monitor and the icons or text still look tiny
    after changing the font size, you may need to adjust your OS-level
    scaling settings, as IDLE is a bit older and sometimes struggles
    with modern 4K displays.


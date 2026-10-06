===========================
Python Functions
===========================

| In programming, a **function** is a reusable block of code designed to perform a specific task.
| Instead of writing the same code multiple times throughout a program, you can write it once inside a function and execute it whenever needed.
| Using functions helps make your code organized, easier to read, and simpler to debug.

.. code-block:: python

    # Defining a simple function
    def greet():
        print("Hello, welcome to Python!")

    # Calling (executing) the function
    greet()

----

Defining and Calling Functions
==============================

To create and use a function in Python, you follow two main steps:

- **Defining a Function**: Use the ``def`` keyword, followed by the function name, parentheses ``()``, and a colon ``:``.
- **Function Body**: The block of code inside the function must be indented (usually 4 spaces).
- **Calling a Function**: To run the function's code, write its name followed by parentheses ``()``.
- **Code Execution**: Defining a function does not execute its code immediately; it only runs when the function is explicitly called.

.. code-block:: python

    # Function definition
    def show_menu():
        print("--- Main Menu ---")
        print("1. Start Game")
        print("2. Exit")

    # Function call
    show_menu()

Quiz: Defining and Calling Functions
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Python functions are defined using the @@def@@ keyword.
    2. To execute a function, you write its name followed by @@parentheses@@.
    3. The code statements belonging inside a function body must be @@indented@@.
    4. Defining a function creates the code, but it will not run until the function is @@called@@.
    5. A function name must be followed by parentheses and a @@colon@@ at the end of the header line.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define and call a basic function that prints a greeting.

.. ordering::

    def say_hello():
        print("Hello, World!")

    say_hello()

----

**Example 2:** Define a function that displays a cheer, then call it twice.

.. ordering::

    def cheer():
        print("Go Team!")

    cheer()
    cheer()

----

**Example 3:** Define a function that prints a line separator and call it.

.. ordering::

    def draw_line():
        print("--------------------")

    draw_line()

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which keyword is used to define a function in Python?

        [x] def | Correct! The def keyword tells Python you are defining a new custom function.
        [ ] function | Incorrect. function is used in other languages like JavaScript, but not Python.
        [ ] create | Incorrect. create is not a valid Python keyword for functions.
        [ ] define | Incorrect. Python uses the abbreviated keyword def.


    .. multichoice::

        What happens when you define a function without calling it?

        [x] Python stores the function in memory, but does not execute its code | Correct! Function bodies only run when explicitly called.
        [ ] The code inside the function runs immediately | Incorrect. Defining only registers the function for later use.
        [ ] Python raises a SyntaxError | Incorrect. Defining a function without calling it is completely valid.
        [ ] The function is automatically deleted | Incorrect. The function stays in memory ready to be called.


    .. multichoice::

        How do you correctly call a function named ``display_score``?

        [x] display_score() | Correct! Calling a function requires its name followed by parentheses.
        [ ] call display_score | Incorrect. Python does not use the keyword call.
        [ ] def display_score() | Incorrect. Including def defines a function rather than calling it.
        [ ] display_score | Incorrect. Missing parentheses references the function object without executing it.


    .. multichoice::

        What must be placed at the end of a function definition header line (e.g. ``def my_func()``)?

        [x] A colon (:) | Correct! Block headers in Python must end with a colon.
        [ ] A semicolon (;) | Incorrect. Python does not require semicolons at line endings.
        [ ] A period (.) | Incorrect. Periods are used for attribute access, not block headers.
        [ ] An equals sign (=) | Incorrect. Equals signs are used for variable assignment.


    .. multichoice::

        Why are functions useful in computer programming?

        [x] They allow code reuse, reduce repetition, and make programs organized | Correct! Functions modularize code for clarity and maintainability.
        [ ] They make programs run 10 times faster | Incorrect. Functions organize code structure rather than increasing raw hardware speed.
        [ ] They convert variable data types automatically | Incorrect. Casting functions perform type conversions.
        [ ] They prevent users from making input errors | Incorrect. Input validation logic handles user input checks.


    .. multichoice::

        How many times can a defined function be called in a program?

        [x] As many times as needed | Correct! Functions can be invoked repeatedly across a script.
        [ ] Exactly once | Incorrect. Functions are designed to be reused multiple times.
        [ ] Maximum of 10 times | Incorrect. There is no arbitrary low limit on function calls.
        [ ] Only inside loops | Incorrect. Functions can be called from anywhere in your code.


    .. multichoice::

        What error occurs if you attempt to call a function before defining it?

        [x] NameError | Correct! Python executes sequentially, so calling an undefined function raises a NameError.
        [ ] TypeError | Incorrect. TypeErrors occur with mismatched data types.
        [ ] IndentationError | Incorrect. IndentationErrors relate to improper code alignment.
        [ ] ValueError | Incorrect. ValueErrors occur when functions receive invalid argument values.


    .. multichoice::

        How does Python identify which statements belong inside a function body?

        [x] Indentation (standard 4 spaces) | Correct! Python uses indentation levels to group code blocks.
        [ ] Curly braces {} | Incorrect. Languages like C++ and Java use curly braces, but Python uses indentation.
        [ ] END keywords | Incorrect. Languages like Ruby use end statements; Python relies on indentation.
        [ ] Square brackets [] | Incorrect. Square brackets define list literals and indexing.


    .. multichoice::

        Which of the following is a valid function name in Python?

        [x] calculate_total | Correct! Function names follow variable naming rules (lowercase with underscores).
        [ ] 2nd_function | Incorrect. Function names cannot start with a digit.
        [ ] print-message | Incorrect. Hyphens are interpreted as subtraction operators.
        [ ] def | Incorrect. Reserved keywords cannot be used as function names.


    .. multichoice::

        Given ``def test(): print("A"); print("B")``, what happens when ``test()`` is called?

        [x] Both "A" and "B" are printed | Correct! Calling a function executes all statements inside its body sequentially.
        [ ] Only "A" is printed | Incorrect. All statements in the function body execute.
        [ ] Only "B" is printed | Incorrect. Execution starts at the top of the function body.
        [ ] Nothing is printed | Incorrect. Calling the function triggers execution.

----

Function Parameters and Arguments
=================================

Functions can accept input values to perform dynamic operations:

- **Parameters**: Variables listed inside the parentheses of a function's definition header.
- **Arguments**: The actual values passed into the function when it is called.
- **Multiple Inputs**: Functions can take multiple parameters separated by commas.
- **Positional Matching**: Arguments are assigned to parameters based on their order in the function call.

.. code-block:: python

    # Function with one parameter
    def greet_user(name):
        print("Hello, " + name + "!")

    greet_user("Alex")  # Argument "Alex" passed to parameter name

    # Function with multiple parameters
    def add_numbers(a, b):
        print("Sum:", a + b)

    add_numbers(5, 10)  # Output: Sum: 15

Quiz: Parameters and Arguments
------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Variables defined in a function header to receive input values are called @@parameters@@.
    2. The actual values passed to a function during a call are known as @@arguments@@.
    3. Multiple parameters in a function definition must be separated by @@commas@@.
    4. Arguments are matched to parameters based on their @@positional@@ order.
    5. If a function expects two parameters, you must provide @@2@@ arguments when calling it.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a function that accepts a person's name and prints a personalized welcome.

.. ordering::

    def welcome(person_name):
        print("Welcome,", person_name)

    welcome("Sam")

----

**Example 2:** Define a function that calculates and displays the area of a rectangle.

.. ordering::

    def calculate_area(width, height):
        area = width * height
        print("Area:", area)

    calculate_area(4, 5)

----

**Example 3:** Define a function that repeats a word a specified number of times.

.. ordering::

    def repeat_word(word, count):
        for i in range(count):
            print(word)

    repeat_word("Python", 3)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the difference between a parameter and an argument?

        [x] A parameter is the variable in the function definition; an argument is the actual value passed in the call | Correct! Parameters hold incoming argument data inside the function context.
        [ ] An argument is in the definition; a parameter is in the call | Incorrect. Roles are reversed.
        [ ] They are completely identical terms with no structural difference | Incorrect. Parameters define placeholders; arguments supply runtime values.
        [ ] Parameters are numbers while arguments are strings | Incorrect. Both can be any valid data type.


    .. multichoice::

        What happens if you call a function requiring 2 parameters with only 1 argument (e.g. ``def add(x, y):`` called with ``add(5)``)?

        [x] Python raises a TypeError regarding missing arguments | Correct! Argument counts must match expected parameter counts.
        [ ] The missing parameter defaults to 0 | Incorrect. Unless default values are specified, missing arguments trigger errors.
        [ ] The missing parameter becomes None | Incorrect. Python requires explicit arguments for non-default parameters.
        [ ] The function runs normally | Incorrect. Parameter mismatch prevents execution.


    .. multichoice::

        Given ``def multiply(a, b): print(a * b)``, what is output by ``multiply(3, 4)``?

        [x] 12 | Correct! Parameter a receives 3, b receives 4; $3 \times 4 = 12$.
        [ ] 7 | Incorrect. Multiplication occurs, not addition.
        [ ] 34 | Incorrect. Numeric multiplication evaluates math results rather than string concatenation.
        [ ] None | Incorrect. The calculation prints 12.


    .. multichoice::

        What value is assigned to ``city`` in ``def trip(city, days):`` when called as ``trip("Paris", 5)``?

        [x] "Paris" | Correct! First positional argument "Paris" maps to first parameter city.
        [ ] 5 | Incorrect. 5 is the second argument, mapping to days.
        [ ] ("Paris", 5) | Incorrect. Arguments map individually to positional parameters.
        [ ] None | Incorrect. "Paris" is assigned to city.


    .. multichoice::

        How are multiple parameters separated in a function header definition?

        [x] Commas (,) | Correct! Commas separate multiple parameters.
        [ ] Colons (:) | Incorrect. Colons mark header endings.
        [ ] Semicolons (;) | Incorrect. Semicolons are not used for parameter separation.
        [ ] Plus signs (+) | Incorrect. Plus signs denote mathematical addition or concatenation.


    .. multichoice::

        What will ``def show(x): print(x * 2)`` output when called with ``show("A")``?

        [x] AA | Correct! Multiplying string "A" by integer 2 duplicates the string.
        [ ] A2 | Incorrect. String multiplication repeats string characters rather than appending numbers.
        [ ] TypeError | Incorrect. String multiplication by integers is syntactically valid in Python.
        [ ] 2 | Incorrect. String content "A" is repeated.


    .. multichoice::

        Given ``def print_full_name(first, last): print(first + " " + last)``, what outputs for ``print_full_name("Jane", "Doe")``?

        [x] Jane Doe | Correct! "Jane" maps to first, "Doe" maps to last; concatenation outputs "Jane Doe".
        [ ] Doe Jane | Incorrect. Positional arguments preserve order: "Jane" first, then "Doe".
        [ ] JaneDoe | Incorrect. The space string " " creates separation.
        [ ] TypeError | Incorrect. Valid string concatenation.


    .. multichoice::

        Can a function be defined with ZERO parameters?

        [x] Yes, functions can take no parameters if they do not need external data | Correct! Functions like def menu(): require no inputs.
        [ ] No, every function must have at least one parameter | Incorrect. Parameters are optional depending on function design.
        [ ] Yes, but only if it contains a loop | Incorrect. Parameter requirements are independent of control statements inside.
        [ ] No, Python requires at least two parameters | Incorrect. Functions accept any number of parameters, including zero.


    .. multichoice::

        What parameter values are received in ``def check(a, b):`` when calling ``check(10, 20)``?

        [x] a = 10, b = 20 | Correct! Arguments pass positionally from left to right.
        [ ] a = 20, b = 10 | Incorrect. Order of parameters is preserved.
        [ ] a = 30, b = 0 | Incorrect. Values map directly to variables.
        [ ] a = 10, b = 10 | Incorrect. Second argument 20 maps to b.


    .. multichoice::

        Given ``def square(n): print(n ** 2)``, what call produces an output of ``25``?

        [x] square(5) | Correct! $5^2 = 25$.
        [ ] square(25) | Incorrect. $25^2 = 625$.
        [ ] square(10) | Incorrect. $10^2 = 100$.
        [ ] square(2) | Incorrect. $2^2 = 4$.

----

Return Values
=============

Functions can compute results and send values back to the main program using the ``return`` statement:

- **The return Keyword**: Ends function execution immediately and hands a specified value back to the caller.
- **Capturing Return Values**: The returned value can be stored in a variable or printed directly.
- **Print vs. Return**: ``print()`` displays output on the console, whereas ``return`` passes data back for further computation.
- **Early Exit**: Code inside a function after a ``return`` statement will **never execute**.

.. code-block:: python

    # Function with return value
    def double_value(num):
        return num * 2

    # Capturing returned value in a variable
    result = double_value(7)
    print("Result:", result)  # Output: Result: 14

    # Using return value directly in calculations
    total = double_value(5) + 10  # (5 * 2) + 10 = 20
    print("Total:", total)

Quiz: Return Values
-------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@return@@ statement sends a calculated result back to where the function was called.
    2. A function exits @@immediately@@ when a return statement is executed.
    3. While `print()` displays text on the screen, `return` hands data back to the @@caller@@.
    4. If a Python function reaches its end without a return statement, it returns @@None@@.
    5. Code placed directly below a return statement inside the same block is @@unreachable@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a function that returns the cube of a number and store its result.

.. ordering::

    def cube(x):
        return x ** 3

    ans = cube(3)
    print(ans)

----

**Example 2:** Define a function that checks if a number is even and returns `True` or `False`.

.. ordering::

    def is_even(number):
        return number % 2 == 0

    check = is_even(4)
    print(check)

----

**Example 3:** Define a function that returns the maximum of two numbers.

.. ordering::

    def get_max(a, b):
        if a > b:
            return a
        return b

    highest = get_max(12, 8)
    print(highest)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the primary difference between ``print()`` and ``return`` inside a function?

        [x] print() displays text to the console, while return passes data back for use in the program | Correct! print showing text differs from return supplying reusable program values.
        [ ] print() exits the function, while return keeps it running | Incorrect. return exits functions; print does not.
        [ ] return can only send back strings, while print handles numbers | Incorrect. return handles any Python data type.
        [ ] They are identical in function execution | Incorrect. Displaying output is distinct from returning data values.


    .. multichoice::

        What happens to code placed inside a function directly AFTER a ``return`` statement?

        [x] It is skipped and never executes | Correct! Executing return terminates function execution instantly.
        [ ] It executes normally | Incorrect. Execution stops immediately upon hitting return.
        [ ] It causes a SyntaxError | Incorrect. Unreachable code is valid syntax, though useless.
        [ ] It runs before the return statement | Incorrect. Execution flows sequentially until hitting return.


    .. multichoice::

        Given ``def add(x, y): return x + y``, what is stored in ``val`` after ``val = add(10, 20)``?

        [x] 30 | Correct! add(10, 20) evaluates to $10 + 20 = 30$, which is returned and stored in val.
        [ ] None | Incorrect. Function explicitly returns x + y.
        [ ] "1020" | Incorrect. Integer addition adds numeric values.
        [ ] 10 | Incorrect. Sum result 30 is returned.


    .. multichoice::

        What is the return value of a Python function that has NO ``return`` statement?

        [x] None | Correct! Functions without return statements implicitly return the special value None.
        [ ] 0 | Incorrect. None is returned rather than integer zero.
        [ ] False | Incorrect. None is returned rather than Boolean False.
        [ ] Error | Incorrect. Executing functions without return statements is completely valid.


    .. multichoice::

        Given ``def Mystery(): return 5; return 10``, what value is returned when called?

        [x] 5 | Correct! Function terminates on the first return statement, returning 5.
        [ ] 10 | Incorrect. Second return statement is unreachable.
        [ ] 15 | Incorrect. Values are not added together.
        [ ] None | Incorrect. First return statement returns integer 5.


    .. multichoice::

        How can you use the result of a function with a return value in a mathematical calculation?

        [x] Assign it to a variable or use the function call directly inside an expression | Correct! Function calls with returns evaluate to their returned values in place.
        [ ] You must print it first | Incorrect. Printing displays output rather than returning values.
        [ ] Return values cannot be used in calculations | Incorrect. Returned data functions as normal values.
        [ ] Wrap the call in input() | Incorrect. input() captures keyboard input from users.


    .. multichoice::

        What does ``def convert(celsius): return (celsius * 9/5) + 32`` compute?

        [x] Converts Celsius temperature to Fahrenheit and returns the value | Correct! Evaluates conversion formula and hands back calculation.
        [ ] Converts Fahrenheit temperature to Celsius | Incorrect. Formula represents Celsius to Fahrenheit.
        [ ] Prints temperature in Celsius | Incorrect. Function returns calculated data rather than printing.
        [ ] Raises TypeError | Incorrect. Mathematical calculation is valid.


    .. multichoice::

        Given ``def calc(n): print(n * 2)``, what is stored in ``result`` after ``result = calc(5)``?

        [x] None | Correct! calc prints 10 but lacks a return statement, so result stores None.
        [ ] 10 | Incorrect. 10 is printed, but not returned.
        [ ] 5 | Incorrect. 5 was passed as parameter n.
        [ ] Error | Incorrect. Valid Python code; assignment receives None.


    .. multichoice::

        Can a function return a Boolean value (``True`` or ``False``)?

        [x] Yes, functions can return any valid Python data type including Booleans | Correct! Functions return integers, floats, strings, booleans, lists, etc.
        [ ] No, functions only return numbers | Incorrect. Data types are unrestricted.
        [ ] No, functions only return strings | Incorrect. Functions return any data type.
        [ ] Yes, but only inside while loops | Incorrect. Return data types are independent of internal loops.


    .. multichoice::

        What is output by ``def check(): return "Pass"; print("Done"); print(check())``?

        [x] Pass | Correct! check() returns "Pass" (skipping print("Done")), which is then printed by the outer call.
        [ ] Done Pass | Incorrect. print("Done") is unreachable code after return.
        [ ] Pass Done | Incorrect. Function exits before reaching print("Done").
        [ ] None | Incorrect. Explicit return value is "Pass".

----

Variable Scope (Local vs. Global)
=================================

**Scope** determines where variables can be accessed or modified within a Python program:

- **Local Variables**: Defined **inside** a function. They exist only while the function is running and cannot be accessed outside it.
- **Global Variables**: Defined **outside** all functions in the main body of the script. They can be read from anywhere in the file.
- **Scope Isolation**: Local variables protect functions from accidentally modifying variables in other parts of your code.

.. code-block:: python

    global_var = "I am global"  # Global scope

    def my_function():
        local_var = "I am local"  # Local scope
        print(local_var)          # Accessible here
        print(global_var)         # Accessible here

    my_function()

    # print(local_var)  # NameError! local_var does not exist outside the function!

Quiz: Variable Scope
--------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. A variable defined inside a function has @@local@@ scope.
    2. A variable defined outside all functions in a file has @@global@@ scope.
    3. Local variables cannot be accessed @@outside@@ the function where they were created.
    4. Attempting to print an uncreated or out-of-scope local variable raises a @@NameError@@.
    5. Local variable scope isolates functions to prevent unintentional variable @@name@@ conflicts.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Demonstrate local variable scope inside a function.

.. ordering::

    def create_message():
        msg = "Inside local scope"
        print(msg)

    create_message()

----

**Example 2:** Access a global variable from inside a function block.

.. ordering::

    app_name = "MathQuiz"

    def display_app():
        print("Welcome to", app_name)

    display_app()

----

**Example 3:** Show local variable isolation with same variable name as global variable.

.. ordering::

    x = 100

    def override():
        x = 5
        print("Local x:", x)

    override()
    print("Global x:", x)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Where can a local variable defined inside a function be accessed?

        [x] Only inside that specific function body | Correct! Local scope restricts variable existence to the enclosing function.
        [ ] Anywhere in the script | Incorrect. Global variables are accessible anywhere, not local ones.
        [ ] Only inside imported modules | Incorrect. Scope remains bound to function definition.
        [ ] Inside any function defined in the file | Incorrect. Local scope is restricted to the declaring function.


    .. multichoice::

        What happens if you try to print a local variable outside its function?

        [x] Python raises a NameError | Correct! The variable name is undefined in global scope.
        [ ] Python prints None | Incorrect. The variable does not exist in outer scope.
        [ ] Python prints 0 | Incorrect. Out-of-scope variables raise errors.
        [ ] The script pauses execution | Incorrect. Execution crashes with a NameError.


    .. multichoice::

        Given ``score = 100`` defined at the top of a script outside functions, what scope does ``score`` have?

        [x] Global scope | Correct! Variables defined at module root level hold global scope.
        [ ] Local scope | Incorrect. Local variables are defined inside function bodies.
        [ ] Universal scope | Incorrect. "Universal scope" is not standard Python terminology.
        [ ] Block scope | Incorrect. Python manages local and global scopes for functions.


    .. multichoice::

        What output is produced by ``x = 10; def run(): x = 20; run(); print(x)``?

        [x] 10 | Correct! x = 20 inside run() creates a local variable x, leaving global x as 10.
        [ ] 20 | Incorrect. Modifying local x does not alter global x.
        [ ] 30 | Incorrect. Values are kept in isolated scopes.
        [ ] NameError | Incorrect. Global x exists and holds 10.


    .. multichoice::

        Why is local scope useful when building large programming projects?

        [x] It prevents function variables from accidentally overwriting variables elsewhere in the code | Correct! Scope isolation protects variable state.
        [ ] It makes functions run faster | Incorrect. Scope management relates to variable visibility rather than performance speed.
        [ ] It automatically deletes unused files | Incorrect. Scope manages memory references for active execution.
        [ ] It converts local variables into constants | Incorrect. Local variables remain mutable within their scope.


    .. multichoice::

        Can a function read the value of a global variable without special keywords?

        [x] Yes, global variables can be read inside functions | Correct! Functions can read global variable values directly.
        [ ] No, global variables are completely invisible inside functions | Incorrect. Global values can be read within functions.
        [ ] Yes, but only if the variable is an integer | Incorrect. Any global data type can be read.
        [ ] No, attempting to read global variables causes SyntaxError | Incorrect. Reading globals is syntactically valid.


    .. multichoice::

        Given ``def set_val(): a = 50; set_val(); print(a)``, what occurs when running this code?

        [x] NameError: name 'a' is not defined | Correct! Variable a is local to set_val() and cannot be printed globally.
        [ ] Outputs 50 | Incorrect. Variable a is inaccessible outside set_val().
        [ ] Outputs None | Incorrect. Variable a does not exist in global scope.
        [ ] Outputs 0 | Incorrect. Undefined global variables trigger NameError.


    .. multichoice::

        What is variable shadowing in Python?

        [x] Creating a local variable with the same name as a global variable, hiding the global variable within the function | Correct! Local variables shadow global variables of identical name.
        [ ] Deleting a global variable inside a function | Incorrect. Shadowing hides global names locally rather than deleting them.
        [ ] Copying a variable across two separate scripts | Incorrect. Shadowing occurs within local function boundaries.
        [ ] Renaming functions dynamically | Incorrect. Shadowing refers to variable name collisions across scopes.


    .. multichoice::

        When is a local variable created and destroyed?

        [x] Created when the function is called, destroyed when the function finishes | Correct! Local variable lifetimes match function call execution.
        [ ] Created when script starts, destroyed when script ends | Incorrect. That describes global variable lifetimes.
        [ ] Created during compilation, never destroyed | Incorrect. Memory is cleaned up after function execution ends.
        [ ] Created when defined, destroyed immediately before return | Incorrect. Exists throughout function execution.


    .. multichoice::

        What output is produced by ``val = "A"; def test(): print(val); test()``?

        [x] A | Correct! test() reads global variable val and prints "A".
        [ ] NameError | Incorrect. Global val is accessible for reading inside test().
        [ ] None | Incorrect. val holds string "A".
        [ ] SyntaxError | Incorrect. Valid global variable access.


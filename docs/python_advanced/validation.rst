==========================
Validation
==========================

| The examples below are for existence, type and range validation.

----

----

Age validation
--------------------------------

| The code gets user input for an age.
| Then it tests for existence by first removing whitespace characters at the start and the end of the input string.
| Then is does a type check for integers.
| Then it does a range checl to make sure the integer is between 0 and 120 inclusive.

Syntax:

.. py:function:: string.strip([chars])

    | chars (optional): A string specifying the set of characters to remove from both the beginning and the end of the original string.
    | If chars is not provided, it returns the string with spaces, tabs, newlines, etc. removed from the ends.

Syntax:

.. py:function:: string.isdigit()

    | Returns True if all characters are digits.
    | Returns False if the string is empty or contains non-digit characters (including signs, spaces, or decimal points).



.. code-block:: python

    age_input = input("Enter your age: ").strip()

    if age_input == "":
        print("Error: Age is required.")
    elif not age_input.isdigit():
        print("Error: Age must be a number.")
    else:
        age = int(age_input)
        if 0 <= age <= 120:
            print(f"Age accepted: {age}")
        else:
            print("Error: Age must be between 0 and 120.")

----

Type Hints
-------------

| Type hints (or annotations) in Python tell you — and tools like IDEs or linters — what types of arguments a function expects and what it returns.
| This improves readability, debugging, and helps prevent bugs.

Syntax:

.. py:function:: def function_name(arg1: Type1, arg2: Type2) -> ReturnType:

| Part            | Meaning                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `def`           | Declares a function in Python.                                                                                                     |
| `function_name` | The name you give to your function.                                                                                                |
| `arg1: Type1`   | `arg1` is the **name of the first parameter**, and `Type1` is the **expected type** of that parameter (e.g. `int`, `str`, `list`). |
| `arg2: Type2`   | `arg2` is the second parameter, expected to be of type `Type2`.                                                                    |
| `-> ReturnType` | Tells you (and the interpreter/tools) that the function **returns** a value of type `ReturnType` (e.g. `str`, `bool`, `None`).     |
| `:`             | Marks the start of the function body.                                                                                              |


.. code-block:: python

    # with typing for clarity
    # --Optional[int]: This means the function might return an int or None (if validation fails).

    from typing import Optional

    def get_valid_age(age_input: str) -> Optional[int]:
        """Validates age input: existence, type, range."""
        age_input = age_input.strip()

        # Existence check
        if not age_input:
            print("Error: Age is required.")
            return None

        # Type check
        if not age_input.isdigit():
            print("Error: Age must be a number.")
            return None

        age = int(age_input)

        # Range check
        if not (0 <= age <= 120):
            print("Error: Age must be between 0 and 120.")
            return None

        return age

    # Example usage
    user_input: str = input("Enter your age: ")
    validated_age: Optional[int] = get_valid_age(user_input)

    if validated_age is not None:
        print(f"Validated age: {validated_age}")

----

Data classes
-----------------

| A dataclass in Python is a decorator (@dataclass) that automatically generates boilerplate code for classes that primarily store data — like __init__.

Instead of writing this:

.. code-block:: python

    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

You can write this:

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class User:
        name: str
        age: int


.. code-block:: python

    from dataclasses import dataclass


    # Define the User dataclass
    @dataclass
    class User:
        name: str
        age: int


    # Function to validate and create a user from input
    def create_user(name_input: str, age_input: str) -> User:
        name = name_input.strip()
        if not name:
            raise ValueError("Name is required.")

        if not age_input.strip().isdigit():
            raise ValueError("Age must be a number.")

        age = int(age_input)
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120.")

        return User(name=name, age=age)


    # Function to create a default user (for testing/demo)
    def create_default_user() -> User:
        return User(name="Alice", age=25)


    # Main program
    if __name__ == "__main__":
        try:
            user = create_user(input("Enter name: "), input("Enter age: "))
            print(f"Created user from input: {user}")
        except ValueError as e:
            print("Validation error:", e)

        # Also create and print a default user
        default_user = create_default_user()
        print(f"Default user: {default_user}")


----

Extended dataclass
---------------------

The dataclass above can be extended using optional and default values.

.. code-block:: python

    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class User:
        name: str
        age: int
        email: Optional[str] = None
        is_active: bool = True

        def greet(self) -> str:
            """Return a greeting message."""
            status = "active" if self.is_active else "inactive"
            greeting = f"Hello, {self.name}! You are {self.age} years old and currently {status}."
            if self.email:
                greeting += f" We will contact you at {self.email}."
            else:
                greeting += f" We don't have your email address."
            return greeting


    # All fields provided
    user1 = User(name="Alice", age=30, email="alice@example.com", is_active=False)

    # Optional fields omitted
    user2 = User(name="Bob", age=22)

    print(user1.greet())
    # Output: Hello, Alice! You are 30 years old and currently active. We will contact you at alice@example.com.

    print(user2.greet())
    # Output: Hello, Bob! You are 22 years old and currently active. We don't have your email address.

----

Pydantic
--------------

| Pydantic is the most widely used data validation library for Python.
| Pydantic is useful where user data comes from an external source like a JSON file.
| This will highlight why Pydantic model-level validation is valuable, especially when you can't trust the input.

.. code-block:: python


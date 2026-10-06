===========================
Python Classes & Objects
===========================

| In Python, **Object-Oriented Programming (OOP)** allows developers to structure code by creating reusable templates called **classes**.
| A **class** acts like a blueprint or mold, while an **object** is an individual instance created from that blueprint.
| Classes combine data (**attributes**) and actions (**methods**) into a single organized structure.

.. code-block:: python

    # Defining a simple Class blueprint
    class Dog:
        def __init__(self, name, age):
            self.name = name  # Attribute
            self.age = age    # Attribute

        def bark(self):       # Method
            print(f"{self.name} says Woof!")

    # Creating an Object (Instance)
    my_dog = Dog("Buddy", 3)
    my_dog.bark()  # Output: Buddy says Woof!

----

Classes, Objects, and Attributes
================================

Classes define the structure, and objects represent specific instances containing unique attributes:

*Class Definition**: Declared using the ``class`` keyword followed by a capitalized class name (e.g., ``class Student:``).
- **Object Instantiation**: Objects are created by calling the class name as if it were a function (e.g., ``s1 = Student()``).
- **The __init__() Constructor**: A special initialization method that runs automatically whenever a new object is created.
- **The self Parameter**: Refers to the current instance of the class, allowing access to instance attributes and methods.
- **Attributes**: Variables attached directly to an object that store state data (e.g., ``self.name = name``).

.. code-block:: python

    class Player:
        def __init__(self, username, score):
            self.username = username
            self.score = score

    # Creating two distinct player objects
    p1 = Player("Alex", 100)
    p2 = Player("Sam", 250)

    print(p1.username)  # Output: Alex
    print(p2.score)     # Output: 250

Quiz: Classes, Objects, and Attributes
--------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In Python, a blueprint for creating objects is called a @@class@@.
    2. An individual instance created from a class blueprint is called an @@object@@.
    3. The special method used to initialize object attributes automatically is @@__init__()@@.
    4. Inside class definitions, the @@self@@ parameter represents the specific instance being accessed.
    5. Variables that belong to an object and hold its data are called @@attributes@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a simple class and instantiate an object.

.. ordering::

    class Car:
        def __init__(self, brand):
            self.brand = brand

    my_car = Car("Toyota")
    print(my_car.brand)

----

**Example 2:** Create a Student class with name and grade attributes.

.. ordering::

    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

    s1 = Student("Jordan", 8)
    print(f"{s1.name} is in Year {s1.grade}")

----

**Example 3:** Initialize a Book object and print its title attribute.

.. ordering::

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

    b1 = Book("Python Basics", "Guido")
    print(b1.title)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which keyword is used to define a class in Python?

        [x] class | Correct! The class keyword introduces a new class definition.
        [ ] def | Incorrect. def is used to define functions and methods.
        [ ] object | Incorrect. object is a base type, not a definition keyword.
        [ ] create | Incorrect. No create keyword exists in Python syntax.


    .. multichoice::

        What role does the ``__init__()`` method play in a Python class?

        [x] It serves as the constructor method that automatically initializes new objects | Correct! __init__() runs automatically when instantiating objects.
        [ ] It deletes objects from memory | Incorrect. Deletion is handled by __del__() or garbage collection.
        [ ] It converts class objects into strings | Incorrect. String conversion uses __str__() or __repr__().
        [ ] It prevents methods from modifying attributes | Incorrect. __init__() sets initial attribute values.


    .. multichoice::

        What does the ``self`` parameter represent inside a class method?

        [x] The specific instance of the object calling the method | Correct! self references the current object instance.
        [ ] A global variable shared by all classes | Incorrect. self refers to the local instance.
        [ ] The parent Python module | Incorrect. self is instance-bound.
        [ ] A built-in class counter | Incorrect. self references the instance.


    .. multichoice::

        Given ``class Hero: pass``, how do you instantiate an instance of ``Hero``?

        [x] my_hero = Hero() | Correct! Calling the class name with parentheses creates an instance.
        [ ] my_hero = class.Hero() | Incorrect. Incorrect syntax for object creation.
        [ ] my_hero = new Hero() | Incorrect. 'new' is used in Java/JS, not Python.
        [ ] my_hero = Hero.create() | Incorrect. Object instantiation uses direct class calling syntax Hero().


    .. multichoice::

        What are variables defined inside ``__init__()`` attached to ``self`` called?

        [x] Attributes | Correct! Variables attached to self represent object attributes (properties).
        [ ] Functions | Incorrect. Functions defined inside classes are called methods.
        [ ] Constants | Incorrect. They are instance variables / attributes.
        [ ] Modules | Incorrect. Modules are external code files.


    .. multichoice::

        How do you access the ``age`` attribute of an object named ``cat1``?

        [x] cat1.age | Correct! Attribute access uses dot notation object.attribute.
        [ ] cat1[age] | Incorrect. Bracket syntax is used for dictionaries and sequences.
        [ ] cat1->age | Incorrect. Arrow notation is C/C++ syntax.
        [ ] cat1(age) | Incorrect. Parentheses imply method execution or function call.


    .. multichoice::

        What happens if you omit ``self`` as the first parameter of ``__init__()``?

        [x] Python raises a TypeError when instantiating the class | Correct! Instance methods require self as their first positional parameter.
        [ ] Python automatically inserts self for you | Incorrect. Parameter definition must explicitly include self.
        [ ] The class converts into a list | Incorrect. Syntax/TypeError exceptions occur.
        [ ] Attributes become global variables | Incorrect. A TypeError is raised.


    .. multichoice::

        Can two different objects created from the same class have different attribute values?

        [x] Yes, each object instance maintains its own independent attribute values | Correct! Object instances store unique instance data.
        [ ] No, all objects share identical attribute values permanently | Incorrect. Instances hold separate attribute state.
        [ ] Yes, but only if they are integer values | Incorrect. Any data type can differ per instance.
        [ ] No, changing one instance changes all other instances | Incorrect. Instance attributes are distinct per object.


    .. multichoice::

        What convention is standard for naming Python classes?

        [x] PascalCase (e.g., SmartPhone) | Correct! Class names traditionally use PascalCase capitalization.
        [ ] camelCase (e.g., smartPhone) | Incorrect. Functions and methods often use snake_case, class names use PascalCase.
        [ ] ALL_CAPS (e.g., SMART_PHONE) | Incorrect. ALL_CAPS is reserved for constants.
        [ ] kebab-case (e.g., smart-phone) | Incorrect. Hyphens are invalid in Python identifiers.


    .. multichoice::

        Given ``p = Person("Eva")``, where does the argument ``"Eva"`` get passed inside ``__init__(self, name)``?

        [x] To the name parameter | Correct! "Eva" matches the second positional parameter 'name' (self is passed automatically).
        [ ] To the self parameter | Correct instance self is provided automatically by Python as first argument.
        [ ] To both self and name | Incorrect. Arguments match explicit parameters after self.
        [ ] To a global variable | Incorrect. Assigned to local parameter name.

----

Class Methods and Behavior
==========================

Methods are functions defined inside a class that define what actions or behaviors an object can perform:

- **Method Definition**: Defined using ``def`` inside a class block, always requiring ``self`` as the first parameter.
- **Calling Methods**: Executed using dot notation on an object instance (e.g., ``my_object.method_name()``).
- **Modifying State**: Methods can read or update instance attributes using ``self.attribute_name``.
- **Inter-Method Calls**: A method within a class can invoke another method on the same instance using ``self.other_method()``.

.. code-block:: python

    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
            else:
                print("Insufficient funds!")

    acc = BankAccount("Taylor", 100)
    acc.deposit(50)   # Output: Deposited $50. New balance: $150
    acc.withdraw(30)  # Output: Withdrew $30. Remaining balance: $120

Quiz: Class Methods and Behavior
--------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Functions defined inside a class that define object behavior are called @@methods@@.
    2. Calling a method on an object uses @@dot@@ notation (`object.method()`).
    3. Every instance method must accept @@self@@ as its first parameter.
    4. Methods can modify an object's internal state by updating its @@attributes@@.
    5. To call another method from @@inside@@ a class, use `self.method_name()`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a class with a method that prints a custom greeting.

.. ordering::

    class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello, my name is {self.name}")

    p = Person("Alice")
    p.greet()

----

**Example 2:** Implement a Counter class that increments an attribute.

.. ordering::

    class Counter:
        def __init__(self):
            self.count = 0

        def increment(self):
            self.count += 1

    c = Counter()
    c.increment()
    print(c.count)

----

**Example 3:** Define a GameCharacter class with a take_damage method.

.. ordering::

    class GameCharacter:
        def __init__(self, hp):
            self.hp = hp

        def take_damage(self, dmg):
            self.hp -= dmg

    hero = GameCharacter(100)
    hero.take_damage(20)
    print(hero.hp)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How do you invoke a method named ``speak()`` on an object named ``dog1``?

        [x] dog1.speak() | Correct! Method invocation uses object.method() dot notation.
        [ ] speak(dog1) | Incorrect. Functions are called this way, but instance methods use dot notation.
        [ ] dog1->speak() | Incorrect. C++ arrow operator is invalid in Python.
        [ ] Dog.speak(self) | Incorrect. Preferred instance invocation is dog1.speak().


    .. multichoice::

        When calling ``obj.speak()``, do you explicitly pass an argument for the ``self`` parameter?

        [x] No, Python automatically passes the instance as self in the background | Correct! Python automatically binds the object instance to self.
        [ ] Yes, you must write obj.speak(self) | Incorrect. self is passed implicitly.
        [ ] Yes, you must pass the string "self" | Incorrect. self binding is handled by Python automatically.
        [ ] No, self is only used in C++ | Incorrect. self is used in Python but passed implicitly.


    .. multichoice::

        Given the class below, what does ``c.get_double()`` return?
        ``class Calc: def __init__(self, x): self.x = x; def get_double(self): return self.x * 2``
        ``c = Calc(5)``

        [x] 10 | Correct! Retrieves self.x (5) and multiplies by 2 to return 10.
        [ ] 5 | Incorrect. Multiplies x by 2.
        [ ] 25 | Incorrect. Multiplies by 2, does not square x.
        [ ] None | Incorrect. Explicit return statement yields 10.


    .. multichoice::

        Can a class method accept additional parameters besides ``self``?

        [x] Yes, parameters are listed after self in the method definition | Correct! Methods take additional positional/keyword arguments after self.
        [ ] No, methods can only take self as a parameter | Incorrect. Methods take additional arguments as needed.
        [ ] Yes, but only one extra parameter is allowed | Incorrect. Methods can accept any number of parameters.
        [ ] No, additional data must be passed via global variables | Incorrect. Parameters pass data directly to methods.


    .. multichoice::

        Given ``class Light: def __init__(self): self.is_on = False; def toggle(self): self.is_on = not self.is_on``
        What is ``lamp.is_on`` after executing ``lamp = Light(); lamp.toggle()``?

        [x] True | Correct! toggle() flips False to True.
        [ ] False | Incorrect. toggle() inverted the initial False value.
        [ ] None | Incorrect. Value is Boolean True.
        [ ] AttributeError | Incorrect. Valid class attribute mutation.


    .. multichoice::

        What happens if a method definition misses the ``self`` argument (e.g., ``def display():``)?

        [x] Calling instance.display() raises a TypeError regarding positional arguments | Correct! Python attempts to pass instance implicitly into display(), causing argument count mismatch.
        [ ] It automatically becomes a static function without errors | Incorrect. Raises TypeError unless staticmethod decorator is applied.
        [ ] The method deletes the object | Incorrect. Parameter count mismatch causes TypeError.
        [ ] The program converts display into an attribute | Incorrect. Raises TypeError upon execution.


    .. multichoice::

        How can a method inside a class modify an object's attribute ``self.score``?

        [x] Assigning a new value using self.score = new_value | Correct! Attribute re-assignment updates object state.
        [ ] Re-defining the __init__() method | Incorrect. __init__() runs only during initial object creation.
        [ ] Creating a global variable score | Incorrect. Attributes are updated via self reference.
        [ ] Deleting self.score and recreating the class | Incorrect. Modifying attributes is done via assignment.


    .. multichoice::

        Which statement best describes the difference between a function and a method in Python?

        [x] A method is a function that belongs to a class and operates on instance data via self | Correct! Methods are class-associated functions operating on instances.
        [ ] Functions require self, while methods do not | Incorrect. Opposite is true; instance methods require self.
        [ ] Functions return values, whereas methods cannot return anything | Incorrect. Both can return values.
        [ ] Methods are written outside files, functions inside files | Incorrect. Both are standard Python code constructs.


    .. multichoice::

        What is output by ``class Test: def show(self): return "OK"; t = Test(); print(t.show())``?

        [x] OK | Correct! show() returns string "OK", which gets printed.
        [ ] None | Incorrect. Method explicitly returns "OK".
        [ ] <class 'Test'> | Incorrect. Returns the string "OK".
        [ ] SyntaxError | Incorrect. Syntax is valid.


    .. multichoice::

        How do you call a method ``reset()`` from INSIDE another method of the same class?

        [x] self.reset() | Correct! Inter-method calls use self.method_name().
        [ ] reset() | Incorrect. Requires self reference to locate method in instance scope.
        [ ] class.reset() | Incorrect. Must reference the instance self.
        [ ] super.reset() | Incorrect. super() references parent inheritance classes.

----

Inheritance Basics
==================

**Inheritance** allows a new class (**child / subclass**) to inherit attributes and methods from an existing class (**parent / superclass**):

- **Code Reuse**: Subclasses automatically gain access to parent class methods without duplicating code.
- **Parent Class Syntax**: Specified in parentheses after child class name: ``class ChildClass(ParentClass):``.
- **Method Overriding**: Subclasses can redefine parent methods to customize behavior.
- **The super() Function**: Used inside subclasses to call parent class methods or constructors.

.. code-block:: python

    # Parent Class
    class Animal:
        def __init__(self, name):
            self.name = name

        def make_sound(self):
            print("Generic animal sound")

    # Child Class inheriting from Animal
    class Dog(Animal):
        def make_sound(self):  # Overriding parent method
            print(f"{self.name} barks: Woof!")

    # Creating instances
    generic = Animal("Some Animal")
    dog = Dog("Rex")

    generic.make_sound()  # Output: Generic animal sound
    dog.make_sound()      # Output: Rex barks: Woof!

Quiz: Inheritance Basics
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Creating a class that inherits attributes and methods from another class is called @@inheritance@@.
    2. The class being inherited from is called the @@parent@@ or superclass.
    3. The new class inheriting functionality is called the @@child@@ or subclass.
    4. Redefining a parent class method in a child class is called method @@overriding@@.
    5. To execute a method from the parent class inside a child class, use the @@super()@@ function.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a parent vehicle class and an inheriting car subclass.

.. ordering::

    class Vehicle:
        def move(self):
            print("Moving forward")

    class Car(Vehicle):
        pass

    c = Car()
    c.move()

----

**Example 2:** Override a parent method in a child class.

.. ordering::

    class Bird:
        def fly(self):
            print("Flying high")

    class Penguin(Bird):
        def fly(self):
            print("Penguins cannot fly!")

    p = Penguin()
    p.fly()

----

**Example 3:** Use super() to invoke the parent constructor in a child class.

.. ordering::

    class Person:
        def __init__(self, name):
            self.name = name

    class Student(Person):
        def __init__(self, name, student_id):
            super().__init__(name)
            self.student_id = student_id

    s = Student("Alex", 101)
    print(f"{s.name}: {s.student_id}")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How do you define a child class ``Cat`` that inherits from a parent class ``Animal``?

        [x] class Cat(Animal): | Correct! Parent class name is placed inside parentheses in class header.
        [ ] class Cat extends Animal: | Incorrect. 'extends' is Java/PHP syntax, not Python.
        [ ] class Animal(Cat): | Incorrect. This makes Animal inherit from Cat.
        [ ] class Cat inherits Animal: | Incorrect. Parent class goes inside parentheses.


    .. multichoice::

        What is "method overriding" in object-oriented programming?

        [x] Redefining a method in a child class that already exists in the parent class | Correct! Child definition replaces/overrides parent implementation.
        [ ] Deleting a method from the parent class | Incorrect. Parent class code remains untouched.
        [ ] Calling two methods at the exact same time | Incorrect. It replaces inherited behavior for child instances.
        [ ] Renaming a class constructor | Incorrect. Overriding replaces inherited method behavior.


    .. multichoice::

        What does ``super().__init__()`` do when called inside a child class constructor?

        [x] It calls the __init__() constructor of the parent superclass | Correct! super() accesses parent class methods.
        [ ] It restarts the Python program | Incorrect. Executes parent constructor code.
        [ ] It converts the child class into a parent class | Incorrect. Inherits and initializes parent attributes.
        [ ] It creates a superuser account | Incorrect. super refers to superclass.


    .. multichoice::

        If class ``Shape`` has a method ``draw()`` and child class ``Circle(Shape)`` does NOT define ``draw()``, what happens when ``circle_obj.draw()`` is called?

        [x] Circle automatically inherits and executes draw() from Shape | Correct! Child classes inherit parent methods automatically.
        [ ] Python raises an AttributeError | Incorrect. Method is inherited from parent class.
        [ ] Circle creates an empty draw() method | Incorrect. Executes parent method directly.
        [ ] Program crashes | Incorrect. Inheritance enables parent method fallback.


    .. multichoice::

        Why is inheritance useful in software development?

        [x] It allows developers to reuse existing code and avoid duplicate logic | Correct! Promotes DRY (Don't Repeat Yourself) design principles.
        [ ] It makes code execute 10 times faster | Incorrect. Primary benefit is organization and code reuse.
        [ ] It prevents any class attributes from being altered | Incorrect. Does not restrict mutability.
        [ ] It turns Python code into HTML | Incorrect. Inheritance is an OOP concept.


    .. multichoice::

        Given ``class Parent: pass`` and ``class Child(Parent): pass``, what does ``issubclass(Child, Parent)`` return?

        [x] True | Correct! Child is a valid subclass of Parent.
        [ ] False | Incorrect. Relationship evaluates to True.
        [ ] None | Incorrect. Returns Boolean True.
        [ ] TypeError | Incorrect. issubclass accepts valid class references.


    .. multichoice::

        Can a child class add new methods that do NOT exist in its parent class?

        [x] Yes, child classes can extend parent functionality by adding unique methods | Correct! Subclasses can freely add new methods.
        [ ] No, child classes can only use methods defined in parent class | Incorrect. Subclasses can add new attributes and methods.
        [ ] Yes, but only if parent methods are deleted first | Incorrect. Parent methods remain intact.
        [ ] No, adding new methods raises a SyntaxError | Incorrect. Extending capabilities is a core OOP feature.


    .. multichoice::

        Given ``class A: def speak(self): print("A")`` and ``class B(A): def speak(self): print("B")``, what does ``B().speak()`` print?

        [x] B | Correct! Subclass B overrides speak(), so "B" prints.
        [ ] A | Incorrect. Subclass method overrides parent implementation.
        [ ] A B | Incorrect. Only overridden subclass method runs unless super() is called.
        [ ] None | Incorrect. Method prints "B".


    .. multichoice::

        Which function checks if an object is an instance of a specific class or its subclasses?

        [x] isinstance() | Correct! isinstance(obj, ClassName) evaluates instance type relationships.
        [ ] typecheck() | Incorrect. No built-in named typecheck().
        [ ] isclass() | Incorrect. Python uses isinstance().
        [ ] check_instance() | Incorrect. Built-in function name is isinstance().


    .. multichoice::

        Given ``class Engine: pass`` and ``class Car(Engine): pass``, which statement is accurate?

        [x] Car is the child class and Engine is the parent class | Correct! Car inherits from Engine.
        [ ] Engine is the child class and Car is the parent class | Incorrect. Class in parentheses is the parent.
        [ ] Neither class inherits from the other | Incorrect. Parent-child relationship is declared.
        [ ] Both classes are identical built-in modules | Incorrect. They are custom classes.




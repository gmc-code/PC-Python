=========================================================
Pizza orders Lesson 5: Adding OptionMenu for Quantity
=========================================================

Lesson 5: Adding OptionMenu for Quantity
----------------------------------------
- **Objective**: Add an OptionMenu for selecting the quantity of pizzas.
- **Content**:
  - Introduction to OptionMenu.
  - Creating and positioning the OptionMenu.
  - Updating the total cost based on quantity.

Lesson 5: Adding OptionMenu for Quantity
========================================

Objective
---------
Add an OptionMenu for selecting the quantity of pizzas.

Content
-------

1. Introduction to OptionMenu
   - OptionMenu is a dropdown menu that allows users to select one option from a list.

2. Creating and Positioning the OptionMenu

.. code-block:: python

   quantity_var = tk.StringVar(root)
   quantity_var.set("1")
   quantity_menu = tk.OptionMenu(root, quantity_var, *[str(i) for i in range(1, 31)])
   quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

   - ``quantity_var = tk.StringVar(root)``: Creates a StringVar to hold the selected quantity.
   - ``quantity_var.set("1")``: Sets the default value of the OptionMenu.
   - ``tk.OptionMenu(root, quantity_var, *[str(i) for i in range(1, 31)])``: Creates an OptionMenu with options from 1 to 30.
   - ``.grid(row=3, column=1, padx=10, pady=5, sticky="w")``: Positions the OptionMenu in the grid layout.

3. Updating the Total Cost Based on Quantity
   - You can use the ``trace`` method of ``StringVar`` to call a function whenever the value changes.

.. code-block:: python

   def update_total_cost(*args):
       pizza = pizza_var.get()
       size = size_var.get()
       quantity = int(quantity_var.get())
       if pizza and size:
           total_cost = prices[pizza][size] * quantity
           total_cost_var.set(f"Total cost: ${total_cost}")

   quantity_var.trace("w", update_total_cost)

4. Additional Examples
   - Creating an OptionMenu for drink quantities:

.. code-block:: python

   drink_quantity_var = tk.StringVar(root)
   drink_quantity_var.set("1")
   drink_quantity_menu = tk.OptionMenu(root, drink_quantity_var, *[str(i) for i in range(1, 11)])
   drink_quantity_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")
